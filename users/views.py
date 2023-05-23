from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import  BreakFast,Voted
from datetime import datetime
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F
from django.contrib.auth import get_user

def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

@login_required
def votes(request):
    mymembers = BreakFast.objects.all().values()
    template = loader.get_template('users/votes.html')
    context = {
    'mymembers': mymembers,
  }
    return HttpResponse(template.render(context, request))
#Checks if the user has already voted and allows update
@login_required
def update(request, id):
    username= request.user.username
    lastVote=Voted.objects.filter(user=username).values("timeVoted")
    if len(lastVote) == 0:
        BreakFast.objects.filter(id=id).update(voteCount=F("voteCount") + 1)
        newVote=Voted(user=username,timeVoted=datetime.utcnow())
        newVote.save()
        mydata = BreakFast.objects.all().order_by('-voteCount').values()
        messages.success(request, f'Vote cast successfully')
        return render(request, 'users/update.html', {'mydata': mydata})

    if lastVote[0]["timeVoted"].date() == datetime.utcnow().date():
        mydata = BreakFast.objects.all().order_by('-voteCount').values()
        messages.info(request, f'Hello {username},You have already voted today')

        return render(request, 'users/invalidVote.html', {'mydata': mydata})


    BreakFast.objects.filter(id=id).update(voteCount=F("voteCount") + 1)
    Voted.objects.filter(user=username).update(timeVoted=datetime.utcnow())
    mydata = BreakFast.objects.all().order_by('-voteCount').values()
    messages.success(request, f'Hello {username}, Your vote was cast successfully')
    return render(request, 'users/update.html',{'mydata':mydata})
  
@login_required
def standings(request):
    username = request.user.username
    mydata = BreakFast.objects.all().order_by('-voteCount').values()
    messages.info(request, f'Hello {username}')
    return render(request, 'users/invalidVote.html', {'mydata': mydata})

