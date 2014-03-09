from django.conf import settings

from ip import get_geo

OPEN_SERVER = getattr(settings, 'OPEN_SERVER_DOMAIN')

def get_environment(request):
    result = dict()
    result.update({'open_server': OPEN_SERVER})
    result.update({'html5': 'Mozilla/5.0' in request.META.get('HTTP_USER_AGENT')})
    result.update({'intranet': get_geo(request) is not None})

    return result
