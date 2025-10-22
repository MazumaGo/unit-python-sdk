from unit.models import *



class CheckRegisteredAddressRequest(UnitDTO):
    def __init__(
        self,
        street: str,
        city: str,
        state: str,
        postal_code: str,
        country: str,
        street2: Optional[str] = None,
    ):
        self.type = "checkRegisteredAgentAddress"

        self.attributes = {
            "street": street,
            "city": city,
            "state": state,
            "postalCode": postal_code,
            "country": country,
        }

        if street2:
            self.attributes["street2"] = street2

    def to_json_api(self) -> Dict:
        payload = {
            "data": {
                "type": self.type,
                "attributes": self.attributes,
            }
        }
        return payload


class CheckRegisteredAddressResponse(UnitDTO):
    def __init__(
        self,
        is_registered_agent_address: bool,
    ):
        self.type = "checkRegisteredAgentAddress"
        self.is_registered_agent_address = is_registered_agent_address
        self.attributes = {
            "isRegisteredAgentAddress": is_registered_agent_address,
        }

    @staticmethod
    def from_json_api(_id, _type, attributes, relationships):
        return CheckRegisteredAddressResponse(
            attributes.get("isRegisteredAgentAddress"),
        )
