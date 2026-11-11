# RELEASE RUSH
## Phase 4 — Monitoring & Incident Response

**Challenge 5 | Total Marks: 20**

### PRODUCTION INCIDENT

The Inventory API production environment is experiencing an unusual increase in failed requests and response latency.

The monitoring system has generated multiple alerts.

Your team has been assigned as the on-call engineering team responsible for investigating the incident, identifying its root cause, restoring service reliability and validating the recovery.

### YOUR TASKS

1. Inspect the supplied monitoring dashboard.
2. Investigate the alert data.
3. Analyse the historical metrics.
4. Inspect the application logs.
5. Identify the production symptoms.
6. Correlate evidence from multiple sources.
7. Determine the root cause.
8. Investigate the relevant application implementation.
9. Implement the necessary corrective action.
10. Run the automated recovery tests.
11. Verify that the application recovers successfully.
12. Complete the incident submission report.

---

### PARTICIPANT SETUP

**Step 1 — Clone the official repository**

https://github.com/sammjoshuaa07-ui/ReleaseRush-Phase-4-Monitoring

```bash
git clone https://github.com/sammjoshuaa07-ui/ReleaseRush-Phase-4-Monitoring.git
cd ReleaseRush-Phase-4-Monitoring
```

**Step 2 — Create your team's repository**

The team leader must create a new, empty GitHub repository.

Suggested name:

`RR-TEAM-ID-Phase-4-Monitoring`

Do not initialize it with a README, Gitignore or license.

**Step 3 — Configure your remotes**

```bash
git remote rename origin source
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Verify:

```bash
git remote -v
```

- `origin` must point to your team's repository.
- `source` must point to the official event repository.

**Step 4 — Push the starter code**

```bash
git push -u origin main
```

All investigation and corrections must be performed in your team's repository.

---

### FILES PROVIDED

- Monitoring dashboard.
- Historical metrics.
- System alert data.
- Application logs.
- Application source code.
- Automated tests.
- Recovery verification script.
- GitHub Actions workflow.
- Submission template.

---

### INVESTIGATION

Open the monitoring dashboard:

`incident/dashboard.html`

Inspect the supplied evidence:

- `incident/alerts.json`
- `incident/metrics.csv`
- `incident/application.log`

Correlate the incident timeline with the application behavior.

Your root-cause explanation must be supported by evidence from at least two incident artifacts.

Investigate the relevant application code and determine what corrective action is required.

---

### RUN AUTOMATED TESTS

Python 3.10 or newer is recommended.

No third-party Python packages are required.

From the repository root:

Windows:

```powershell
py -m unittest discover -s tests -v
```

Other systems:

```bash
python -m unittest discover -s tests -v
```

---

### VERIFY RECOVERY

Run the recovery verification script separately.

Windows:

```powershell
py verify_recovery.py
```

Other systems:

```bash
python verify_recovery.py
```

Use the verification result to demonstrate that the application can recover from the incident and continue processing requests correctly.

---

### COMMIT AND PUSH YOUR SOLUTION

Check your changes:

```bash
git status
```

Stage your solution:

```bash
git add .
```

Commit:

```bash
git commit -m "fix: resolve production monitoring incident"
```

Push to your team's repository:

```bash
git push origin main
```

Do not push to the official event repository or the `source` remote.

---

### GITHUB ACTIONS VALIDATION

Open your team's GitHub repository and select the Actions tab.

Inspect the latest Phase 4 workflow run.

Verify that:

- Automated recovery tests pass.
- The recovery verification script succeeds.
- The workflow corresponds to your final submitted commit.
- The workflow completes successfully.

Workflow configuration:

`.github/workflows/monitoring.yml`

---

### SUBMISSION REQUIREMENTS

Submit:

1. Team ID and member names.
2. Your team's repository URL.
3. Incident summary.
4. Identified production symptoms.
5. Root-cause explanation.
6. Evidence from at least two incident artifacts.
7. Description of the corrective action.
8. Successful automated test output.
9. Recovery verification output.
10. Final commit hash.
11. Successful GitHub Actions run link.
12. Completed `SUBMISSION_TEMPLATE.md`.
13. Final recovery flag.

### RULES

- Teams of 2–3 members.
- Internet search is permitted.
- Discussion only within your own team.
- Do not delete or weaken supplied tests.
- Do not suppress errors merely to make tests pass.
- Preserve existing application functionality.
- Do not push to the official event repository or the `source` remote.
- All solutions must be committed and pushed to your own repository.

**Good luck!**
