from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from log.models import Entry

import time

# Create your views here.

def index(request):
    entries = Entry.objects.order_by('-date')
    template = loader.get_template('log/index.html')
    context = RequestContext(request, {
        'entries': entries,
    })
    return HttpResponse(template.render(context))

def add(request):
    entry = Entry()
    entry.date = time
    entry.text = None
    return HttpResponse('Under construction')
