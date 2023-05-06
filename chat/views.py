from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'POST':
        print('This request:'+request.POST['textmessage'])
    return render(request,'chats/index.html',{'username':'Katja'})