"""
Openedx receivers for events in the tutorial_hooks_conf.
"""
import requests


def send_enrollment_data_to_webhook(enrollment, **kwargs):
    """
    Listen for the enrollment event data and pass it to google sheets
    """
    envelope = kwargs.get("metadata")
