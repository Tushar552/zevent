from django.contrib import admin

from users.models import Account,Account_more_info

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