from dataclasses import dataclass

from app.utils.serializer import mgadget_serialize
from .base_response import BaseResponse
from app.domain.entity import MGadgetModel
from typing import List, Dict, Any


@dataclass
class ListMGadgetResponse(BaseResponse):
    mgadgets: List[MGadgetModel]

    def to_json(self) -> Dict[str, Any]:
        return {
            'datas': [mgadget_serialize(mgadget) for mgadget in self.mgadgets]
        }
