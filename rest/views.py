# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView,RedirectView
from rest_framework.generics import GenericAPIView,RetrieveAPIView 
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import generics
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
class PropertyView(APIView):
    def get(self, request):
        properties = Property.objects.all()
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = PropertySerializer(properties, many=True)
        return Response({"properties": serializer.data})
   

    def post(self, request):
        property = request.data.get('property')

        # Create an article from the above data
        serializer = PropertySerializer(data=property)
        if serializer.is_valid(raise_exception=True):
            property_saved = serializer.save()
        return Response({"success": "Property '{}' added successfully".format(property_saved.name)})
        
    def put(self, request, pk):
        saved_property = get_object_or_404(Property.objects.all(), pk=pk)
        data = request.data.get('property')
        serializer = PropertySerializer(instance=saved_property, data=data, partial=True
        if serializer.is_valid(raise_exception=True):
        property_saved = serializer.save()
        return Response({"success": "Property '{}' updated successfully".format(property_saved.name)}) 

def delete(self, request, pk):
    # Get object with this pk
    property = get_object_or_404(   Property.objects.all(), pk=pk)
    property.delete()
    return Response({"message": "Property with id `{}` has been deleted.".format(pk)},status=204)


class UserPropertyListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'location']
   








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







