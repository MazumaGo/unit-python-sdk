from typing import Union, List

from unit.api.base_resource import BaseResource
from unit.models import UnitResponse, UnitError
from unit.models.reward import RewardDTO, ListRewardsParams, CreateRewardRequest

from unit.models.codecs import DtoDecoder


class RewardResource(BaseResource):
    def __init__(self, api_url, token):
        super().__init__(api_url, token)
        self.resource = "rewards"

    def create(self, request: CreateRewardRequest) -> Union[UnitResponse[RewardDTO], UnitError]:
        payload = request.to_json_api()
        response = super().post(self.resource, payload)
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[RewardDTO](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def get(self, reward_id: str) -> Union[UnitResponse[RewardDTO], UnitError]:
        response = super().get(f"{self.resource}/{reward_id}")
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[RewardDTO](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())

    def list(self, params: ListRewardsParams = None) -> Union[UnitResponse[List[RewardDTO]], UnitError]:
        params = params or ListRewardsParams()
        response = super().get(self.resource, params.to_dict())
        if super().is_20x(response.status_code):
            data = response.json().get("data")
            return UnitResponse[List[RewardDTO]](DtoDecoder.decode(data), None)
        else:
            return UnitError.from_json_api(response.json())
