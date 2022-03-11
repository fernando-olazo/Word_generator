from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    #1 generate word
    word = get_random_string(length=14)
    #2 make counter
    if "counter" not in request.session:
        request.session['counter'] = 0
    
    request.session['counter']+= 1
    request.session['random_w'] = word

    return render(request, "index.html") #get request, and it renders index.html

def r_word(request):
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')