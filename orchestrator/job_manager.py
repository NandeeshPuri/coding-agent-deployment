import os
import uuid
import json
from typing import Dict

JOBS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../jobs'))

class JobManager:
    def __init__(self):
        os.makedirs(JOBS_DIR, exist_ok=True)
        self.jobs: Dict[str, dict] = {}

    def create_job(self, task: str) -> str:
        job_id = str(uuid.uuid4())
        job_path = os.path.join(JOBS_DIR, job_id)
        os.makedirs(job_path, exist_ok=True)
        self.jobs[job_id] = {'status': 'pending', 'task': task, 'path': job_path}
        with open(os.path.join(job_path, 'task.txt'), 'w') as f:
            f.write(task)
        return job_id

    def set_status(self, job_id: str, status: str):
        if job_id in self.jobs:
            self.jobs[job_id]['status'] = status
            with open(os.path.join(self.jobs[job_id]['path'], 'status.json'), 'w') as f:
                json.dump({'status': status}, f)

    def get_status(self, job_id: str) -> dict:
        if job_id in self.jobs:
            return self.jobs[job_id]
        # Try to load from disk
        job_path = os.path.join(JOBS_DIR, job_id)
        if os.path.exists(job_path):
            try:
                with open(os.path.join(job_path, 'status.json')) as f:
                    status = json.load(f)
                return {'status': status['status'], 'path': job_path}
            except Exception:
                return {'status': 'unknown', 'path': job_path}
        return {'status': 'not_found'}

    def get_output_link(self, job_id: str) -> str:
        job = self.get_status(job_id)
        if job['status'] == 'complete':
            # In real deployment, serve via HTTP static
            return f"/jobs/{job_id}/output.zip"
        return "" 