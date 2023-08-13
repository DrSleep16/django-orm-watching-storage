from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone


def get_non_closed_visits():
    actives = Visit.objects.filter(leaved_at=None)
    now = timezone.localtime()
    non_closed_visits = []
    for active in actives:
        then = timezone.localtime(active.entered_at)
        time_difference = now - then
        total_seconds = time_difference.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)
        formatted_hours = f"{hours:02}"
        formatted_minutes = f"{minutes:02}"
        formatted_seconds = f"{seconds:02}"

        non_closed_visits.append({
            'who_entered': active.passcard.owner_name,
            'entered_at': f'''{timezone.localtime(active.entered_at).strftime('%Y-%m-%d %H:%M:%S')}''',
            'duration': f'''{formatted_hours}:{formatted_minutes}:{formatted_seconds}''',
        })
    return non_closed_visits

def storage_information_view(request):
    non_closed_visits = get_non_closed_visits()
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

