from core.dns import DNSRecon
from core.ssh import SSHAudit
from core.fingerprint import WebFingerprinter


class InfraEngine:
    def __init__(self, target):
        self.target = target

    def run(self):
        results = {
            "dns": None,
            "ssh": None,
            "web": None
        }

        print(f"\n[+] Scanning Target: {self.target}\n")

        # 1. DNS / Subdomain / takeover signals
        dns = DNSRecon(self.target)
        results["dns"] = dns.run()

        # 2. SSH security audit (if port open)
        ssh = SSHAudit(self.target)
        results["ssh"] = ssh.run()

        # 3. Web fingerprinting
        web = WebFingerprinter(self.target)
        results["web"] = web.run()

        return results
