# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# Root project views                                                   #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(render(request, 'index.html'))
