from unit.utils import date_utils
from unit.models import *

DisputeStatus = Literal[
    "InvestigationStarted",
    "ProvisionallyCredited",
    "Denied",
    "ResolvedLost",
    "ResolvedWon",
]


class DisputeDTO(object):
    def __init__(
        self,
        id: str,
        source: str,
        status_history: List[Dict[str, str]],
        status: DisputeStatus,
        description: str,
        dispute_type: str,
        created_at: datetime,
        amount: int,
        decision_reason: Optional[str],
        relationships: Optional[Dict[str, Relationship]],
    ):
        self.id = id
        self.type = "dispute"
        self.attributes = {
            "createdAt": created_at,
            "source": source,
            "statusHistory": status_history,
            "status": status,
            "description": description,
            "disputeType": dispute_type,
            "amount": amount,
            "decisionReason": decision_reason,
        }
        self.relationships = relationships

    @staticmethod
    def from_json_api(_id, _type, attributes, relationships):
        return DisputeDTO(
            _id,
            date_utils.to_datetime(attributes["createdAt"]),
            attributes["source"],
            attributes["statusHistory"],
            attributes["status"],
            attributes["description"],
            attributes["disputeType"],
            attributes["amount"],
            attributes.get("decisionReason"),
            relationships,
        )
