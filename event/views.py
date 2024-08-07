from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm

# Create your views here.


def event_list(request):
    """
    Renders a list of past and future shows forthe band
    Displays instances of :model:'event.Event`.
    **Context**
    ``events``
        A list of :model:`event:Event`.
    **Template**
    :template:`event/event_list.html`
    """
    events = Event.objects.all()
    return render(request, 'event/event_list.html', {'events': events})


def event_detail(request, event_id):
    """
    Renders details fort a single show
    Displays an instance of :model:'event.Event`.
    **Context**
    ``event``
        A single :model:`event:Event`.
    **Template**
    :template:`event/event_detail.html`
    """
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'event/event_detail.html', {'event': event})
