# Attack Tree Risk Analysis Tool
**ISM Assignment | MSc Computer Science | University of Essex**

**By Lauren Pechey**

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

| Test | Result |
|------|--------|
| test_leaf_basic | PASSED |
| test_leaf_zero_prob | PASSED |
| test_leaf_zero_impact | PASSED |
| test_or_takes_max | PASSED |
| test_and_sums_children | PASSED |
| test_unknown_type | PASSED |

---

## How to Run the Linter

```bash
pip install flake8
flake8 main.py attack_tree.py aggregator.py visualiser.py
```

A clean run (no output) means the code passes the linter.

---

## File Structure

| File | Purpose |
|------|---------|
| `main.py` | Entry point — runs the full analysis |
| `attack_tree.py` | Loads the attack tree from a JSON file |
| `aggregator.py` | Calculates risk scores recursively |
| `visualiser.py` | Draws the tree as a hierarchical graph |
| `pre_tree.json` | Attack tree: pre-digitalisation threats |
| `post_tree.json` | Attack tree: post-digitalisation threats |
| `test_aggregator.py` | Unit tests for the aggregator |
| `requirements.txt` | Python dependencies |

---

## Risk Calculation

| Node Type | Calculation | Rationale |
|-----------|-------------|-----------|
| LEAF | probability × impact | Expected monetary value of that threat |
| AND | sum of children | All steps must succeed — costs accumulate |
| OR | max of children | Only one path needs to work — worst case |

---

## Threat Model

Threats are drawn from the Pampered Pets baseline risk assessment (Unit 3) and
mapped to the attack tree as follows:

**Pre-digitalisation** — models the current as-is environment with shared
wireless access, legacy systems, unmanaged endpoints, and a single
point-of-failure POS system.

**Post-digitalisation** — models the to-be environment after applying
mitigations including network segmentation, MFA, endpoint protection,
automated backups, and cybersecurity awareness training, aligned with
ISO/IEC 27001 and the NIST RMF.

---

## Submission Screenshots

| # | Screenshot | What to Capture |
|---|-----------|-----------------|
| 1 | Figure 1 | Terminal output showing all values entered and final risk summary |
| 2 | Figure 2 | Pre-digitalisation attack tree diagram |
| 3 | Figure 3 | Post-digitalisation attack tree diagram |
| 4 | Figure 4 | Risk comparison bar chart |
| 5 | Figure 5 | pytest terminal output showing all 6 tests passing |
| 6 | Figure 6 | flake8 terminal output showing a clean run |

<details>
<summary>Figure 1 — Terminal Output</summary>

![Figure 1: Attack Tree Risk Analysis Tool — Terminal Output](screenshots/figure1_terminal_output.png)

</details>

<details>
<summary>Figure 2 — Pre-Digitalisation Attack Tree</summary>

![Figure 2: Attack Tree Visualisation — Pre-Digitalisation Threat Model](screenshots/figure2_pre_tree.png)

</details>

<details>
<summary>Figure 3 — Post-Digitalisation Attack Tree</summary>

![Figure 3: Attack Tree Visualisation — Post-Digitalisation Threat Model](screenshots/figure3_post_tree.png)

</details>

<details>
<summary>Figure 4 — Risk Comparison Bar Chart</summary>

![Figure 4: Risk Comparison Bar Chart — Pre vs Post Digitalisation Expected Monetary Risk](screenshots/figure4_bar_chart.png)

</details>

<details>
<summary>Figure 5 — Unit Test Results</summary>

![Figure 5: Unit Test Results — pytest Output](screenshots/figure5_pytest.png)

</details>

<details>
<summary>Figure 6 — Linter Report</summary>

![Figure 6: Linter Evaluation Report — flake8 Output](screenshots/figure6_flake8.png)

</details>

---

## Dependencies

- `networkx` (3.6.1) — graph construction and layout: https://networkx.org
- `matplotlib` (3.11.0) — visualisation: https://matplotlib.org
- `pytest` (8.3.5) — unit testing: https://pytest.org

---

## References

Aoudi, S. and Al-Aqrabi, H. (2026) 'Integrating IoT security practices into a
risk-based framework for small and medium enterprises', *Computer Standards &
Interfaces*, 97, p. 104099.

ISO. (2022) *ISO/IEC 27001:2022 Information security, cybersecurity and privacy
protection*. Available at: https://www.iso.org/standard/27001

Lallie, H.S., Debattista, K. and Bal, J. (2020) 'A review of attack graph and
attack tree visual syntax in cyber security', *Computer Science Review*, 35,
p. 100219.

Lincke, S. (2024) *Information security planning: A practical approach*. Cham:
Springer International Publishing.

Marsland, T. (2024) *Unveiling the NIST Risk Management Framework (RMF)*.
Birmingham: Packt Publishing Ltd.

Mauw, S. and Oostdijk, M. (2005) 'Foundations of Attack Trees', *Information
Security and Cryptology*, LNCS 3935, pp. 186–198.

NIST. (2023) *National Vulnerability Database*. Available at: https://nvd.nist.gov/

Python Software Foundation. (2024) *json — JSON encoder and decoder*.
Available at: https://docs.python.org/3/library/json.html

Schneier, B. (1999) 'Attack Trees', *Dr Dobb's Journal*, 24(12), pp. 21–29.

Stack Overflow. (2014) *Hierarchical layout for NetworkX graphs*.
Available at: https://stackoverflow.com/a/29597209
(Used as the basis for the tree layout algorithm in visualiser.py)