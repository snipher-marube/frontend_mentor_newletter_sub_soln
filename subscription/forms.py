from django import forms

from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email',)
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if Subscription.objects.filter(email=email).exists():
            raise forms.ValidationError('You are already subscribed.')
        return email