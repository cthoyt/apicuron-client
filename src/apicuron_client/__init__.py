# -*- coding: utf-8 -*-

"""A client for interacting with APICURON."""

from .api import (
    Achievement,
    UPDATE_DESCRIPTION_URL,
    Description,
    RESUBMISSION_URL,
    Report,
    Submission,
    Term,
    resubmit_curations,
    submit_description,
    get_reports,
)

__all__ = [
    # URLs
    "UPDATE_DESCRIPTION_URL",
    "RESUBMISSION_URL",
    # Data Models
    "Term",
    "Achievement",
    "Description",
    "Report",
    "Submission",
    # Utilities
    "submit_description",
    "resubmit_curations",
    "get_reports",
]
