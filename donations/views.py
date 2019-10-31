import stripe

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET

def donation(request):
    key = settings.STRIPE_PUBLISHABLE

    context = {
        'key': key
    }

    return render(request, 'donations/donation.html', context)


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount = 2000,
            currency = 'eur',
            description = 'Job Finder donation charge',
            source = request.POST['stripeToken']
        )
        
        messages.success(request, 'Thank you for your donation!')
        return redirect('jobs')
