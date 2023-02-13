import logging

from app.repositories import MGadgetRepository
from app.domain.exceptions import UnexpectedError
from app.controllers.request_objects import RetrieveMGadgetRequest
from app.controllers.response_object import RetrieveMGadgetResponse
from ..base_use_case import BaseUseCase


class RetrieveMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository) -> None:
        self._repo = repo

    def handle(self, request: RetrieveMGadgetRequest) -> RetrieveMGadgetResponse:
        mgadget = None

        try:
            mgadget = self._repo.get(request.id)
        except Exception as e:
            logging.exception(e)

            raise UnexpectedError("Failed to retrieve gadget.")

        return RetrieveMGadgetResponse(mgadget)
