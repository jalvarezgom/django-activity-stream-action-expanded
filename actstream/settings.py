import django
from django.conf import settings
from django.db.models import get_model


SETTINGS = getattr(settings, 'ACTSTREAM_SETTINGS', {})

def get_models():
    """
    Returns a lookup of 'app_label.model': <model class> from ACTSTREAM_SETTINGS['MODELS']
    Only call this right before you need to inspect the models
    """
    models = {}
    for name in SETTINGS.get('MODELS', ('auth.User',)):
        try:
            model = get_model(*name.split('.'))
            assert model
        except (AssertionError, LookupError, RuntimeError):
            continue
        models[name.lower()] = model
    return models

def get_action_manager():
    """
    Returns the class of the action manager to use from ACTSTREAM_SETTINGS['MANAGER']
    """
    mod = SETTINGS.get('MANAGER', 'actstream.managers.ActionManager')
    a, j = mod.split('.'), lambda l: '.'.join(l)
    return getattr(__import__(j(a[:-1]), {}, {}, [a[-1]]), a[-1])()

USE_PREFETCH = SETTINGS.get('USE_PREFETCH',
                            django.VERSION[0] == 1 and django.VERSION[1] >= 4)

FETCH_RELATIONS = SETTINGS.get('FETCH_RELATIONS', True)

GFK_FETCH_DEPTH = SETTINGS.get('GFK_FETCH_DEPTH', 0)

USE_JSONFIELD = SETTINGS.get('USE_JSONFIELD', False)
