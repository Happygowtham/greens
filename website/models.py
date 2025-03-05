from django.db import models

class Room(models.Model):
    room_number = models.CharField(max_length=20, null=True, blank=True)
    room_type = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField(null=True, blank=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='room_images/')
    amenities = models.ManyToManyField('Amenity', null=True, blank=True)

    def __str__(self):
        return self.room_number + " - " + self.room_type

class BookingEnquiry(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    check_in_date = models.DateField(null=True, blank=True)
    check_out_date = models.DateField(null=True, blank=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    customer_phone = models.CharField(max_length=20)
    no_of_adults = models.PositiveIntegerField()
    no_of_children = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.customer_name

class CustomerFeedback(models.Model):
    cust_name = models.CharField(max_length=200)
    cust_image = models.ImageField(upload_to="user_images/", null=True, blank=True)
    rating = models.IntegerField()
    feedback = models.TextField()

    def __str__(self):
        return str(self.rating)

class Amenity(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="amenity/")
    description = models.TextField( null=True, blank=True)

    def __str__(self):
        return self.name

class InformationUpdate(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return str(self.image)
    
class Activity(models.Model):
    description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='activity/')

    def __str__(self):
        return str(self.image)

class Contact(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
