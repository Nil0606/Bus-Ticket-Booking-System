from django.db import models
from django.contrib.auth.models import User 
class Bus(models.Model):
    bus_name =models.CharField(max_length=30,null=True)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    created=models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return self.bus_name

class Booking(models.Model):
    status_choices=(("BOOKED","BOOKED"),("CANCEL","CANCEL"))
    cost=models.IntegerField()
    tickets=models.IntegerField(default=1)
    bus=models.ForeignKey(to=Bus,on_delete=models.CASCADE)
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(choices=status_choices,max_length=30,default="BOOKED")
    
    def __str__(self):
        return self.user.username+" - "+self.bus.source+" to "+self.bus.dest


