#! /usr/bin/env python
__author__ = 'Chris Bell'

# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='home')
]
