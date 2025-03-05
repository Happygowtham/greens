from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import *

router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'enquiry', BookingEnquiryViewSet)
router.register(r'feedback', CustomerFeedbackViewSet)
router.register(r'amenity', AmenityViewSet)
router.register(r'updates', InformationUpdateViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'activity', ActivityViewSet)
router.register(r'contact', ContactViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('send-email/', sendEmail, name='send_email'),
]
