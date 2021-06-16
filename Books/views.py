from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request, book_id = None):
    response = "You are at the books repository"
    if book_id:
        response += "<br>Viewing Book# %s" % book_id
    return HttpResponse(response)
