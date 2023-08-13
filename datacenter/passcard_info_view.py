from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_passcard_visits = []
    visits = Visit.objects.filter(passcard=passcard).order_by('-entered_at')

    for visit in visits:
        duration = visit.duration()
        is_strange = visit.is_long_visit()

        visit_data = {
            'entered_at': visit.entered_at,
            'duration': str(duration),
            'is_strange': is_strange
        }
        this_passcard_visits.append(visit_data)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
