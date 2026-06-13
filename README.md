# Attack Tree Risk Analysis Tool
**ISM Assignment | MSc Computer Science | University of Essex**

---

## What This Does

This Python application models cybersecurity attack trees for Pampered Pets and
calculates the expected financial impact of attacks on the business. It compares
the risk profile of the system before and after digitalisation controls are applied.

The user enters probability and impact values for each threat at runtime. The
application visualises the tree and aggregates the values into an overall risk
score (£), then produces a bar chart comparing both scenarios.

---

## How to Install

**Requirements:** Python 3.8+

**Option 1 — with a virtual environment (recommended):**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Option 2 — without a virtual environment:**
```bash
pip install -r requirements.txt
```

---

## How to Run

```bash
python3 main.py
```

You will be prompted to enter a probability (0.0–1.0) and impact (£) for each
leaf node. Use the values below to reproduce the Pampered Pets threat model.

### Pre-Digitalisation Values

| Node | Probability | Impact (£) |
|------|-------------|------------|
| Wireless Eavesdropping | 0.7 | 60000 |
| Malware Injection via Wi-Fi | 0.6 | 80000 |
| Phishing / Credential Compromise | 0.7 | 45000 |
| Data Loss via Legacy Warehouse System | 0.65 | 70000 |
| POS System Failure | 0.5 | 35000 |

### Post-Digitalisation Values

| Node | Probability | Impact (£) |
|------|-------------|------------|
| Wireless Eavesdropping | 0.2 | 60000 |
| Malware Injection via Wi-Fi | 0.15 | 80000 |
| Phishing / Credential Compromise | 0.25 | 45000 |
| Data Loss via Legacy Warehouse System | 0.1 | 70000 |
| POS System Failure | 0.2 | 35000 |

The reduced probabilities in the post-digitalisation scenario reflect the
controls recommended in the report: network segmentation, MFA, endpoint
protection, automated backups, and staff cybersecurity training.

---

## How to Run Tests

```bash
pytest test_aggregator.py -v
```

Expected output: