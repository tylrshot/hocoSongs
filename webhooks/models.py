from django.db import models

# Create your models here.

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Song(models.Model):
    name = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    played = models.BooleanField()
    
    FAST = "Fast"
    SLOW = "Slow"
    DANCE = "Dance"
    OTHER = "Other"
    CR = "Christmas"
    
    GENRE = (
        (FAST, 'Fast'),
        (SLOW, 'Slow'),
        (DANCE, 'Dance'),
        (OTHER, 'Other'),
        (CR, 'Christmas')
    )
    
    genre = models.CharField(
        max_length=25,
        choices=GENRE,
        default=FAST,
    )
    
    on_playlist = models.BooleanField(
        default=False,
    )
    
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    author = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    
    #user = models.OneToOneField(User, models.SET_NULL, blank=True, null=True,)
    
class Vote(models.Model):
    name = models.CharField(max_length=200, default='Hoco2018')
    
    song1Win = models.BooleanField(default=False)
    song2Win = models.BooleanField(default=False)
    
    song1 = models.CharField(max_length=200, default='Song1')
    artist1 = models.CharField(max_length=200, default='Artist1')
    song2 = models.CharField(max_length=200, default='Song2')
    artist2 = models.CharField(max_length=200, default='Artist2')
    
    votes1 = models.IntegerField(default=0)
    votes2 = models.IntegerField(default=0)
    
    totalVotes = models.IntegerField(default=0)
    
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    
    winner = models.CharField(max_length=200, blank=True, null=True)
    winnerArtist = models.CharField(max_length=200, blank=True, null=True)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('song_edit', kwargs={'pk': self.pk})
