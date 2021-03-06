from django.shortcuts import render, get_object_or_404 #render html, context dictionaries and get a single object
from django.http import HttpResponse ,HttpResponseRedirect #generate http responses
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
from PIL import Image
from io import BytesIO
from models import Incident
from forms import Incident_Report_Form
from base64 import b64decode
from django.views.decorators.csrf import csrf_exempt
import os
import json #for json encoding, decoding
from django.utils import timezone
# Create your views here.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
def index(request):
    return HttpResponse("Index")

def show_map(request):
    incident_list = Incident.objects.get_queryset()
    api_key = "AIzaSyBiH87EbyZfS3ekdWJ_BBQ-vlrE8jhU-jk"
    context = {'incident_list':incident_list, "API_KEY":api_key}
    return render(request, 'incident_report/map.html', context)

def incident(request):
    if request.method == 'POST':
        form = Incident_Report_Form(request.POST, request.FILES)
        if form.is_valid():
            print "form was valid"

            cd = form.cleaned_data
            print "cd: ", cd
            i = Incident(description=cd['description'], incident_image=cd['incident_image'], x_gps_coordinate=cd['x_gps_coordinate'],
                         y_gps_coordinate=cd['y_gps_coordinate'], pub_date=timezone.now())
            i.save()
            return HttpResponse("Thank You!")
    else:
        print "Generating form:"
        form = Incident_Report_Form()
    return render(request, 'incident_report/incident.html', {'form':form})


@csrf_exempt
def receive_incident(request):
    #print "LOL"
    print "Request: ", request
    try:
        #print "Data: ", data

        latitude = request.POST['LATITUDE']
        print "got latitude"
        longitude = request.POST['LONGITUDE']
        print "got longitude"
        description = request.POST['DESCRIPTION']
        print "got description"
        image = request.FILES['PHOTOGRAPH']
        today = now()
        print "\n\n\nDescription: ", description
        i = Incident(description=description, incident_image=image, x_gps_coordinate=latitude, y_gps_coordinate=longitude,
                    pub_date=today)
        i.save()
    except:
        print "Could not parse json"



    return HttpResponse("")