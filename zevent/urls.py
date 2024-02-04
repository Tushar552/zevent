"""
URL configuration for zevent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from users.views import signin,signup,home,signout, user_details_page
from event.views import create_event, view_event, EventSNSListView, EventSNSDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path("",home,name = "home"),
    path("login/",signin,name = "login"),
    path("signup/",signup,name = "signup"),
    path("logout/",signout,name="logout"),
    path('user-details/', user_details_page, name='user_details_page'),
    path('create-event/', create_event, name='create_event'),
    path('view_event/<int:event_id>/', view_event, name='view_event'),
    path('event_sns/', EventSNSListView.as_view(), name='event_sns_list'),
    path('event_sns/<int:pk>/', EventSNSDetailView.as_view(), name='event_sns_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)