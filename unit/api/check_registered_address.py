from unit.api.base_resource import BaseResource
from unit.models.application import *
from unit.models.check_registered_address import CheckRegisteredAddressRequest, CheckRegisteredAddressResponse
from unit.models.codecs import DtoDecoder


class CheckRegisteredAddressResource(BaseResource):
    def __init__(self, api_url, token):
        super().__init__(api_url, token)
        self.resource = "applications/check-registered-agent-address"

    def create(self, request: CheckRegisteredAddressRequest) -> Union[UnitResponse[CheckRegisteredAddressResponse], UnitError]:
        payload = request.to_json_api()
        response = super().post(self.resource, payload)

        if response.ok:
            data = response.json().get("data")
            return UnitResponse[CheckRegisteredAddressResponse](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

