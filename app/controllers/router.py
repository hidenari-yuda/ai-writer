import json

from django.http import HttpRequest, HttpResponse

from app.controllers.routes.user import create_mgadget, delete_mgadget, list_mgadget, retrieve_mgadget, update_mgadget

from app.utils.optional import optional_or
from typing import Optional


def mgadget_id_handler(request: HttpRequest, id: str) -> Optional[HttpResponse]:
    resp = None

    resp = optional_or(resp, retrieve_mgadget(request, id))
    resp = optional_or(resp, update_mgadget(request, id))
    resp = optional_or(resp, delete_mgadget(request, id))

    return resp


def mgadget_handler(request: HttpRequest) -> Optional[HttpResponse]:
    resp = None

    resp = optional_or(resp, list_mgadget(request))
    resp = optional_or(resp, create_mgadget(request))

    return resp
