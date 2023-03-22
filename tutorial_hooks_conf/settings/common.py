"""
Common settings for the tutorial-hooks-conf project.
"""


def plugin_settings(settings):
    """
    Set of plugin settings used by the Open Edx platform.
    More info: https://github.com/edx/edx-platform/blob/master/openedx/core/djangoapps/plugins/README.rst
    """
    # Plugin settings.

    settings.OPEN_EDX_FILTERS_CONFIG = {}

    settings.OPEN_EDX_FILTERS_CONFIG["org.openedx.learning.course_about.render.started.v1"] = {
        "fail_silently": False,
        "pipeline": [
            "tutorial_hooks_conf.pipeline.OnlyVisibleIfLoggedIn"
        ]
    }
    print("this are the settings!!\n\n\n")
