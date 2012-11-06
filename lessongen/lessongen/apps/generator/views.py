

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
from reportlab.lib.units import cm 
import os

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


from PIL import Image, ImageDraw

def getanswer(a,b,operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == 'x':
        return a*b
    else:
        return a/b



def gen_simple_math(request, template_name="generator/basic.html"):
    

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
            response['Content-Disposition'] = 'attachment; filename="math.pdf"'
        
            # Create the PDF object, using the response object as its "file."
            c = canvas.Canvas(response)
            ca = canvas.Canvas(response)
            #for num in ['i', 'ii', 'iii', 'iv', 'v']:
            for num in ['i']:
         
                
                width, height = A4
                c.drawString(width /2.0,1*cm, num)
                ca.drawString(width /2.0,1*cm, num)
                
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
                
                
                data =[]
                irow=[]
                while i < numrows:
                    j = 0
                    jrow= []
                    while j < numcols:
                        jrow.append([random.randrange(int(lowertop),int(uppertop)),random.randrange(int(lowerbottom),int(upperbottom))])
                        j = j +1
                    data.append(jrow)
                    i = i +1  

            
                i = 0
                j = 0
                               
                while i < numrows:
                    j = 0
                    while j < numcols:
                        
                        a = data[i][j][0]
                        print a
                        b = data[i][j][1]
                        print b
                        c.drawString(leftmargin + gapbetweencols*j,height - topmargin - gapbetweenrows*i,"  % 3d" % (a))
                        c.drawString(leftmargin + gapbetweencols*j,height - topmargin -rowinterval - gapbetweenrows*i,"%s% 3d" % (operator,b))
                        c.drawString(leftmargin + gapbetweencols*j,height - topmargin -rowinterval - gapbetweenrows*i,'____')
                        j = j + 1
                    i = i +1
                

                c.drawString(width /2.0 -75, height - topmargin+20, "Created for %s by 1000lessons.com"%name )
                
                # Close the PDF object cleanly, and we're done.
                c.showPage()
                
                i = 0
                j = 0
                               
                while i < numrows:
                    j = 0
                    while j < numcols:
                        
                        a = data[i][j][0]
                       
                        b = data[i][j][1]
                        
                        c.drawString(leftmargin + gapbetweencols*j,height - topmargin - gapbetweenrows*i,"  % 3d" % (a))
                        c.drawString(leftmargin + gapbetweencols*j,height - topmargin -rowinterval - gapbetweenrows*i,"%s% 3d" % (operator,b))
                        c.drawString(leftmargin + gapbetweencols*j,height - topmargin -rowinterval - gapbetweenrows*i,'____')
                
                        c.drawString(leftmargin + gapbetweencols*j,height - topmargin -rowinterval*2 - gapbetweenrows*i ,"  % 3d" % (getanswer(a,b,operator)))
                        j = j + 1
                    i = i +1
                

                c.drawString(width /2.0 -75, height - topmargin+20, "Created for %s by 1000lessons.com"%name )
                
                # Close the PDF object cleanly, and we're done.
                c.showPage()               
                
      
            c.save()
            return response
    else:
        form = SimpleMathForm() # An unbound form

    return render(request, template_name, {
        'form': form,
    })
    

def gen_images(request):


    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="math.pdf"'

    # Create the PDF object, using the response object as its "file."
    v = settings.IMAGE_DIR[0]

    c = canvas.Canvas(response)
    

    
    im =  '%s/%s'%(v,'Gerald_G_Simple_Fruit_(FF_Menu)_13_40.png')
    mask = mask=[0,1,0,1,0,1]
    #im =  '%s/%s'%(v,'matou_apple_white.png')
    #mask=[254,255,254,255,254,255]
    numrows = 7
    k = 1
    width, height = A4
    while k <= numrows:
        i = random.randrange(2,7)
        j = random.randrange(2,7)
        #c.drawString(100, 100, "How many apples? %s"%i)
        x = 1 
        y = 1
        while x <= i:
            #c.drawImage(im, 20 + 30*x, 30, mask=[0,1,0,1,0,1])
            c.drawImage(im, 20 + 30*x, height - 100 *k, mask=mask)
            x = x +1
        c.drawString(70 + 30*x, height - 100 *k + 50, "+")
        while y <= j:
            #c.drawImage(im, 20 + 30*x, 30, mask=[0,1,0,1,0,1])
            c.drawImage(im, 50 + 30*x + 30*y, height - 100 *k, mask=mask)
            y = y +1
        k =k +1
    c.showPage()               
        

    c.save()
    return response
  
INK = "red", "blue", "green", "yellow"

def image(request):

    # ... create/load image here ...
    image = Image.new("RGB", (800, 600), random.choice(INK))
    draw = ImageDraw.Draw(image)

    # ... draw graphics here ...
    for i in range(20):
        x0 = random.randint(10, image.size[0])
        y0 = random.randint(0, image.size[1])
        x1 = random.randint(0, image.size[0])
        y1 = random.randint(0, image.size[1])
        draw.rectangle((x0, y0, x1, y1))

    #draw.flush()
    # serialize to HTTP response
    response = HttpResponse(mimetype="image/png")
    image.save(response, "PNG")
    return response


from maze import Maze
def maze(request):
    size = 20
    try:
        size =  request.GET['size']
        size = int(size)
    except:
        pass
    if size > 30:
        size = 30
        
    m = Maze(size, size)
    image = m.as_image()
    # ... create/load image here ...
#    image = Image.new("RGB", (800, 600), random.choice(INK))
#    draw = ImageDraw.Draw(image)
#
#    # ... draw graphics here ...
#    for i in range(20):
#        x0 = random.randint(10, image.size[0])
#        y0 = random.randint(0, image.size[1])
#        x1 = random.randint(0, image.size[0])
#        y1 = random.randint(0, image.size[1])
#        draw.rectangle((x0, y0, x1, y1))

    #draw.flush()
    # serialize to HTTP response
    response = HttpResponse(mimetype="image/png")
    image.save(response, "PNG")
    return response

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def homepage(request):
    return render(request, 'homepage.html')
    
    
    