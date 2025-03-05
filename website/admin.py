from django.contrib import admin
from .models import *
from .forms import GalleryForm, ActivityForm
from io import BytesIO
from PIL import Image
from django.core.files import File


admin.site.register(Room)
admin.site.register(BookingEnquiry)
admin.site.register(CustomerFeedback)
admin.site.register(Amenity)
admin.site.register(InformationUpdate)

def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=60) 
    new_image = File(im_io, name=image.name)
    return new_image
class GalleryAdmin(admin.ModelAdmin):
    form = GalleryForm

    def save_model(self, request, obj, form, change):
        if 'image' in request.FILES:
            for img in request.FILES.getlist('image'):
                comp_image=compress(img)
                Gallery.objects.create(description=obj.description, image=comp_image)
        else:
            super().save_model(request, obj, form, change)

admin.site.register(Gallery, GalleryAdmin)
class ActivityAdmin(admin.ModelAdmin):
    form = ActivityForm

    def save_model(self, request, obj, form, change):
        if 'image' in request.FILES:
            for img in request.FILES.getlist('image'):
                comp_image=compress(img)
                Activity.objects.create(description=obj.description, image=comp_image)
        else:
            super().save_model(request, obj, form, change)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Contact)

admin.site.site_header = "New Greens Inn"
admin.site.site_title = "New Greens Inn"
admin.site.index_title = "Welcome to Your Admin Panel"
