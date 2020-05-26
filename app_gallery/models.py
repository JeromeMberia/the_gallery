from django.db import models

# Create your models here.
class Location(models.Model):
    pic_location = models.CharField(max_length=50)

    def __str__(self):
        return self.pic_location

    

    @classmethod
    def get_location(cls, id):
        the_location = Location.objects.get(id=id)
        return the_location


  
   
    
    
    


