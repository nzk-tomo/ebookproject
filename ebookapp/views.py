from django.shortcuts import render
from .models import Ebook
from django.views.generic import CreateView
from django.urls import reverse_lazy
import urllib.request
import requests
from bs4 import BeautifulSoup


class Create(CreateView):
  template_name = 'home.html'
  model = Ebook
  fields = ('url',)
  success_url = reverse_lazy('list')

def bookwalker(request):
  url = 'https://bookwalker.jp/special/'
  list = []
  res = requests.get(url)
  soup = BeautifulSoup(res.content, "html.parser")
  elem = soup.find_all(class_='feature-list-uni')
  for e in elem:
      label = e.a.get("aria-label")
      title = e.h3.getText()
      u = e.a.get("href")
      link = urllib.parse.urljoin(url, u)
      data = e.find(class_='feature-list-date').getText()
      list.append([label, title, link, data])
  context = {'list': list,}
  return render(request, 'bookwalker.html', context)
    
def kobo(request):
  url = 'https://books.rakuten.co.jp/event/e-book/?l-id=tp-main-cp-bnr-more'
  list = []
  res = requests.get(url)
  soup = BeautifulSoup(res.content, "html.parser")
  elem = soup.find_all(class_='isPC sc-cSHVUG jlMtjm')
  for e in elem:
      title = e.a.getText()
      u = e.a.get("href")
      link = urllib.parse.urljoin(url, u)
      data = e.p.getText()
      list.append([title, link, data])
  context = {'list': list,}
  return render(request, 'kobo.html', context)