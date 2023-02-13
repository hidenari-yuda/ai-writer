import logging

from app.repositories import MGadgetRepository
from app.domain.exceptions import UnexpectedError
from app.controllers.request_objects import DeleteMGadgetRequest
from app.controllers.response_object import DeleteMGadgetResponse
from ..base_use_case import BaseUseCase


class DeleteMGadgetUseCase(BaseUseCase):
    def __init__(self, repo: MGadgetRepository) -> None:
        self._repo = repo

    def handle(self, request: DeleteMGadgetRequest) -> DeleteMGadgetResponse:
        try:
            self._repo.delete(request.id)
        except Exception as e:
            logging.exception(e)

            raise UnexpectedError('Failed to delete gadget.')

        return DeleteMGadgetResponse()
