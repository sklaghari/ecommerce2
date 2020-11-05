from django import forms
from .models import Address,Coupon
from cities_light.models import City
class checkoutform(forms.ModelForm):
    class Meta:
        model=Address
        fields=['country','city','street_address']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['city'].queryset=City.objects.none()
        if 'country' in self.data:
            try:
                country=self.data.get('country')
                self.fields['city'].queryset=City.objects.filter(country=country)
            except(ValueError,TypeError):
                print('error in city')
class couponform(forms.Form):
    code=forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Promo Code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))
