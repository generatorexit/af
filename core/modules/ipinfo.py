import requests

from core.abstract.module import ModuleBase
from core.database.types.ip_address import IPAddress


class IPInfo(ModuleBase):

    name = "ipinfo"
    version = "0.0.1"
    author = "generatorexit"
    description = "Gather informations on IP addresses"
    category = "scanning"

    def sub_action(self, ip_address: IPAddress):
        with requests.get(f"https://ipinfo.io/{ip_address.value}/json") as response:
            json_data = response.json()

        if response.status_code != 200 or "bogon" in json_data:
            return

        _id = self.database.get_id_by_value(ip_address.value)

        try:
            self.database.update_subdata("ip_addrs", _id, "org", json_data["org"])

            self.database.update_subdata(
                "ip_addrs",
                _id,
                "loc",
                {"country": json_data["country"], "city": json_data["city"]},
            )
        except KeyError:
            pass

    def execute(self):
        targets = self.database.select_data("ip_addrs") or {}

        for _, target in targets.items():
            self.respect_threads_run((target,))
