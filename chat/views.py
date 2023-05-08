from django.shortcuts import render
from .models import Chat,Message
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')

def index(request):
    if request.method == 'POST':
        print('This request:'+request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text = request.POST['textmessage'],author=request.user, receiver = request.user, chat = myChat)
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