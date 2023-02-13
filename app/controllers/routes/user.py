import json

from django.http import HttpRequest, HttpResponse

from app.controllers.request_objects import (
    RetrieveMGadgetRequest,
    ListMGadgetRequest,
    CreateMGadgetRequest,
    UpdateMGadgetRequest,
    DeleteMGadgetRequest,
)

from app.usecases import (
    RetrieveMGadgetUseCase,
    ListMGadgetUseCase,
    CreateMGadgetUseCase,
    UpdateMGadgetUseCase,
    DeleteMGadgetUseCase,
)

from app.domain.entity import MGadgetModel
from app.repositories import MGadgetRepository
from app.controllers.routes.base_routes import handle_success
from typing import Optional


def retrieve_mgadget(request: HttpRequest, id: str) -> Optional[HttpResponse]:
    if request.method == 'GET':
        req = RetrieveMGadgetRequest(id)

        repo = MGadgetRepository(MGadgetModel)
        use_case = RetrieveMGadgetUseCase(repo)

        resp = use_case.handle(req)

        return handle_success(resp)


def list_mgadget(request: HttpRequest) -> Optional[HttpResponse]:
    if request.method == 'GET':
        req = ListMGadgetRequest()

        repo = MGadgetRepository(MGadgetModel)
        use_case = ListMGadgetUseCase(repo)

        resp = use_case.handle(req)

        return handle_success(resp)


def create_mgadget(request: HttpRequest) -> Optional[HttpResponse]:
    if request.method == 'POST':
        data = json.loads(request.body)

        req = CreateMGadgetRequest(**data)

        repo = MGadgetRepository(MGadgetModel)
        use_case = CreateMGadgetUseCase(repo)

        resp = use_case.handle(req)

        return handle_success(resp)


def update_mgadget(request: HttpRequest, id: str) -> Optional[HttpResponse]:
    if request.method == 'PUT' or request.method == 'PATCH':
        data = json.loads(request.body)

        req = UpdateMGadgetRequest(data, id)

        repo = MGadgetRepository(MGadgetModel)
        use_case = UpdateMGadgetUseCase(repo)

        resp = use_case.handle(req)

        return handle_success(resp)


def delete_mgadget(request: HttpRequest, id: str) -> Optional[HttpResponse]:
    if request.method == 'DELETE':
        req = DeleteMGadgetRequest(id)

        repo = MGadgetRepository(MGadgetModel)
        use_case = DeleteMGadgetUseCase(repo)

        resp = use_case.handle(req)

        return handle_success(resp)
