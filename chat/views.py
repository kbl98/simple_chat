from django.shortcuts import render
from .models import Chat,Message

# Create your views here.
def index(request):
    if request.method == 'POST':
        print('This request:'+request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text = request.POST['textmessage'],author=request.user, receiver = request.user, chat = myChat)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request,'chats/index.html',{'username':'Katja','messages':chatMessages})