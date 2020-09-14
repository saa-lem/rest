# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView,RedirectView
from rest_framework.generics import GenericAPIView,RetrieveAPIView 
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework import filters
from django.http import HttpResponse
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PropertySerializer, ProfileSerializer
from .models import Property, Profile
from .forms import ProfileUpdateForm, UserUpdateForm, PostPropertyForm
from .models import Profile
from itertools import chain
# Create your views here.
def index(request):
    message = "Welcome to our Site"

    context = {
        "message":message,
    }

    return render(request,'templates/index.html',context)

def display_profile(request,username):
    profile = Profile.objects.get(user__username= username)

    user_properties = Property.objects.get(profile =profile)

    context={
        "profile":profile,
        "user_properties":user_properties
    }
    return render(request,'templates/profile_detail.html',context)

# class PropertyListView(ListView):
    
#     model = Property
#     template_name='index.html'
#     context_object_name ='properties'
class PropertyList(ListModelMixin,GenericAPIView,CreateModelMixin):
    '''
    View that allows you to view and add to the list of all posts
    '''

    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get(self, request, *args, **kwargs):
        '''
        Function that gives you list of all the posts
        '''
        return self.list(request, *args, *kwargs)

    def property(self, request, *args, **kwargs):
        '''
        Function that lets you add a new post to the list of all post
        '''
        return self.create(request,*args, *kwargs)






class PropertyDetailView(RetrieveAPIView):
    '''
    View that allows you to access one item on the list 
    '''
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def get_property(self,pk):
        try:
            return Property.objects.get(pk=pk)
        except Property.DoesNotExist:
            return Http404

    def get(self,request, pk, format=None):
        '''
        Function that retrieves specified post
        '''
        property = self.get_property(pk)
        serializers = PropertySerializer(property)
        return Response(serializers.data)

    def put(self,request,pk, format=None):
        '''
        Function that updates a specified post
        '''
        property = self.get_property(pk)
        serializers = PropertySerializer(property, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        '''
        Function that deletes a specified post
        '''
        property = self.get_property(pk)
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class PropertyUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
     
    model = Property

    fields = ['name','image','description','price','location','size']


    def form_valid(self,form):
        form.instance.profile = self.request.user.profile
        return super().form_valid(form)


    def test_func(self):
        property = self.get_object()

        if self.request.user.profile == property.profile:
            return True

        return False

    def get_redirect_url(self,pk, *args, **kwargs):
        obj = get_object_or_404(Property, pk = pk)
        url= obj.get_absolute_url()
      
      
        return url


class PropertyDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Property
    success_url = ('/')
    def test_func(self):
        property = self.get_object()

        if self.request.user.profile == property.profile:
            return True

        return False

class UserPropertyListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'location']
   




class PropertyList(APIView):
    def get(self, request, format = None):
        all_properties = Property.objects.all()
        serializers = PropertySerializer(all_properties, many = True)
        return Response(serializers.data)



class ProfileList(APIView):
    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        return Response(serializers.data)

def hup_find(request):
    if ('properties' in request.GET) and request.GET['properties']:
        search_term=request.GET.get('properties')
        searched_properties=Property.search_by_name(search_term)
        message = f'{search_term}'
        context = {
            "message": message,
            "properties": searched_properties,
           
        } 
        return render(request, 'search.html',context)
          
    else:
        message= "Search "
        return render(request, 'search.html',{'message':message})


# def search_results(request):
#     if 'search_property' in request.GET and request.GET["search_property"]:
#         search_term = request.GET.get("search_project")
#         searched_properties = Property.objects.filter(name__icontains=search_term)
#         searched_properties = Property.objects.filter(location__icontains=search_term)
#         message=search_term
#         return render(request, "/templatessearch.html", {"projects":searched_properties, "message":message})

#     else:
#         message = "Land not found"

#         return render(request,'templates/search.html',{"message":message})







