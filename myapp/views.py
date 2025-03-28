from bs4 import BeautifulSoup
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import requests
from webcolors import names
from myapp.models import Link

# Create your views here.
def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')

        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        link_address = []
        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string

            Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

        return render(request, 'result.html', {'data': data})

def clear(request):
    Link.objects.all().delete()
    return render(request,'result.html')