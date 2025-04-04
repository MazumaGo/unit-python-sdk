from unit.api.base_resource import BaseResource
from unit.models.payment import *
from unit.models.codecs import DtoDecoder, split_json_api_single_response


class PaymentResource(BaseResource):
    def __init__(self, api_url, token):
        super().__init__(api_url, token)
        self.resource = "payments"

    def create(self, request: CreatePaymentRequest, timeout: float = None) -> Union[UnitResponse[PaymentDTO], UnitError]:
        payload = request.to_json_api()
        response = super().post(self.resource, payload, timeout=timeout)
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[PaymentDTO](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def update(self, request: PatchPaymentRequest) -> Union[UnitResponse[PaymentDTO], UnitError]:
        payload = request.to_json_api()
        response = super().patch(f"{self.resource}/{request.payment_id}", payload)
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[PaymentDTO](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def get(self, payment_id: str, include: Optional[str] = "") -> Union[UnitResponse[PaymentDTO], UnitError]:
        response = super().get(f"{self.resource}/{payment_id}", {"include": include})
        if response.status_code == 200:
            data = response.json().get("data")
            included = response.json().get("included")
            return UnitResponse[PaymentDTO](DtoDecoder.decode(data), DtoDecoder.decode(data))
        else:
            return UnitError.from_json_api(response.json())

    def list(self, params: ListPaymentParams = None) -> Union[UnitResponse[List[PaymentDTO]], UnitError]:
        params = params or ListPaymentParams()
        response = super().get(self.resource, params.to_dict())
        if response.status_code == 200:
            data = response.json().get("data")
            included = response.json().get("included")
            return UnitResponse[PaymentDTO](DtoDecoder.decode(data), DtoDecoder.decode(data))
        else:
            return UnitError.from_json_api(response.json())

    def simulate_incoming_ach(self, request: SimulateIncomingAchRequest) -> Union[UnitResponse[PaymentDTO], UnitError]:
        payload = request.to_json_api()
        response = super().post(f"sandbox/{self.resource}", payload)
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            # TODO Fix dto
            _id, _type, attributes, relationships = split_json_api_single_response(data)
            return UnitResponse[SimulateIncomingAchPaymentDTO](SimulateIncomingAchPaymentDTO.from_json_api(_id, _type, attributes, relationships), None)
        else:
            return UnitError.from_json_api(response.json())

    def cancel(self, payment_id: str) -> Union[UnitResponse[PaymentDTO], UnitError]:
        response = super().post(f"{self.resource}/{payment_id}/cancel")
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[PaymentDTO](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())
