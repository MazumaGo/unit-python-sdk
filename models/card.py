import json
from datetime import datetime, date
from typing import Literal, Optional
from utils import date_utils
from models import *

CardStatus = Literal["Inactive", "Active", "Stolen", "Lost", "Frozen", "ClosedByCustomer", "SuspectedFraud"]


class IndividualDebitCardDTO(object):
    def __init__(self, id: str, created_at: datetime, last_4_digits: str, expiration_date: str, status: CardStatus,
                 shipping_address: Optional[Address], design: Optional[str], relationships: Optional[dict[str, Relationship]]):
        self.id = id
        self.type = "individualDebitCard"
        self.created_at = created_at
        self.last_4_digits = last_4_digits
        self.expiration_date = expiration_date
        self.status = status
        self.shipping_address = shipping_address
        self.design = design
        self.relationships = relationships

    @staticmethod
    def from_json_api(_id, _type, attributes, relationships):
        return IndividualDebitCardDTO(
            _id, date_utils.to_datetime(attributes["createdAt"]), attributes["last4Digits"], attributes["expirationDate"],
            attributes["status"], attributes.get("shippingAddress"), attributes.get("design"), relationships
        )


class BusinessDebitCardDTO(object):
    def __init__(self, id: str, created_at: datetime, last_4_digits: str, expiration_date: str, ssn: str,
                 full_name: FullName, date_of_birth: date, address: Address, phone: Phone, email: str, status: CardStatus,
                 passport: Optional[str], nationality: Optional[str], shipping_address: Optional[Address], design: Optional[str],
                 relationships: Optional[dict[str, Relationship]]):
        self.id = id
        self.type = "businessDebitCard"
        self.created_at = created_at
        self.last_4_digits = last_4_digits
        self.expiration_date = expiration_date
        self.ssn = ssn
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone = phone
        self.email = email
        self.status = status
        self.passport = passport
        self.nationality = nationality
        self.shipping_address = shipping_address
        self.design = design
        self.relationships = relationships

    def from_json_api(_id, _type, attributes, relationships):
        return BusinessDebitCardDTO(
            _id, date_utils.to_datetime(attributes["createdAt"]), attributes["last4Digits"], attributes["expirationDate"],
            attributes["ssn"], attributes["fullName"], attributes["dateOfBirth"], attributes["address"], attributes["phone"],
            attributes["email"], attributes["status"],  attributes.get("passport"), attributes.get("nationality"),
            attributes.get("shippingAddress"), attributes.get("design"), relationships
        )


class IndividualVirtualDebitCardDTO(object):
    def __init__(self, id: str, created_at: datetime, last_4_digits: str, expiration_date: str, status: CardStatus,
                 relationships: Optional[dict[str, Relationship]]):
        self.id = id
        self.type = "individualVirtualDebitCard"
        self.created_at = created_at
        self.last_4_digits = last_4_digits
        self.expiration_date = expiration_date
        self.status = status
        self.relationships = relationships

    @staticmethod
    def from_json_api(_id, _type, attributes, relationships):
        return IndividualVirtualDebitCardDTO(
            _id, date_utils.to_datetime(attributes["createdAt"]), attributes["last4Digits"], attributes["expirationDate"],
            attributes["status"], relationships
        )


class BusinessVirtualDebitCardDTO(object):
    def __init__(self, id: str, created_at: datetime, last_4_digits: str, expiration_date: str, ssn: str,
                 full_name: FullName, date_of_birth: date, address: Address, phone: Phone, email: str, status: CardStatus,
                 passport: Optional[str], nationality: Optional[str], relationships: Optional[dict[str, Relationship]]):
        self.id = id
        self.type = "businessVirtualDebitCard"
        self.created_at = created_at
        self.last_4_digits = last_4_digits
        self.expiration_date = expiration_date
        self.ssn = ssn
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone = phone
        self.email = email
        self.status = status
        self.passport = passport
        self.nationality = nationality
        self.relationships = relationships

    def from_json_api(_id, _type, attributes, relationships):
        return BusinessVirtualDebitCardDTO(
            _id, date_utils.to_datetime(attributes["createdAt"]), attributes["last4Digits"], attributes["expirationDate"],
            attributes["ssn"], attributes["fullName"], attributes["dateOfBirth"], attributes["address"], attributes["phone"],
            attributes["email"], attributes["status"],  attributes.get("passport"), attributes.get("nationality"), relationships
        )


Card = Union[IndividualDebitCardDTO, BusinessDebitCardDTO, IndividualVirtualDebitCardDTO, BusinessVirtualDebitCardDTO]


class CreateIndividualDebitCard(object):
    def __init__(self, relationships: dict[str, Relationship], shipping_address: Optional[Address] = None,
                 design: Optional[str] = None, idempotency_key: Optional[str] = None, tags: Optional[dict[str, str]] = None):
        self.shipping_address = shipping_address
        self.design = design
        self.idempotency_key = idempotency_key
        self.tags = tags
        self.relationships = relationships

    def to_json_api(self) -> dict:
        payload = {
            "data": {
                "type": "individualDebitCard",
                "attributes": {},
                "relationships": self.relationships
            }
        }

        if self.shipping_address:
            payload["data"]["attributes"]["shippingAddress"] = self.shipping_address

        if self.design:
            payload["data"]["attributes"]["design"] = self.design

        if self.idempotency_key:
            payload["data"]["attributes"]["idempotencyKey"] = self.idempotency_key

        if self.tags:
            payload["data"]["attributes"]["tags"] = self.tags

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())

class CreateBusinessDebitCard(object):
    def __init__(self, full_name: FullName, date_of_birth: date, address: Address, phone: Phone, email: str,
                 status: CardStatus, shipping_address: Optional[Address], ssn: Optional[str], passport: Optional[str],
                 nationality: Optional[str], design: Optional[str], idempotency_key: Optional[str],
                 tags: Optional[dict[str, str]], relationships: Optional[dict[str, Relationship]]):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone = phone
        self.email = email
        self.status = status
        self.shipping_address = shipping_address
        self.ssn = ssn
        self.passport = passport
        self.nationality = nationality
        self.design = design
        self.idempotency_key = idempotency_key
        self.tags = tags
        self.relationships = relationships

    def to_json_api(self) -> dict:
        payload = {
            "data": {
                "type": "businessDebitCard",
                "attributes": {
                    "fullName": self.full_name,
                    "dateOfBirth": self.date_of_birth,
                    "address": self.address,
                    "phone": self.phone,
                    "email": self.email,
                },
                "relationships": self.relationships
            }
        }

        if self.shipping_address:
            payload["data"]["attributes"]["shippingAddress"] = self.shipping_address

        if self.ssn:
            payload["data"]["attributes"]["ssn"] = self.ssn

        if self.passport:
            payload["data"]["attributes"]["passport"] = self.passport

        if self.nationality:
            payload["data"]["attributes"]["nationality"] = self.nationality

        if self.design:
            payload["data"]["attributes"]["design"] = self.design

        if self.idempotency_key:
            payload["data"]["attributes"]["idempotencyKey"] = self.idempotency_key

        if self.tags:
            payload["data"]["attributes"]["tags"] = self.tags

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())

class CreateIndividualVirtualDebitCard(object):
    def __init__(self, relationships: dict[str, Relationship], idempotency_key: Optional[str] = None,
                 tags: Optional[dict[str, str]] = None):
        self.idempotency_key = idempotency_key
        self.tags = tags
        self.relationships = relationships

    def to_json_api(self) -> dict:
        payload = {
            "data": {
                "type": "individualVirtualDebitCard",
                "attributes": {},
                "relationships": self.relationships
            }
        }

        if self.idempotency_key:
            payload["data"]["attributes"]["idempotencyKey"] = self.idempotency_key

        if self.tags:
            payload["data"]["attributes"]["tags"] = self.tags

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())


class CreateBusinessVirtualDebitCard(object):
    def __init__(self, full_name: FullName, date_of_birth: date, address: Address, phone: Phone, email: str,
                 status: CardStatus, ssn: Optional[str], passport: Optional[str], nationality: Optional[str],
                 idempotency_key: Optional[str], tags: Optional[dict[str, str]],
                 relationships: Optional[dict[str, Relationship]]):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.address = address
        self.phone = phone
        self.email = email
        self.status = status
        self.ssn = ssn
        self.passport = passport
        self.nationality = nationality
        self.idempotency_key = idempotency_key
        self.tags = tags
        self.relationships = relationships

    def to_json_api(self) -> dict:
        payload = {
            "data": {
                "type": "businessVirtualDebitCard",
                "attributes": {
                    "fullName": self.full_name,
                    "dateOfBirth": self.date_of_birth,
                    "address": self.address,
                    "phone": self.phone,
                    "email": self.email,
                },
                "relationships": self.relationships
            }
        }

        if self.ssn:
            payload["data"]["attributes"]["ssn"] = self.ssn

        if self.passport:
            payload["data"]["attributes"]["passport"] = self.passport

        if self.nationality:
            payload["data"]["attributes"]["nationality"] = self.nationality

        if self.idempotency_key:
            payload["data"]["attributes"]["idempotencyKey"] = self.idempotency_key

        if self.tags:
            payload["data"]["attributes"]["tags"] = self.tags

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())


CreateCardRequest = Union[CreateIndividualDebitCard, CreateBusinessDebitCard, CreateIndividualVirtualDebitCard, CreateBusinessVirtualDebitCard]

class PatchIndividualDebitCard(object):
    def __init__(self,card_id: str, shipping_address: Optional[Address] = None, design: Optional[str] = None, tags: Optional[dict[str, str]] = None):
        self.card_id = card_id
        self.shipping_address = shipping_address
        self.design = design
        self.tags = tags

    def to_json_api(self) -> dict:
        payload = {
            "data": {
                "type": "individualDebitCard",
                "attributes": {},
            }
        }

        if self.shipping_address:
            payload["data"]["attributes"]["shippingAddress"] = self.shipping_address

        if self.design:
            payload["data"]["attributes"]["design"] = self.design

        if self.tags:
            payload["data"]["attributes"]["tags"] = self.tags

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())


class PatchBusinessDebitCard(object):
    def __init__(self, card_id: str, shipping_address: Optional[Address] = None, address: Optional[Address] = None,
                 phone: Optional[Phone] = None, email: Optional[str] = None, design: Optional[str] = None,
                 tags: Optional[dict[str, str]] = None):
        self.card_id = card_id
        self.shipping_address = shipping_address
        self.design = design
        self.tags = tags

    def to_json_api(self) -> dict:
        payload = {
            "data": {
                "type": "businessDebitCard",
                "attributes": {},
            }
        }

        if self.shipping_address:
            payload["data"]["attributes"]["shippingAddress"] = self.shipping_address

        if self.address:
            payload["data"]["attributes"]["address"] = self.address

        if self.phone:
            payload["data"]["attributes"]["phone"] = self.phone

        if self.email:
            payload["data"]["attributes"]["email"] = self.email

        if self.design:
            payload["data"]["attributes"]["design"] = self.design

        if self.tags:
            payload["data"]["attributes"]["tags"] = self.tags

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())

class PatchIndividualVirtualDebitCard(object):
    def __init__(self, card_id: str, tags: Optional[dict[str, str]] = None):
        self.card_id = card_id
        self.tags = tags

    def to_json_api(self) -> dict:
        payload = {
            "data": {
                "type": "individualVirtualDebitCard",
                "attributes": {},
            }
        }

        if self.tags:
            payload["data"]["attributes"]["tags"] = self.tags

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())

class PatchBusinessVirtualDebitCard(object):
    def __init__(self, card_id: str, address: Optional[Address] = None, phone: Optional[Phone] = None, email: Optional[str] = None,
                 tags: Optional[dict[str, str]] = None):
        self.card_id = card_id
        self.address = address
        self.phone = phone
        self.email = email
        self.tags = tags

    def to_json_api(self) -> dict:
        payload = {
            "data": {
                "type": "businessVirtualDebitCard",
                "attributes": {},
            }
        }

        if self.address:
            payload["data"]["attributes"]["address"] = self.address

        if self.phone:
            payload["data"]["attributes"]["phone"] = self.phone

        if self.email:
            payload["data"]["attributes"]["email"] = self.email

        if self.tags:
            payload["data"]["attributes"]["tags"] = self.tags

        return payload

    def __repr__(self):
        json.dumps(self.to_json_api())

PatchCardRequest = Union[PatchIndividualDebitCard, PatchBusinessDebitCard, PatchIndividualVirtualDebitCard, PatchBusinessVirtualDebitCard]

class ReplaceCardRequest(object):
    def __init__(self, shipping_address: Optional[Address] = None):
        self.shipping_address = shipping_address

    def to_json_api(self) -> dict:
        payload = {
            "data": {
                "type": "replaceCard",
                "attributes": {},
            }
        }

        if self.shipping_address:
            payload["data"]["attributes"]["shippingAddress"] = self.shipping_address

        return payload

        def __repr__(self):
            json.dumps(self.to_json_api())