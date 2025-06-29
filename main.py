from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict
import docker
import threading
import shutil
import os
import time
from job_manager import JobManager

app = FastAPI()
job_manager = JobManager()
docker_client = docker.from_env()

class ScheduleRequest(BaseModel):
    task: str

@app.post("/schedule")
def schedule_job(req: ScheduleRequest):
    job_id = job_manager.create_job(req.task)
    threading.Thread(target=run_agent_container, args=(job_id, req.task), daemon=True).start()
    return {"job_id": job_id}

@app.get("/status/{job_id}")
def get_status(job_id: str):
    status = job_manager.get_status(job_id)
    output_link = job_manager.get_output_link(job_id)
    return {"status": status['status'], "output_link": output_link}

def run_agent_container(job_id: str, task: str):
    job_manager.set_status(job_id, 'running')
    job_path = job_manager.get_status(job_id)['path']
    try:
        # Mount job_path to /workspace in the container
        container = docker_client.containers.run(
            "coding-agent",
            detach=True,
            volumes={job_path: {'bind': '/workspace', 'mode': 'rw'}},
            environment={"TASK": task},
            ports={"6080/tcp": None, "5901/tcp": None},
            remove=True
        )
        # Wait for the agent to finish (simulate with sleep for now)
        time.sleep(10)  # Replace with actual monitoring
        # Simulate output
        with open(os.path.join(job_path, 'output.txt'), 'w') as f:
            f.write(f"Task '{task}' completed.")
        # Optionally zip output
        shutil.make_archive(os.path.join(job_path, 'output'), 'zip', job_path)
        job_manager.set_status(job_id, 'complete')
    except Exception as e:
        job_manager.set_status(job_id, f'error: {e}') 