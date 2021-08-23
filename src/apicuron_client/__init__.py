# -*- coding: utf-8 -*-

"""A client for interacting with APICURON."""

from .api import (
    Achievement,
    DESCRIPTION_URL,
    Description,
    RESUBMISSION_URL,
    Report,
    Submission,
    Term,
    resubmit_curations,
    submit_description,
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
    # Utilities
    "submit_description",
    "resubmit_curations",
]
