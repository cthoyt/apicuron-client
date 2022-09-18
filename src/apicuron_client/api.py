# -*- coding: utf-8 -*-

"""Main code for interacting with APICURON."""

import datetime
import logging
from typing import Any, List, Mapping, Optional, Union

import pystow
import requests
from pydantic import BaseModel

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

logger = logging.getLogger(__name__)

BASE_URL = "https://apicuron.org/api"

#: The endpoint for updating the description
SUBMIT_DESCRIPTION_URL = f"{BASE_URL}/submit_description"

#: The endpoint for updating the description
UPDATE_DESCRIPTION_URL = f"{BASE_URL}/update_description"

#: An endpoint for total resubmission
RESUBMISSION_URL = f"{BASE_URL}/resubmit_activity"

#: An endpoint for reports. See
REPORTS_URL = f"{BASE_URL}/reports"


class Term(BaseModel):
    """A term."""

    activity_term: str
    activity_name: str
    activity_category: str
    description: str
    score: int = 50


class Achievement(BaseModel):
    """An achievement."""

    category: str  # TODO this could be restricted with an enum
    name: str
    list_terms: List[str]
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
    terms_def: List[Term]
    achievements_def: List[Achievement]

    def submit_remote(self, *, token: Optional[str] = None) -> requests.Response:
        """Submit this description on the APICURON site."""
        return requests.post(
            SUBMIT_DESCRIPTION_URL,
            json=self.dict(),
            headers=get_header(token=token),
        )

    def update_remote(self, *, token: Optional[str] = None) -> requests.Response:
        """Update this description on the APICURON site."""
        return requests.post(
            UPDATE_DESCRIPTION_URL,
            json=self.dict(),
            headers=get_header(token=token),
        )


class Report(BaseModel):
    """A report on a single curation event."""

    curator_orcid: str
    resource_uri: str
    #: Corresponds to the :`Term.activity_term` in an entry in `Description.terms_def` list
    entity_uri: str
    activity_term: str
    timestamp: Optional[datetime.datetime] = None


class Submission(BaseModel):
    """A full submission."""

    resource_uri: str
    reports: List[Report]
    time_start: Optional[datetime.datetime] = None
    time_end: Optional[datetime.datetime] = None

    def update_remote(self, *, token: Optional[str] = None) -> requests.Response:
        """Update this resource on the APICURON site."""
        return requests.post(
            RESUBMISSION_URL,
            json=self.dict(),
            headers=get_header(token=token),
        )


def get_header(*, token: Optional[str] = None):
    """Get the APICURON header information."""
    token = pystow.get_config("apicuron", "token", passthrough=token, raise_on_missing=True)
    if token is None:
        raise RuntimeError("missing APICURON_TOKEN")
    header = {
        "Authorization": f"Bearer [{token}]",
    }
    return header


def submit_description(
    payload: Union[Description, Mapping[str, Any]], *, token: Optional[str] = None
) -> requests.Response:
    """Submit resource data."""
    if not isinstance(payload, Description):
        payload = Description(**payload)
    reports_res = get_reports(payload.resource_uri, limit=1)
    reports_res.raise_for_status()
    if not reports_res.json():
        logger.info(f"submitting {payload.resource_name} ({payload.resource_uri}) for the first time")
        submit_res = payload.submit_remote(token=token)
        submit_res.raise_for_status()
    return payload.update_remote(token=token)


def resubmit_curations(
    payload: Union[Submission, Mapping[str, Any]], *, token: Optional[str] = None
) -> requests.Response:
    """Submit curations data."""
    if not isinstance(payload, Submission):
        payload = Submission(**payload)
    return payload.update_remote(token=token)


def get_reports(
    uri: str,
    *, limit: Optional[int] = None, token: Optional[str] = None
) -> requests.Response:
    """Get reports."""
    params = {"resource_uri": uri}
    if limit:
        params["limit"] = limit
    return requests.get(
        REPORTS_URL,
        params=params,
        headers=get_header(token=token),
    )
