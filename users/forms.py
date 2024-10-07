from allauth.account.forms import SignupForm
from .models import CustomUser
from django import forms


GENDER = (('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'),)

class CustomSignupForm(SignupForm):
    phone_number = forms.CharField(max_length=12, label='Phone Number', required=False)
    gender = forms.MultipleChoiceField(choices=GENDER, required=False)
    photo  = forms.ImageField( required=False)
    
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.phone_number = self.cleaned_data['phone_number']
        user.gender = self.cleaned_data['gender']
        user.photo = self.cleaned_data['photo']
        user.save()
        return user

class UpdateProfileForm(forms.ModelForm):
    model = CustomUser
    fields = ['phone_number', 'gender', 'photo','username']
    
    def __init__(self, *args, **kwargs):
        super(UpdateProfileForm, self).__init__(*args, **kwargs)
        # Optionally customize your form fields here, for example:
        self.fields['gender'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['username'].widget.attrs.update({'class':'form-control'})