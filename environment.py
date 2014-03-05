from ip import get_geo

def get_environment(request):
    result = dict()
    result.update({'html5': 'Mozilla/5.0' in request.META.get('HTTP_USER_AGENT')})
    result.update({'intranet': get_geo(request) is not None})

    return result
