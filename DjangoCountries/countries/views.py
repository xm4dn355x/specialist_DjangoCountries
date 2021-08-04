# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# Countries application views                                          #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


import json

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .services import get_languages_list, get_alphabet


with open(file='countries/country-by-languages.json', mode='r', encoding='utf-8') as f:
    DATA = json.load(f)


def countries_list(request):
    context = {'countries_list': DATA, 'alphabet': get_alphabet()}
    return HttpResponse(render(request, 'countries/countries_list.html', context))


def countries_list_by_letter(request, letter):
    context = {'countries_list': [country for country in DATA if country['country'][0] == letter]}
    return HttpResponse(render(request, 'countries/countries_list_by_letter.html', context))


def country_detail(request, pk: int):
    context = {'country': DATA[pk]}
    return HttpResponse(render(request, 'countries/country_detail.html', context))


def languages_list(request):
    context = {'languages_list': get_languages_list(DATA), 'alphabet': get_alphabet()}
    return HttpResponse(render(request, 'countries/languages_list.html', context))


def languages_list_by_letter(request, letter):
    context = {'languages_list': [language for language in get_languages_list(DATA) if language[0] == letter]}
    return HttpResponse(render(request, 'countries/languages_list_by_letter.html', context))


def language_detail(request, language: str):
    context = {'countries_list': [country for country in DATA if language in country['languages']]}
    return HttpResponse(render(request, 'countries/language_detail.html', context))


# TODO: Добавить пагинаторы. И не забыть что нужно всегда у пагинатора вызывать get_page()
# TODO: Не забыть переписать, чтоб только GET запросы эти вьюхи обрабатывали, ну или на переписать на class-based views