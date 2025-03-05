from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    amenities = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = '__all__'

    def get_amenities(self, obj):
        return obj.amenities.values_list('name', flat=True)

class BookingEnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingEnquiry
        fields = '__all__'

class CustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFeedback
        fields = '__all__'

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = '__all__'

class InformationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationUpdate
        fields = '__all__'

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()