"""
Openedx Pipeline Steps for tutorial_hooks_conf.
"""
from openedx_filters import PipelineStep
from openedx_filters.learning.filters import CourseAboutRenderStarted

import logging


log = logging.getLogger()


class OnlyVisibleIfLoggedIn(PipelineStep):
    """
    Filter to make the /courses/<course-ID>/about page visible to logged in users only.
    """


    def run_filter(self, context, template_name):

        log.warning("we are in!")



        return {
            "context": context,
            "template_name": template_name,
        }
