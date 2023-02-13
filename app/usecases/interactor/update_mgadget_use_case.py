import logging

from app.repositories import MGadgetRepository
from app.domain.exceptions import UnexpectedError
from app.controllers.request_objects import UpdateMGadgetRequest
from app.controllers.response_object import UpdateMGadgetResponse
from ..base_use_case import BaseUseCase


class UpdateMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository) -> None:
        self._repo = repo

    def handle(self, request: UpdateMGadgetRequest) -> UpdateMGadgetResponse:
        try:
            self._repo.update(request.data)
        except Exception as e:
            logging.exception(e)

            raise UnexpectedError("Failed to update gadget.")

        return UpdateMGadgetResponse()
