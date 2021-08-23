# -*- coding: utf-8 -*-

"""A client to `APICURON <https://apicuron.org>`_."""

from .api import (
    Achievement,
    DESCRIPTION_URL,
    Description,
    RESUBMISSION_URL,
    Report,
    Submission,
    Term,
)

__all__ = [
    # URLs
    "DESCRIPTION_URL",
    "RESUBMISSION_URL",
    # Data Models
    "Term",
    "Achievement",
    "Description",
    "Report",
    "Submission",
]
