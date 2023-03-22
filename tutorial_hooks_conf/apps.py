"""
tutorial_hooks_conf Django application initialization.
"""

from django.apps import AppConfig


class TutorialHooksConfConfig(AppConfig):
    """
    Configuration for the tutorial_hooks_conf Django application.
    """

    name = 'tutorial_hooks_conf'
    verbose_name = 'tutorial_hooks_conf'
    plugin_app = {
        'settings_config': {
            'lms.djangoapp': {
                'common': {'relative_path': 'settings.common'},
            },
        },
    }

