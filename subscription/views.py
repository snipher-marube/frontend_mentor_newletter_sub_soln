from django.shortcuts import render
from django.contrib import messages

from .forms import SubscriptionForm
from .models import Subscription

def home(request):
    context = {}
    return render(request, 'subscription/home.html', context)

def subscribe(request):
    '''form = SubscriptionForm()
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            # check if the email exists in the database
            email=form.cleaned_data['email']
            if Subscription.objects.filter(email=email).exists():
                return render(request, 'Subscription/already_subscribed.html')
            form.save()
            return render(request, 'subscription/success.html',  {'email': email})
        else:
            return render(request, 'subscription/home.html', {'form': form})
    '''

    # uncomment the above code and comment the below code to use the form
    return render(request, 'subscription/success.html')
