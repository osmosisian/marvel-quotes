from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls.base import resolve, reverse



quotes_and_actors = {
     "iron man1": "long live iron man",
    "thor": "earth has wizards now",
    "iron man2": "when did you became expert , last night",
    "iron man3": "i am not iron man",
    "thanos": "stark you will have my respect",
    "spider man4": "i just wanted to be like you mr stark",
    "dr strange": "he is supposed to be the best among us",
    "iron man5": "i wished someone has told you",
    "iron man6": "you can take all my toys and suits but still i am iron man",
    "iron man7": "smart peoples they know how to cover their asses",
    "iron man8": "I want her",
    "iron man9": "i am iron man"
}

def index(request):
    list_items = ""
    quotes = list(quotes_and_actors.keys())
    for quote in quotes:
        capitalized_actor = quote.capitalize()
        quote_path = reverse("quotes",args=[quote])
        list_items += f"<li><a href=\"{quote_path}\">{capitalized_actor}</a></li>"
    response_data = f"<ul>{list_items}</ul>"    
    return HttpResponse(response_data) 
  

def monthly_challange_by_number(request,quote):
    quotes = list(quotes_and_actors.keys())
    if quote > len(quotes):
        return HttpResponseNotFound("<h1>invalid character</h1>")
    redirect_quote = quotes[quote-1]
    redirect_path = reverse("quotes",args=[redirect_quote]) # challange/redirect_month
    return HttpResponseRedirect(redirect_path)

def monthly_challange(request,character):
    try:
        challange_text = quotes_and_actors[character]
        response_data = f"<h1>{challange_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>invalid character</h1>")    