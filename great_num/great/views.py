from django.shortcuts import render ,redirect
import random

def show(request):
    if 'key' not in request.session :
        request.session['key']= random.randint(1, 100)

    if 'count' not in request.session:
        request.session['count']=0
        

    return render(request,'index.html')

def take(request):
    if request.method == "POST":
        guess_number = request.POST['name']
        if int(guess_number) ==  request.session['key']:
            request.session['result'] = 'correct'
            
        elif int(guess_number) >  request.session['key']:
            request.session['result'] = 'high'
            request.session['count']+=1
        else:
            request.session['result'] = 'low'
            request.session['count']+=1

    return redirect('/')

def delete(request):
    if request.method == "POST":
        del request.session['key']
        del request.session['result']
        del request.session['count']

    return redirect('/')


# Create your views here.
