
from django.urls import path
from .views import PropertyDetailView,PropertyUpdateView,PropertyDeleteView,UserPropertyListView,PropertyList
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
  path('api/search/',UserPropertyListView.as_view(), name = 'user-projects'),
  path('api/properties/', views.PropertyView.as_view()),
  path('api/properties/<property id>', views.PropertyView.as_view)
  path('api/properties/delete', views.PropertyView.as_view)
  path('api/properties/<int:pk>', views.PropertyView.as_view) 
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)