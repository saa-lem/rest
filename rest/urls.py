
from django.urls import path
from .views import PropertyListView,PropertyDetailView,PropertyUpdateView,PropertyDeleteView,UserPropertyListView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('',PropertyListView.as_view(), name = 'home'),
  #  path('property/new/',ProjectCreateView.as_view(), name = 'project-create'),
  path('property/<int:pk>/',PropertyDetailView.as_view(), name = 'property-detail'),
  path('property/<int:pk>/update/',PropertyUpdateView.as_view(), name = 'property-update'),
  path('property/<int:pk>/delete/',PropertyDeleteView.as_view(), name = 'property-delete'),
  path('profile/details/<str:username>/',views.display_profile, name = 'profile-detail'),
  path('user/<str:username>/',UserPropertyListView.as_view(), name = 'user-projects'),
  path('search/',views.hup_find, name = 'search'),
  path('api/properties/', views.PropertyList.as_view()),
  path('api/profiles/', views.ProfileList.as_view()),
  path('api/properties/<int:pk>', views.PropertyDetailView.as_view())

   
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)