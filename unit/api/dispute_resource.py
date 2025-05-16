from unit.api.base_resource import BaseResource
from unit.models.codecs import DtoDecoder
from unit.models.dispute import *



class DisputeResource(BaseResource):
    def __init__(self, api_url, token):
        super().__init__(api_url, token)
        self.resource = "disputes"

    def get(self, dispute_id: str) -> Union[UnitResponse[DisputeDTO], UnitError]:
        response = super().get(f"{self.resource}/{dispute_id}")
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[DisputeDTO](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())
