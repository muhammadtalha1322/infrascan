import socket


class DNSRecon:
    def __init__(self, domain):
        self.domain = domain

    def run(self):
        result = {
            "ip": None,
            "takeover_risk": False,
            "notes": []
        }

        try:
            ip = socket.gethostbyname(self.domain)
            result["ip"] = ip

            # basic heuristic signals
            if "github.io" in self.domain:
                result["takeover_risk"] = True
                result["notes"].append("Possible GitHub Pages takeover risk")

        except:
            result["notes"].append("DNS resolution failed")

        return result
