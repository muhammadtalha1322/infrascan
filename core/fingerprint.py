import requests


class WebFingerprinter:
    def __init__(self, target):
        self.target = target
        self.url = f"http://{target}"

    def run(self):
        result = {
            "server": None,
            "technologies": [],
            "status": None
        }

        try:
            r = requests.get(self.url, timeout=5)

            result["status"] = r.status_code
            result["server"] = r.headers.get("Server", "Unknown")

            headers = str(r.headers).lower()

            # simple tech detection logic
            if "cloudflare" in headers:
                result["technologies"].append("Cloudflare")

            if "wordpress" in r.text.lower():
                result["technologies"].append("WordPress")

            if "php" in headers:
                result["technologies"].append("PHP")

        except:
            result["status"] = "unreachable"

        return result
