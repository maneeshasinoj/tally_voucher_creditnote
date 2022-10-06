from django import forms
from app1.models import paymentvoucher

class paymentvoucherform(forms.ModelForm):
    class Meta:
        model=paymentvoucher
        fields='__all__'