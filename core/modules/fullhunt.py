import requests

from json.decoder import JSONDecodeError
from core.abstract.module import ModuleBase
from core.database.types.subdomain import Subdomain


class FullHunt(ModuleBase):

    name = "fullhunt"
    version = "0.0.1"
    author = "generatorexit"
    description = "Search subdomains on FullHunt.io"

    def sub_action(self, domain):

        with requests.get(
            "https://fullhunt.io/api/v1/domain/%(domain)s/subdomains"
            % {"domain": domain}
        ) as response:
            json_data = response.json()

        try:
            subdomains = json_data["hosts"]
        except JSONDecodeError:
            return

        for subdomain in subdomains:
            self.database.insert_data(Subdomain(subdomain))

    def execute(self):
        targets = self.database.select_data("domains") or {}

        for _, target in targets.items():
            self.respect_threads_run((target.value,))
