# Orchestrator

This service provides:
- `/schedule` endpoint: Accepts a plain-text task, spins up an agent container, returns a job ID.
- `/status/:id` endpoint: Returns job status and download link if complete.
- File-based job management in `../jobs/`.

## Usage

Install dependencies:
```
pip install -r requirements.txt
```

Run the server:
```
uvicorn main:app --reload
```

## API

- `POST /schedule` with JSON `{ "task": "Build me a todo app in React" }`
- `GET /status/{id}` returns `{ "status": "pending|running|complete|error", "output_link": "/jobs/{id}/output.zip" }`

## Notes
- Each job runs in an isolated Docker container (can be extended to Firecracker VMs).
- Output is zipped and available for download when complete.
- Horizontally scalable: stateless API, jobs tracked on disk. 