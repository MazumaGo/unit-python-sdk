import json
from datetime import datetime, date
from typing import Literal, Optional
from utils import date_utils
from models import *


class IndividualCustomerDTO(object):
    def __init__(self, id: str, created_at: datetime, full_name: FullName, date_of_birth: date, address: Address,
                 phone: Phone, email: str, ssn: Optional[str], passport: Optional[str], nationality: Optional[str],
                 tags: Optional[dict[str, str]], relationships: Optional[dict[str, Relationship]]):
        self.id = id
        self.type = 'individualCustomer'
        self.created_at = created_at
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone = phone
        self.email = email
        self.ssn = ssn
        self.passport = passport
        self.nationality = nationality
        self.tags = tags
        self.relationships = relationships

    @staticmethod
    def from_json_api(_id, _type, attributes, relationships):
        return IndividualCustomerDTO(
            _id, date_utils.to_datetime(attributes["createdAt"]),
            FullName.from_json_api(attributes["fullName"]), date_utils.to_date(attributes["dateOfBirth"]),
            Address.from_json_api(attributes["address"]), Phone.from_json_api(attributes["phone"]),
            attributes["email"], attributes.get("ssn"), attributes.get("passport"), attributes.get("nationality"),
            attributes.get("tags"), relationships
        )


class BusinessCustomerDTO(object):
    def __init__(self, id: str, created_at: datetime, name: str, address: Address, phone: Phone,
                 state_of_incorporation: str, ein: str, entity_type: EntityType, contact: BusinessContact,
                 authorized_users: [AuthorizedUser], dba: Optional[str], tags: Optional[dict[str, str]],
                 relationships: Optional[dict[str, Relationship]]):
        self.id = id
        self.type = 'businessCustomer'
        self.created_at = created_at
        self.name = name
        self.address = address
        self.phone = phone
        self.state_of_incorporation = state_of_incorporation
        self.ein = ein
        self.entity_type = entity_type
        self.contact = contact
        self.authorized_users = authorized_users
        self.dba = dba
        self.tags = tags
        self.relationships = relationships

    @staticmethod
    def from_json_api(_id, _type, attributes, relationships):
        return BusinessCustomerDTO(
            _id, date_utils.to_datetime(attributes["createdAt"]), attributes["name"],
            Address.from_json_api(attributes["address"]), Phone.from_json_api(attributes["phone"]),
            attributes["stateOfIncorporation"], attributes["ein"], attributes["entityType"],
            BusinessContact.from_json_api(attributes["contact"]), AuthorizedUser.from_json_api(attributes["authorizedUsers"]),
            attributes.get("dba"), attributes.get("tags"), relationships
        )

CustomerDTO = Union[IndividualCustomerDTO, BusinessCustomerDTO]


class PatchIndividualCustomerRequest(UnitRequest):
    def __init__(self, customer_id: str, address: Optional[Address] = None, phone: Optional[Phone] = None, email: Optional[str] = None, dba: Optional[str] = None,
                 tags: Optional[dict[str, str]] = None):
        self.customer_id = customer_id
        self.address = address
        self.phone = phone
        self.email = email
        self.dba = dba
        self.tags = tags

    def to_json_api(self) -> dict:
        payload = {
            "data": {
                "type": "individualCustomer",
                "attributes": {}
            }
        }

        if self.address:
            payload["data"]["attributes"]["address"] = self.address

        if self.phone:
            payload["data"]["attributes"]["phone"] = self.phone

        if self.email:
            payload["data"]["attributes"]["email"] = self.email

        if self.dba:
            payload["data"]["attributes"]["dba"] = self.dba

        if self.tags:
            payload["data"]["attributes"]["tags"] = self.tags

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())


class PatchBusinessCustomerRequest(UnitRequest):
    def __init__(self, customer_id: str, address: Optional[Address] = None, phone: Optional[Phone] = None,
                 contact: Optional[BusinessContact] = None, authorized_users: Optional[list[AuthorizedUser]] = None,
                 tags: Optional[dict[str, str]] = None):
        self.customer_id = customer_id
        self.address = address
        self.phone = phone
        self.contact = contact
        self.authorized_users = authorized_users
        self.tags = tags

    def to_json_api(self) -> dict:
        payload = {
            "data": {
                "type": "businessCustomer",
                "attributes": {}
            }
        }

        if self.address:
            payload["data"]["attributes"]["address"] = self.address

        if self.phone:
            payload["data"]["attributes"]["phone"] = self.phone

        if self.contact:
            payload["data"]["attributes"]["contact"] = self.contact

        if self.authorized_users:
            payload["data"]["attributes"]["authorizedUsers"] = self.authorized_users

        if self.tags:
            payload["data"]["attributes"]["tags"] = self.tags

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())

