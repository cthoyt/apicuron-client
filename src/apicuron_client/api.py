# -*- coding: utf-8 -*-

"""Main code for interacting with APICURON."""

import datetime

import pystow
import requests
from pydantic import BaseModel

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

#: The endpoint for updating the description
DESCRIPTION_URL = "https://apicuron.bio.unipd.it/api/update_description"

#: An endpoint for total resubmission
RESUBMISSION_URL = "https://apicuron.org/api/resubmit_activity"


class Term(BaseModel):
    """A term."""

    activity_term: str
    activity_name: str
    activity_category: str
    description: str
    score: int = 50


class Achievement(BaseModel):
    """An achievement."""

    category: str
    name: str
    list_terms: list[str]
    count_threshold: int = 10
    color_code: str = "#055701"


class Description(BaseModel):
    """The description."""

    resource_id: str
    resource_name: str
    resource_uri: str
    resource_url: str
    resource_long_name: str
    resource_description: str
    terms_def: list[Term]
    achievements_def: list[Achievement]

    def update_remote(self) -> requests.Response:
        """Update this description on the APICURON site."""
        return requests.post(
            DESCRIPTION_URL,
            json=self.dict(),
            headers=get_header(),
        )


class Report(BaseModel):
    """A report on a single curation event."""

    curator_orcid: str
    resource_uri: str
    timestamp: datetime.datetime
    #: Corresponds to the :`Term.activity_term` in an entry in `Description.terms_def` list
    activity_term: str


class Submission(BaseModel):
    """A full submission."""

    resource_uri: str
    time_start: datetime.datetime
    time_end: datetime.datetime
    reports: list[Report]

    def update_remote(self) -> requests.Response:
        """Update this resource on the APICURON site."""
        return requests.post(
            RESUBMISSION_URL,
            json=self.dict(),
            headers=get_header(),
        )


def get_header():
    token = pystow.get_config("apicuron", "token")
    if token is None:
        raise RuntimeError("missing APICURON_TOKEN")
    header = {
        "Authorization": f"Bearer {token}",
    }
    return header
