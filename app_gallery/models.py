from django.db import models

# Create your models here.
class Location(models.Model):
    pic_location = models.CharField(max_length=50)

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.pic_location = update
        self.save()

    @classmethod
    def get_location(cls, id):
        the_location = Location.objects.get(id=id)
        return the_location

    def __str__(self):
        return self.pic_location

class Category(models.Model):
    pic_category= models.CharField(max_length=50)

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()
    
    def update_category(self, update):
        self.pic_category = update
        self.save()

    @classmethod
    def get_category(cls, id):
        category = Category.objects.get(id=id)
        return category

    def __str__(self):
        return self.pic_category   

class Image(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'pictures/', default="")
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.name

    
    
    
    


