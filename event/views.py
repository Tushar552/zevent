from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Event, EventDetails, EventPicture
from django.views.generic import ListView, DetailView
from .models import EventSNS






@login_required(login_url='login')
def create_event(request):
    if request.method == 'POST':
        poster = request.FILES.get('event_poster')
        type = request.POST.get('event_type')
        name = request.POST.get('event_name')
        starting_date = request.POST.get('starting_date')
        ending_date = request.POST.get('ending_date')
        summary = request.POST.get('summary')
        description = request.POST.get('description')
        category = request.POST.get('category')
        location = request.POST.get('location')
        user = request.user
        Event.objects.create(
            poster=poster,
            type=type,
            name=name,
            starting_date=starting_date,
            ending_date=ending_date,
            published=False,
            author=user
        )

        EventDetails.objects.create(
            summary=summary,
            description=description,
            category=category,
            location=location,
            event_poster=poster
        )

        # You may also want to handle EventPicture here if needed

        messages.success(request, 'Event created successfully!')
        return redirect('home')

    return render(request, 'create_event.html')


@login_required(login_url='login')
def view_event(request, event_id):
    try:
        event = Event.objects.get(id=event_id)
        event_details = EventDetails.objects.get(event=event)
        event_pictures = EventPicture.objects.filter(author=event)
    except Event.DoesNotExist:
        return HttpResponse('Event not found')

    context = {
        'event': event,
        'event_details': event_details,
        'event_pictures': event_pictures,
    }

    return render(request, 'view_event.html', context)

class EventSNSListView(ListView):
    model = EventSNS
    template_name = 'event_sns_list.html'  # Create this template

class EventSNSDetailView(DetailView):
    model = EventSNS
    template_name = 'event_sns_detail.html'  # Create this template

