from django.contrib import admin

from users.models import Account,Account_more_info, Event, EventDetails

from django.contrib.auth.admin import UserAdmin
 
 
# User More Info
class Account_more_info_admin(admin.StackedInline): # Setting up the model to combine bothh the seprate model to be displaded as one
    model = Account_more_info
    

# User Admin Panel
@admin.register(Account) 
class Account_admin(UserAdmin,admin.ModelAdmin):
    inlines = [Account_more_info_admin] # Combinig the 'Account_more_info' model with the main 'Account' model displayed in admin panel 
    
    class Meta:
        model = Account
        
    # Changing the way of displaying the things in admin panel    
    list_display = [
        "email",
        "date_joined",
        "last_login",
        "is_admin",
        "is_active",
        "is_staff",
        "is_superuser"
    ]
    
    search_fields = [
        "email",
    ]
    
    readonly_fields = (
        "date_joined",
        "last_login",
    )
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
#admin.site.register(Account,Account_admin)
    



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_name', 'starting_date', 'ending_date', 'author')
    list_filter = ('event_type', 'created_on', 'published')
    search_fields = ('event_name', 'event_type', 'author__email')

@admin.register(EventDetails)
class EventDetailsAdmin(admin.ModelAdmin):
    list_display = ('event', 'summary', 'description', 'category', 'location')
    search_fields = ('event__event_name', 'category', 'location')