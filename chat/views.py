from django.shortcuts import render,redirect
from .models import Chat,Message
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import  RegisterForm
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
@login_required(login_url='/login/')

def index(request):
    if request.method == 'POST':
        print('This request:'+request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        new_message=Message.objects.create(text = request.POST['textmessage'],author=request.user, receiver = request.user, chat = myChat)
        serialized_obj=serializers.serialize('json',[new_message,])
        print (JsonResponse(serialized_obj,safe=False))
        return JsonResponse(serialized_obj[1:-1],safe=False)
    
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request,'chats/index.html',{'username':'Katja','messages':chatMessages})

def loginindex(request):
    redirect=request.GET.get('next')
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
        if user:
            login(request, user) 
            return HttpResponseRedirect (request.POST.get('redirect'))
        else:
            return render(request,'chats/loginindex.html',{'notUser':True,'redirect':redirect})
            

    return render(request,'chats/loginindex.html',{'redirect':redirect})

def signindex(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'chats/signindex.html', { 'form': form}) 
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return HttpResponseRedirect ('chat/')
        else:
            return render(request, 'chats/signindex.html', {'form': form})