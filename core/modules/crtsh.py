import requests

from core.abstract.module import ModuleBase
from core.database.types.subdomain import Subdomain


class CRT(ModuleBase):

    name = "crtsh"
    version = "0.0.1"
    author = "generatorexit"
    description = "Search subdomains on CRT.sh"
    keywords = ["crtsh", "certificates", "subdomains", "scanning"]

    def sub_action(self, domain):
        with requests.get(
            "https://crt.sh/?q=%(domain)s&output=json" % {"domain": domain}
        ) as response:
            json_data = response.json()

        if not json_data:
            return

        for data in json_data:
            value = data.get("name_value", None)

            if value is None:
                continue

            parts = value.split("\n")

            for part in parts:
                if not part.endswith(domain) or part.startswith("*") or part == domain:
                    continue

                self.database.insert_data(Subdomain(part))

    def execute(self):
        targets = self.database.select_data("domains") or {}

        for _, target in targets.items():
            self.respect_threads_run((target.value,))
