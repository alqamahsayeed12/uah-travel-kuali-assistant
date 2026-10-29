# UAH Travel Planner, Authorization & Reimbursement Assistant

Private colleague edition of the reusable UAH/ESSC travel skill, based on personal version 1.1.0. Includes the complete workflow specification (personal contact names redacted), eight mandatory airfare evidence rules, templates, deterministic calculators and 57 tests. Not an official UAH product or institutional approval service.

## Source layout

The complete source tree is stored in `source-v1.1.0.zip` (including plugin, templates, scripts, tests, and local marketplace configuration). This archive distribution preserves directory paths through the browser upload. `bootstrap.py` checks SHA-256 and extracts it locally without network access. The repository does not yet store each source file as an individually browsable Git file.

## Reproduce and test

Requires Python 3.10 or newer. Core tests and packaging use only the Python standard library; no API keys, paid services or dependencies are required.

```sh
python3 bootstrap.py
python3 scripts/build.py
```

This runs all tests, validates the skill, then writes deterministic ZIPs and SHA-256 hashes into `dist/`. Run from a fresh clone to reproduce the same archives with the same source. Live inventory, policy verification and Kuali browser interactions need a capable authenticated agent host; tests do not simulate institutional approval.

## Use in Codex

Clone this private repository using your own GitHub access. From the repository root:

```sh
codex plugin marketplace add .
codex plugin add uah-travel-kuali-assistant@uah-travel-colleagues
```

Alternatively copy `plugin/skills/uah-travel-kuali-assistant` into your host’s skills directory using its supported installation flow. Installation is per user and needs their approval. CLI support was inspected October 29, 2026; verify local help if your host differs. This repository does not automatically install into ChatGPT cloud or grant Kuali access.

Invoke the skill by name and provide origin, venue, dates, event and funding context. First it presents travel choices; detailed evidence follows selection. Purchase, certification and submission require separate explicit authorization.

## Configure for yourself

Edit `plugin/skills/uah-travel-kuali-assistant/assets/settings.json` or provide overrides in chat. `$HOME/UAH_Travel` means your own home directory, not a literal folder named `$HOME`; resolve it before file access. Routing preferences (Delta, one connection, 45-minute minimum, daytime travel, no overnight flights) are editable examples, not UAH policy. Set your own department and preferences. Confirm funding and approvers per trip; no colleague should inherit another traveler’s accounts or contacts.

Keep actual travel documents outside this checkout. No real trip PDFs, receipts, home address, account codes, credentials or private submission URLs are included. The submitted Kuali PDF was used only to describe dated field structure. Do not commit future trip records. Use separate private trip folders and recheck current university, sponsor, carrier and date-specific per-diem rules.

## Evidence and limitations

The eight-rule airfare protocol is traveler-supplied guidance attributed to Business Services; public verification of its complete protocol is not claimed. Native website/date evidence and exact selected outbound and return comparisons are required. Missing lower fares are not automatically sold out. The scripts validate supplied arithmetic and declared evidence, not screenshots, availability, policy compliance or remote upload contents.

The combined packet, cost fields, notes and uploaded versions must agree. Save and reopen to verify. Submitted/In Progress is not approved or paid. For reimbursement, distinguish PCard/direct payment from traveler expenses.

## Sharing

Keep the GitHub repository private. Grant individual colleagues access deliberately through repository settings; do not post private documents in issues. No open-source license is granted by this repository; obtain permission before redistributing beyond the authorized group.
