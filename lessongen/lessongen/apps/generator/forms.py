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
    name = forms.CharField(initial='My School', help_text="Your School's name")
    lowertop = forms.IntegerField(initial = '10', help_text='the lower limit of the range of number for the top part of the sum')
    uppertop = forms.IntegerField(initial = '20', help_text='the upper limit of the range of number for the top part of the sum ')
    lowerbottom = forms.IntegerField(initial = '5', help_text='the lower limit of the range of number for the bottom part of the sum')
    upperbottom = forms.IntegerField(initial= '10', help_text='the upper limit of the range of number for the top part of the sum')
    operator = forms.ChoiceField(choices=GENDER)
    
    send = forms.BooleanField(required=False)  
