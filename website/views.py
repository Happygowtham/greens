from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from rest_framework.decorators import api_view
from rest_framework.response import Response


load_dotenv()
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = []  

class BookingEnquiryViewSet(viewsets.ModelViewSet):
    queryset = BookingEnquiry.objects.all()
    serializer_class = BookingEnquirySerializer
    permission_classes = [IsAuthenticated] 

class CustomerFeedbackViewSet(viewsets.ModelViewSet):
    queryset = CustomerFeedback.objects.all()
    serializer_class = CustomerFeedbackSerializer
    permission_classes = [IsAuthenticated] 

class AmenityViewSet(viewsets.ModelViewSet):
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    permission_classes = [IsAuthenticated] 

class InformationUpdateViewSet(viewsets.ModelViewSet):
    queryset = InformationUpdate.objects.all()
    serializer_class = InformationUpdateSerializer
    permission_classes = [IsAuthenticated] 

class GalleryViewSet(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    permission_classes = [IsAuthenticated] 

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [] 

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated] 
    

@api_view(['POST'])
def sendEmail(request):
    if request.method == 'POST':
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data.get('subject')
            message = serializer.validated_data.get('message')
            
            if subject and message:
                try:
                    print(os.getenv("EMAIL_TO_USER"))
                    send_mail(subject, message, os.getenv("EMAIL_HOST_USER"), [os.getenv("EMAIL_TO_USER")])
                    return JsonResponse({'message': 'Email sent successfully'})
                except Exception as e:
                    return JsonResponse({'error': str(e)}, status=500)   
        else:
            return Response(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)