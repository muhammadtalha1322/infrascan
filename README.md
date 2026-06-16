# InfraScan

InfraScan is a lightweight infrastructure reconnaissance tool that performs basic analysis of a target’s DNS resolution, SSH exposure, and web server fingerprinting.

It is intended for educational use and early-stage security testing to understand publicly exposed services on a domain.

---

## What it does

InfraScan focuses on three areas:

- DNS resolution and basic domain exposure check
- SSH port detection and simple banner inspection (if accessible)
- Web server header and basic technology fingerprinting

---

## Project Structure

```

core/
dns.py
ssh.py
fingerprint.py
engine.py

utils/
banner.py
resolver.py

main.py
requirements.txt
targets.txt

````

---

## Installation

```bash
git clone https://github.com/muhammadtalha1322/InfraScan.git
cd InfraScan
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

---

## Usage

### Single target

```bash
python main.py -t example.com
```

### Multiple targets

Create a file `targets.txt`:

```
example.com
google.com
```

Run:

```bash
python main.py -f targets.txt
```

---

## Output

The tool prints:

* DNS resolution result
* SSH availability (if port 22 is reachable)
* Basic web server information
* Simple technology hints based on response headers/content

---

## Limitations

* Does not perform deep vulnerability scanning
* Subdomain takeover detection is heuristic only
* Technology detection is basic and not fully reliable
* SSH analysis is limited to banner visibility

---

## Purpose

This tool is meant for:

* Learning infrastructure reconnaissance concepts
* Understanding how exposed services can be identified
* Early-stage security testing practice

---

## Disclaimer

Use only on systems you own or have explicit permission to test.
Unauthorized scanning is your responsibility.

---

## Author

Security Recon project by Muhammad Talha
