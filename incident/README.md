# Incident Evidence Pack

Incident ID: RR-INC-05

Service: inventory-api

Incident window: 2026-11-11 14:30-14:45 UTC

Inspect all four evidence sources:

- dashboard.html - visual summary of error rate, latency, pool usage, and CPU.
- metrics.csv - raw five-minute monitoring samples.
- alerts.json - alert rules and observed values.
- application.log - request-level events around the incident.

Do not assume the first alert is automatically the root cause.

Correlate the timing and behavior across the evidence before changing code.