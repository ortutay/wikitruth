from django.shortcuts import render, redirect
from django.views import View

from forms import NewClaimForm, ResponseForm
from models import Claim, Response


class NewClaimsView(View):
    def get(self, request):
        form = NewClaimForm()
        return render(request, 'claims/new.html', { 'form': form })

    def post(self, request):
        form = NewClaimForm(request.POST)
        print 'got claim', form, form.is_valid()
        if not form.is_valid():
            print 'not valid, errors:', form.errors
            return render(request, 'claims/new.html', { 'form': form })
        claim = Claim.objects.create(thesis=form.cleaned_data['thesis'])
        response = Response.objects.create(
            user=request.user,
            claim=claim,
            direction=form.cleaned_data['direction'],
            body=form.cleaned_data['body'])
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
        claim = Claim.objects.get(pk=id)
        context = {
            'claim': claim,
            'form': form,
            'responses': claim.response_set.all(),
        }
        return render(request, 'claims/detail.html', context)

    def post(self, request, id):
        form = ResponseForm(request.POST)
        print 'POST form', form
        claim = Claim.objects.get(pk=id)
        return redirect('claim-detail', id=claim.id)
