from typing import Union, List, Optional

from unit.api.base_resource import BaseResource
from unit.models import UnitResponse, UnitError
from unit.models.codecs import DtoDecoder
from unit.models.repayment import (
    RepaymentDTO,
    CreateRepaymentRequest,
    ListRepaymentParams,
)


class RepaymentResource(BaseResource):
    def __init__(self, api_url, token):
        super().__init__(api_url, token)
        self.resource = "repayments"

    def create(
        self, request: CreateRepaymentRequest
    ) -> Union[UnitResponse[RepaymentDTO], UnitError]:
        payload = request.to_json_api()
        response = super().post(self.resource, payload)
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[RepaymentDTO](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def get(self, repayment_id: str) -> Union[UnitResponse[RepaymentDTO], UnitError]:
        response = super().get(f"{self.resource}/{repayment_id}")
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[RepaymentDTO](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def list(
        self, params: Optional[ListRepaymentParams] = None
    ) -> Union[UnitResponse[List[RepaymentDTO]], UnitError]:
        params = params or ListRepaymentParams()
        response = super().get(self.resource, params.to_dict())
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[List[RepaymentDTO]](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())
