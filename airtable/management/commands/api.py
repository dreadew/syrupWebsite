import json
import requests
from django.core.management import BaseCommand


class Command(BaseCommand):
    api_key = "keyC4bESDAqJVg3gb"

    def handle(self, *args, **options):
        api_url = "https://api.airtable.com/v0/appx2CBZANmioaAxs/Tasks?maxRecords=3&view=Grid%20view"
        headers = {
            "Authorization": "Bearer " + self.api_key
        }
        h = requests.get(api_url, headers=headers)
        return h.json()


print(Command().handle())
