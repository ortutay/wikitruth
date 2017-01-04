from django.shortcuts import render, redirect
from django.views import View

from forms import NewClaimForm
from models import Claim


class ClaimsView(View):
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
        print 'new claim:', claim
        return redirect('new-claim')
