from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    


class SimpleMathForm(forms.Form):
       
    GENDER = (
       ("+", ("+")),
       ("-", ("-")), 
       ("x", ("x")),
       ("/", ("/")),
   )
    name = forms.CharField()
    lowertop = forms.IntegerField()
    uppertop = forms.IntegerField()
    lowerbottom = forms.IntegerField()
    upperbottom = forms.IntegerField()
    operator = forms.ChoiceField(choices=GENDER)
    
    send = forms.BooleanField(required=False)  
