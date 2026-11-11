# Release Rush - Phase 4: Monitoring and Incident Response

**Challenge 5 | 20 marks**

## Production incident

The Inventory API is experiencing HTTP 503 errors and unusually high p95 latency.

Monitoring reports also indicate database connection-pool saturation.

Your team is the on-call engineering team. Investigate the supplied evidence, identify the root cause, repair the service, and demonstrate recovery.

## Your tasks

1. Open `incident/dashboard.html` in a browser.
2. Read `incident/alerts.json`.
3. Investigate `incident/metrics.csv`.
4. Inspect `incident/application.log`.
5. Identify the production symptom and likely root cause.
6. Support your explanation with evidence from at least two incident artifacts.
7. Inspect `app/inventory.py`.
8. Repair the connection lifecycle so that a connection is always returned to the pool, including when a query raises an exception.
9. Run the tests and recovery verifier.
10. Complete `SUBMISSION_TEMPLATE.md`.

## Run locally

Python 3.10 or newer is recommended.

No third-party packages and no Docker installation are required.

From the repository root:

```powershell
py -m unittest discover -s tests -v
py verify_recovery.py
```

If the `py` command is unavailable, use:

```bash
python -m unittest discover -s tests -v
python verify_recovery.py
```

The starter repository is intentionally faulty. Some tests are expected to fail before the incident is repaired.

## CI validation

The GitHub Actions workflow is:

`.github/workflows/monitoring.yml`

Push your repaired solution to your team's repository. Successful validation requires all recovery tests and the recovery verifier to pass.

## Submission

Complete `SUBMISSION_TEMPLATE.md`.

Include the exact final flag printed by the recovery verifier.

Do not delete or weaken tests. Your fix must correctly handle both success and exception paths.