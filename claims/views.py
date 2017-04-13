import pprint

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response as ApiResponse

from forms import NewClaimForm, ResponseForm, ReplyForm
from models import Claim, Response
from serializers import ClaimSerializer

pp = pprint.PrettyPrinter(indent=2)


class NewClaimsView(View):
    def get(self, request):
        form = NewClaimForm()
        return render(request, 'claims/new.html', { 'form': form })

    def post(self, request):
        form = NewClaimForm(request.POST)
        if not form.is_valid():
            return render(request, 'claims/new.html', { 'form': form })
        claim = Claim.objects.create(thesis=form.cleaned_data['thesis'])
        add_response_to_claim(request, claim, form.cleaned_data)
        return redirect('claim-detail', id=claim.id)


def claims(request):
    claims = Claim.objects.all()
    context = {
        'claims': claims,
    }
    return render(request, 'claims/index.html', context)


class ClaimDetail(View):
    def get(self, request, id):
        form = ResponseForm()
        reply_form = ReplyForm()
        claim = Claim.objects.get(pk=id)
        context = {
            'claim': claim,
            'form': form,
            'reply_form': reply_form,
            'responses': claim.response_set.all(),
        }
        return render(request, 'claims/detail.html', context)

    def post(self, request, id):
        form = ResponseForm(request.POST)
        if not form.is_valid():
            return render(request, 'claims/detail.html', { 'form': form })

        claim = Claim.objects.get(pk=id)
        add_response_to_claim(request, claim, form.cleaned_data)

        return redirect('claim-detail', id=claim.id)


class ResponseDetail(View):
    def get(self, request, id):
        form = ReplyForm()
        response = Response.objects.get(pk=id)
        context = {
            'form': form,
            'response': response,
        }
        return render(request, 'claims/responses/detail.html', context)

    def post(self, request, id):
        form = ReplyForm(request.POST)
        response = Response.objects.get(pk=id)
        if not form.is_valid():
            print 'errors', form.errors
            context = {
                'form': form,
                'response': response,
            }
            return render(request, 'claims/responses/detail.html', context)

        parent = None
        if form.cleaned_data['comment_id']:
            parent = Comment.objects.get(pk=form.cleaned_data['comment_id'])

        print 'trying to make...'

        Comment.objects.create(
            user=request.user,
            response=response,
            parent=parent,
            body=form.cleaned_data['body'])

        print 'made comment, redirecting'

        return redirect('response-detail', id=response.id)


@api_view(['GET'])
def search(request):
    claims = Claim.objects.all()
    serializer = ClaimSerializer(claims, many=True)
    return ApiResponse({ 'results': serializer.data })


def add_response_to_claim(request, claim, cleaned_data):
    response = Response.objects.create(
        user=request.user,
        claim=claim,
        direction=cleaned_data['direction'],
        body=cleaned_data['body'])
    for claim_id in cleaned_data['citations']:
        cited_claim = Claim.objects.get(pk=claim_id)
        response.citations.add(cited_claim)
    response.save()
