import socket


class SSHAudit:
    def __init__(self, target, port=22):
        self.target = target
        self.port = port

    def run(self):
        result = {
            "ssh_open": False,
            "risk": "LOW"
        }

        try:
            sock = socket.socket()
            sock.settimeout(2)
            sock.connect((self.target, self.port))

            banner = sock.recv(1024).decode(errors="ignore")

            result["ssh_open"] = True
            result["banner"] = banner

            # weak version detection heuristic
            if "7.2" in banner or "6." in banner:
                result["risk"] = "MEDIUM"

            sock.close()

        except:
            result["ssh_open"] = False

        return result
