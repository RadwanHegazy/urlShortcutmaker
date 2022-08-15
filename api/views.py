from django.shortcuts import render
from app.models import Link
from django.http import JsonResponse
# Create your views here.



def user_details (request) :
    getLinks = Link.objects.filter(user=request.user).values('link')
    return JsonResponse(list(getLinks),safe=False)

def get_hash_by_link (request) :
    link = request.GET['link']
    hash = Link.objects.filter(link=link).values('hash_code','visitors')
    return JsonResponse(data=list(hash),safe=False)