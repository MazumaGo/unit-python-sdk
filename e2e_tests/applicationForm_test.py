import os
from unit import Unit
from unit.models.applicationForm import CreateApplicationFormRequest

token = os.environ.get('TOKEN')
client = Unit("https://api.s.unit.sh", token)
card_types = ["individualDebitCard", "businessDebitCard", "individualVirtualDebitCard", "businessVirtualDebitCard"]

def create_create_application_form():
    request = CreateApplicationFormRequest(tags={"userId": "106a75e9-de77-4e25-9561-faffe59d7814"},
                                           allowed_application_types=["Individual"])
    return client.applicationForms.create(request)

def test_create_application_form():
    response = create_create_application_form()
    assert response.data.type == "applicationForm"

def test_get_application_form():
    application_form_id = create_create_application_form().data.id
    response = client.applicationForms.get(application_form_id, "application")
    assert response.data.type == "applicationForm"

def test_list_application_form():
    response = client.applicationForms.list()
    for app in response.data:
        assert app.type == "applicationForm"


