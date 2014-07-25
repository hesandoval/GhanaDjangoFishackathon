from django import forms

class Incident_Report_Form(forms.Form):
    description = forms.CharField()
    incident_image = forms.ImageField()
    x_gps_coordinate = forms.DecimalField()
    y_gps_coordinate = forms.DecimalField()