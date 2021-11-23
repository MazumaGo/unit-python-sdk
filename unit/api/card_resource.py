from unit.api.base_resource import BaseResource
from unit.models.card import *
from unit.models.codecs import DtoDecoder


class CardResource(BaseResource):
    def __init__(self, api_url, token):
        super().__init__(api_url, token)
        self.resource = "cards"

    def create(self, request: CreateCardRequest) -> Union[UnitResponse[Card], UnitError]:
        payload = request.to_json_api()
        response = super().post(self.resource, payload)
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[Card](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def report_stolen(self, card_id: str) -> Union[UnitResponse[Card], UnitError]:
        response = super().post(f"{self.resource}/{card_id}/report-stolen")
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[Card](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def report_lost(self, card_id: str) -> Union[UnitResponse[Card], UnitError]:
        response = super().post(f"{self.resource}/{card_id}/report-lost")
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[Card](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def close(self, card_id: str) -> Union[UnitResponse[Card], UnitError]:
        response = super().post(f"{self.resource}/{card_id}/close")
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[Card](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def freeze(self, card_id: str) -> Union[UnitResponse[Card], UnitError]:
        response = super().post(f"{self.resource}/{card_id}/freeze")
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[Card](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def unfreeze(self, card_id: str) -> Union[UnitResponse[Card], UnitError]:
        response = super().post(f"{self.resource}/{card_id}/unfreeze")
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[Card](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def replace(self, card_id: str, shipping_address: Optional[Address]) -> Union[UnitResponse[Union[IndividualDebitCardDTO, BusinessDebitCardDTO]], UnitError]:
        request = ReplaceCardRequest(shipping_address)
        payload = request.to_json_api()
        response = super().post(f"{self.resource}/{card_id}/replace", payload)
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[Union[IndividualDebitCardDTO, BusinessDebitCardDTO]](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def update(self, request: PatchCardRequest) -> Union[UnitResponse[Card], UnitError]:
        payload = request.to_json_api()
        response = super().patch(f"{self.resource}/{request.card_id}", payload)
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[Card](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def get(self, card_id: str, include: Optional[str] = "") -> Union[UnitResponse[Card], UnitError]:
        response = super().get(f"{self.resource}/{card_id}")
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            included = response.json().get("included")
            return UnitResponse[Card](DtoDecoder.decode(data), DtoDecoder.decode(included))
        else:
            return UnitError.from_json_api(response.json())

    def list(self, offset: int = 0, limit: int = 100) -> Union[UnitResponse[list[Card]], UnitError]:
        response = super().get(self.resource, {"page[limit]": limit, "page[offset]": offset})
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            included = response.json().get("included")
            return UnitResponse[Card](DtoDecoder.decode(data), DtoDecoder.decode(included))
        else:
            return UnitError.from_json_api(response.json())