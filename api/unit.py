from api.application_resource import ApplicationResource
from api.customer_resource import CustomerResource


class Unit(object):
    def __init__(self, api_url, token):
        self.applications = ApplicationResource(api_url, token)
        self.customers = CustomerResource(api_url, token)
