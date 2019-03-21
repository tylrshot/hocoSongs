# Create your views here.

import copy, json, datetime
#from .models import Message
from django.utils import timezone

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
#from django.core.urlresolvers import get_callable, reverse
from django.http import StreamingHttpResponse
from django.views.generic import View
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from webhooks.models import Song, Vote

import random

#from .models import Message

Var1 = 0
Var2 = 0

Numbers = []

Song1 = 'Song1'
Song2 = 'Song2'
Artist1 = 'Artist1'
Artist2 = 'Artist2'
songNum1 = 1
genre = 'Fast'

songWinner = 'Winning Song'
artistWinner = 'Winning Artist'
winningVotes = 0
totalVotes = 0

def calcWinner():
    global Var1
    global Var2
    global Numbers
    global songWinner
    global artistWinner
    global winningVotes
    global totalVotes
    
    global Song1
    global Song2
    global Artist1
    global Artist2
    global genre
    
    if Var1 == Var2:
        Var1 += 1
        Var2 -= 1
        
    if Var1 > Var2:
        #Remove Song1
        if Song1 != 'Song1':
            obj = Song.objects.get(name=Song1)
            obj.played = True
            obj.save()

        winningVotes = Var1
        totalVotes = winningVotes + Var2
        songWinner = Song1
        artistWinner = Artist1
        
        if Song1 != 'Song1':
            v = Vote(song1Win=True, song1=Song1, song2=Song2, artist1=Artist1, artist2=Artist2, votes1=Var1, votes2=Var2, totalVotes=totalVotes, winner=songWinner, winnerArtist=artistWinner)

            v.save()
        
    elif Var2 > Var1:
        #Remove Song2
        if Song2 != 'Song2':
            obj = Song.objects.get(name=Song2)
            obj.played = True
            obj.save()
        
        winningVotes = Var2
        totalVotes = winningVotes + Var1
        songWinner = Song2
        artistWinner = Artist2
        
        if Song2 != 'Song2':
            v = Vote(song2Win=True, song1=Song1, song2=Song2, artist1=Artist1, artist2=Artist2, votes1=Var1, votes2=Var2, totalVotes=totalVotes, winner=songWinner, winnerArtist=artistWinner)

            v.save()
        
    else:
        print("CRASH")
        
    print("---------------------")
    print("Winner:")
    print(songWinner)
    print(artistWinner)
    print("Votes:")
    print(winningVotes)
    print("Total Votes:")
    print(totalVotes)
    print("---------------------")

def newSong(newGenre):
    global Var1
    global Var2
    global Numbers
    
    global Song1
    global Song2
    global Artist1
    global Artist2
    global genre
    
    Var1 = 0
    Var2 = 0
    Numbers = []
    
    genre = newGenre
    
    songNamesList = Song.objects.filter(genre=genre, played=False).values_list('name', flat=True)
    artistNamesList = Song.objects.filter(genre=genre, played=False).values_list('artist', flat=True)
    
    numSongs = songNamesList.count()
    print(numSongs)
    
    songNamesList = list(songNamesList)
    artistNamesList = list(artistNamesList)
    
    songNum1 = random.randint(0, int(numSongs-1))
    songNum2 = random.randint(0, int(numSongs-1))
    x = 1
    while songNum2 == songNum1 and x < 25:
        x += 1
        songNum2 = random.randint(0, int(numSongs-1))
        
    Song1 = songNamesList[songNum1]
    Artist1 = artistNamesList[songNum1]
    Song2 = songNamesList[songNum2]
    Artist2 = artistNamesList[songNum2]
    
    if x == 25:
        Song2 = "No Additional Songs"
        Artist2 = "No Additional Artist"
    
    print(songNamesList)
    print(artistNamesList)
    
    print(Song1)
    print(Artist1)
    print(Song2)
    print(Artist2)
    
@csrf_exempt
#@require_POST
def inbound(request):
    global Song1
    global Song2
    
    data = json.loads(request.body)
    
    text = data.get('text')
    number = data.get('msisdn')
    
    print(number)
    print(text)
    
    global Numbers
    global Var1
    global Var2
    
    
    if text == 'reset-pop':
            print('reset pop')
            newSong('Pop')
            number = 0
            
    elif text == 'reset-rap':
            print('reset rap')
            newSong('Rap')  
            number = 0
            
    elif text == 'reset-rock':
            print('reset rock')
            newSong('Rock')  
            number = 0
    
    if number == '17065318630':
        number = random.randint(1,99999)
    
    if number in Numbers:
        print('Number already voted.')
        
    else:
        Numbers.append(number)

        if text == '1':
            Var1 += 1

        if text == '2':
            Var2 += 1

        #print('# of 1:')
        print(Song1 + "-" + Artist1)
        print(Var1)
        #print('# of 2:')
        print(Song2 + "-" + Artist2)
        print(Var2)
    
    
    
    
    #print(json.loads(request.body))

    return HttpResponse('Hi!')


    return HttpResponse('OK')



def inboundView(request):
    
    
    return HttpResponse('OK')


def index(request):
    
    global Song1
    global Song2
    global Artist1
    global Artist2
    global genre
    global Var1
    global Var2
    
    totalVotes = Var1 + Var2
    
    if totalVotes == 0:
        totalVotes+=1
    
    newVar1 = (Var1/totalVotes) * 100
    newVar2 = (Var2/totalVotes) * 100
    
    newVar1 = round(newVar1, -1)
    newVar2 = round(newVar2, -1)
    
    args = {'song1':Song1, 'artist1':Artist1, 'song2':Song2, 'artist2':Artist2, 'genre':genre, 'Var1':newVar1, 'Var2':newVar2}
    
    #args = {'songInfo': [song1, artist1, song2, artist2]}
    
    return render(request, 'webhooks/index.html', args)

def fast(request):
    global songWinner
    global artistWinner2
    global winningVotes
    global totalVotes
    global genre
    
    calcWinner()
    newSong('Fast')
    
    args = {'songWinner':songWinner, 'artistWinner':artistWinner, 'winningVotes':winningVotes, 'totalVotes':totalVotes, 'genre':genre}
    
    return render(request, 'webhooks/songAdminGenre.html', args)

def slow(request):
    global songWinner
    global artistWinner
    global winningVotes
    global totalVotes
    global genre
    
    calcWinner()
    newSong('Slow')
    
    args = {'songWinner':songWinner, 'artistWinner':artistWinner, 'winningVotes':winningVotes, 'totalVotes':totalVotes, 'genre':genre}
    
    return render(request, 'webhooks/songAdminGenre.html', args)

def dance(request):
    global songWinner
    global artistWinner
    global winningVotes
    global totalVotes
    global genre
    
    calcWinner()
    newSong('Dance')
    
    args = {'songWinner':songWinner, 'artistWinner':artistWinner, 'winningVotes':winningVotes, 'totalVotes':totalVotes, 'genre':genre}
    
    return render(request, 'webhooks/songAdminGenre.html', args)

def other(request):
    global songWinner
    global artistWinner
    global winningVotes
    global totalVotes
    global genre
    
    calcWinner()
    newSong('Other')
    
    args = {'songWinner':songWinner, 'artistWinner':artistWinner, 'winningVotes':winningVotes, 'totalVotes':totalVotes, 'genre':genre}
    
    return render(request, 'webhooks/songAdminGenre.html', args)

def christmas(request):
    global songWinner
    global artistWinner
    global winningVotes
    global totalVotes
    global genre
    
    calcWinner()
    newSong('Christmas')
    
    args = {'songWinner':songWinner, 'artistWinner':artistWinner, 'winningVotes':winningVotes, 'totalVotes':totalVotes, 'genre':genre}
    
    return render(request, 'webhooks/songAdminGenre.html', args)

@csrf_exempt
def songAdmin(request):
    global songWinner
    global artistWinner
    global winningVotes
    global totalVotes
    global genre
    
    global Song1
    global Song2
    global Artist1
    global Artist2
    global Var1
    global Var2
    
    args = {'songWinner':songWinner, 'artistWinner':artistWinner, 'winningVotes':winningVotes, 'totalVotes':totalVotes, 'genre':genre, 'song1':Song1, 'artist1':Artist1, 'song2':Song2, 'artist2':Artist2, 'Var1':Var1, 'Var2':Var2}
    
    return render(request, 'webhooks/songAdmin.html', args)

def reset81273(request):
    qs = Song.objects.all()
    qs.update(played=False)
    
    return render(request, 'webhooks/songAdminGenre.html')

#skyblue h1


