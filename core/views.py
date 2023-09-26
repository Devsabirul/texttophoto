from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests

def home(request):
  query = request.GET.get('q')
  if query:
    return redirect(f'/ai-images/{query}')

  return render(request,"core/index.html")


def gallery(request,query):
  api = query.split() 
  api_query = "+".join(api)

  url = f'https://lexica.art/api/v1/search?q={api_query}'
  data = requests.get(url).json()
  all_datas = data['images']
  return render(request,"core/gallery.html",locals())
    
