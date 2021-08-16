from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Contact


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


def getfirst_name(request):
    if request.method == 'POST':
        model = Contact(request.POST)
        if model.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        model = Contact()

    return render(request, 'contact.html', {'model': model} )
