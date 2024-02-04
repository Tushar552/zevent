from django.contrib import admin

from .models import Event, EventDetails, EventPicture, EventSNS


class Event_details_admin(admin.StackedInline):
    model = EventDetails
    
class Event_picture_admin(admin.StackedInline):
    model = EventPicture
    
class Event_sns_admin(admin.StackedInline):
    model = EventSNS


@admin.register(Event)
class Event_admin(admin.ModelAdmin):
    inlines = [Event_details_admin,Event_picture_admin,Event_sns_admin]
    
    class Meta:
        model = Event
    
    list_display = ( 
        'name',
        'starting_date', 
        'ending_date',
        'id', 
        'author'
    )
    
    search_fields = (
        'name',
        'type',
        'author'
    )
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



