from django.shortcuts import render,HttpResponse
import requests
API_KEY='f9785d4fd9a9465294753cf13218a97f'


def home(request):
	
	country = request.GET.get('country')
	category = request.GET.get('category')
	if country:
		url=f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
		response = requests.get(url)
		data = response.json()
		data=data['articles']
		
	else:
		url=f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
		response = requests.get(url)
		data = response.json()
		data=data['articles']
	return render(request,'home.html',{'data':data})
