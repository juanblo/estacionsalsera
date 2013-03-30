#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render


def home(request):
    """Reders the home page
    """
    return render(request, 'home.html', {})
