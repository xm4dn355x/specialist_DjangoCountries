# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
#                                                                      #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2021 Michael Nikitenko                                 #
#                                                                      #
########################################################################


def get_languages_list(countries: list):
    return sorted(set([language for country in countries for language in country['languages']]))


def get_alphabet():
    return [chr(i).upper() for i in range(ord('a'), ord('z') + 1)]
