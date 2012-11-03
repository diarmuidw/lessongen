

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, QueryDict
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import date_based
from django.conf import settings
from django.contrib import messages


from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas



#import pinax.apps.account

if "notification" in settings.INSTALLED_APPS:
    from notification import models as notification
else:
    notification = None

from django import forms
from forms import SimpleMathForm

        
import datetime
import string
import random

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.http import HttpResponse
@login_required
def gen_simple_math(request, template_name="generator/basic.html"):
    print 'gen_math'

    if request.method == 'POST': # If the form has been submitted...
        form = SimpleMathForm(request.POST) # A form bound to the POST data
        if form.is_valid():

            name = form.cleaned_data['name']
            lowertop = form.cleaned_data['lowertop']
            uppertop = form.cleaned_data['uppertop']
            lowerbottom = form.cleaned_data['lowerbottom']
            upperbottom = form.cleaned_data['upperbottom']
            operator = form.cleaned_data['operator']


            response = HttpResponse(mimetype='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="mathn.pdf"'
        
            # Create the PDF object, using the response object as its "file."
            c = canvas.Canvas(response)
                    
            width, height = A4
  
         
            rowinterval = 18
            topmargin = 50
            leftmargin = 55
            colinterval = 50
            numcols = 9
            numrows = 13
            
            
            gapbetweenrows = 60
            gapbetweencols = 60
  
       
            i = 0
            j = 0
            while i < numrows:
                j = 0
                while j < numcols:
                    
                    a = random.randrange(int(lowertop),int(uppertop))
                    b = random.randrange(int(lowerbottom),int(upperbottom))
                    c.drawString(leftmargin + gapbetweencols*j,height - topmargin - gapbetweenrows*i,"  % 3d" % (a))
                    c.drawString(leftmargin + gapbetweencols*j,height - topmargin -rowinterval - gapbetweenrows*i,"%s% 3d" % (operator,b))
                    c.drawString(leftmargin + gapbetweencols*j,height - topmargin -rowinterval - gapbetweenrows*i,'____')
                    j = j + 1
                i = i +1
            

            c.drawString(width /2.0, height - topmargin+20, "Hello, %s"%name)
            
            # Close the PDF object cleanly, and we're done.
            c.showPage()
            c.save()
            return response
    else:
        form = SimpleMathForm() # An unbound form

    return render(request, template_name, {
        'form': form,
    })
    


def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response