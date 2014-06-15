from django.db import models
from django.utils.timezone import now

now_time = now()

# Create your models here.
class Incident(models.Model):
    description = models.CharField(max_length = 1000)
    pub_date = models.DateTimeField(default = now_time, blank = True)
    incident_image = models.ImageField(upload_to='documents/')
    x_gps_coordinate = models.DecimalField(max_digits= 10, decimal_places = 3)
    y_gps_coordinate = models.DecimalField(max_digits = 10, decimal_places = 3)

    def __unicode__(self):
        return "X-Coordinate: " + str(self.x_gps_coordinate) + " Y-Coordinate: " + str(self.y_gps_coordinate)
