# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# Countries application router                                         #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from django.urls import path

from . import views

urlpatterns = [
    path('', views.countries_list, name='countries_list'),
    path('/countries-list/', views.countries_list),
    path('/country/<int:pk>', views.country_detail, name='country_detail'),
    path('/countries/letter/<str:letter>', views.countries_list_by_letter, name='countries_by_letter'),
    path('/languages-list/', views.languages_list, name='languages_list'),
    path('/languages/letter/<str:letter>', views.languages_list_by_letter, name='languages_by_letter'),
    path('/language/<str:language>', views.language_detail, name='language_detail'),
]