from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader, Template, Context
from django.core.urlresolvers import reverse

from log.models import Entry

from datetime import datetime

# Create your views here.

def index(request):
    entries = Entry.objects.order_by('-date')
    template = loader.get_template('log/index.html')
    context = RequestContext(request, {
        'entries_list': entries,
    })
    return HttpResponse(template.render(context))

def view(request):
    entry_id = int(request.GET['entry_id'])
    entries = Entry.objects.order_by('-id')
    found_entry = None
    for entry in entries:
        if (entry.id == entry_id):
            found_entry = entry
    if (found_entry == None):
        return HttpResponse('Entry not found!')
    return HttpResponse(Template('{{ text|linebreaksbr }}').render(Context({'text': found_entry.text})))

def new(request):
    template = loader.get_template('log/new.html')
    return render(request, 'log/new.html', { })

def add(request):
    entry = Entry()
    entry.date = datetime.now()
    entry.text = request.POST['text']
    entry.save()
    return HttpResponseRedirect(reverse('index'))
