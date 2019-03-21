# Register your models here.

from django.contrib import admin
from webhooks.models import Song, Vote

admin.site.site_header = 'Homecoming Song Vote'

#admin.site.register(Song)

def genre_fast(modeladmin, request, queryset):
    queryset.update(genre='Fast')
genre_fast.short_description = "Genre = Fast"

def genre_slow(modeladmin, request, queryset):
    queryset.update(genre='Slow')
genre_slow.short_description = "Genre = Slow"

def genre_dance(modeladmin, request, queryset):
    queryset.update(genre='Dance')
genre_dance.short_description = "Genre = Dance"

def genre_other(modeladmin, request, queryset):
    queryset.update(genre='Other')
genre_other.short_description = "Genre = Other"

def reset(modeladmin, request, queryset):
    queryset.update(played=False)
reset.short_description = "Reset Played to False"

def un_reset(modeladmin, request, queryset):
    queryset.update(played=True)
un_reset.short_description = "Reset Played to True"

def is_on_playlist(modeladmin, request, queryset):
    queryset.update(on_playlist=True)
is_on_playlist.short_description = "Song on Playlist"



# Define the admin class
class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'artist', 'played', 'on_playlist', 'created')
    list_filter = ('genre', 'played', 'artist', 'on_playlist', 'author')
    actions = [genre_fast, genre_slow, genre_dance, genre_other, reset, un_reset, is_on_playlist]
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
    
    exclude = ('author',)

    pass

class VoteAdmin(admin.ModelAdmin):
    list_display = ('totalVotes', 'winner', 'song1Win', 'song1', 'artist1', 'votes1', 'song2Win', 'song2', 'artist2', 'votes2', 'created')
    pass

# Register the admin class with the associated model
admin.site.register(Song, SongAdmin)
admin.site.register(Vote, VoteAdmin)

