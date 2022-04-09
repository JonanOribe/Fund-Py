from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Portfolio

# Create your views here.
@api_view(['GET','POST','DELETE'])
def portfolio_list(request):
    # GET list of portfolios, POST a new portfolio, DELETE all portfolios
    return 0

@api_view(['GET', 'PUT', 'DELETE'])
def portfolio_detail(request, pk):
    # find portfolio by pk (id)
    try: 
        portfolio = Portfolio.objects.get(pk=pk) 
    except Portfolio.DoesNotExist: 
        return JsonResponse({'message': 'The portfolio does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE portfolio
    
        
@api_view(['GET'])
def portfolio_list_published(request):
    # GET all published portfolio
    return 0
