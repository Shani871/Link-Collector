from bs4 import BeautifulSoup
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
import requests
from urllib.parse import urlparse, urljoin
from myapp.models import Link
import csv

def get_category(url, text):
    url = url.lower()
    text = (text or "").lower()
    
    if any(k in url or k in text for k in ['social', 'facebook', 'twitter', 'linkedin', 'instagram', 'github']):
        return 'Social Media'
    elif any(k in url or k in text for k in ['blog', 'article', 'news', 'post']):
        return 'Articles/Blogs'
    elif any(k in url or k in text for k in ['docs', 'api', 'help', 'support']):
        return 'Documentation'
    elif any(k in url or k in text for k in ['shop', 'store', 'cart', 'buy', 'price']):
        return 'E-commerce'
    elif any(k in url or k in text for k in ['video', 'youtube', 'vimeo', 'watch']):
        return 'Media'
    return 'General'

# Create your views here.
def scrape(request):
    if request.method == "POST":
        site = request.POST.get('site', '')
        if not site or not site.strip():
             return HttpResponseRedirect('/')
             
        if not site.startswith('http'):
            site = 'https://' + site

        try:
            page = requests.get(site, timeout=10)
            soup = BeautifulSoup(page.text, 'html.parser')

            for link in soup.find_all('a'):
                address = link.get('href')
                if not address or address.startswith('#') or address.startswith('javascript:'):
                    continue
                
                # Convert relative to absolute
                address = urljoin(site, address)
                name = link.text.strip() if link.text else (link.get('title', 'Unknown').strip() if link.get('title') else "Unnamed Link")
                
                domain = urlparse(address).netloc
                category = get_category(address, name)

                Link.objects.create(
                    address=address, 
                    name=name, 
                    category=category,
                    domain=domain
                )
        except Exception as e:
            print(f"Error scraping {site}: {e}")
            
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all().order_by('-created_at')
        
        # Simple stats for the dashboard
        total_links = data.count()
        categories_dict = {}
        for link in data:
            categories_dict[link.category] = categories_dict.get(link.category, 0) + 1
            
        # Format categories for chart
        cat_labels = list(categories_dict.keys())
        cat_counts = list(categories_dict.values())

        return render(request, 'result.html', {
            'data': data,
            'total_links': total_links,
            'cat_labels': cat_labels,
            'cat_counts': cat_counts
        })

def clear(request):
    Link.objects.all().delete()
    return HttpResponseRedirect('/')

def export_links(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="links.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Name', 'URL', 'Category', 'Domain', 'Date Added'])

    links = Link.objects.all().values_list('id', 'name', 'address', 'category', 'domain', 'created_at')
    for link in links:
        writer.writerow(link)

    return response