# CI/CD Demo App

A tiny Flask web app for testing a CI/CD pipeline end to end.

## Endpoints
- `GET /` — hello message + version
- `GET /health` — health check (used for pipeline/deploy verification)
- `GET /add/<a>/<b>` — adds two integers (supports negatives)

## Run locally
```bash
pip install -r requirements.txt
python app.py
```
App runs at http://localhost:5000

## Run tests
```bash
pytest -v
```

## CI/CD Pipeline
`.github/workflows/ci-cd.yml` runs on every push/PR to `main`:
1. Installs dependencies on Python 3.10, 3.11, 3.12
2. Runs the pytest suite
3. A follow-up job simulates a build/deploy step once tests pass

To use it: push this folder to a GitHub repo — the workflow runs automatically
(check the "Actions" tab). Swap the `build-and-report` job's `run` command
for real deploy steps (Docker build/push, deploy to a server, etc.) when ready.

## Production serving (optional)
```bash
gunicorn -b 0.0.0.0:5000 app:app
```
