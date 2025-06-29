from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ScheduleRequest(BaseModel):
    task: str

@app.post("/schedule")
def schedule_job(req: ScheduleRequest):
    # Return a dummy job id
    return {"job_id": "dummy-job-id"}

@app.get("/status/{job_id}")
def get_status(job_id: str):
    # Return a dummy status and output link
    return {"status": "complete", "output_link": "https://example.com/dummy.zip"} 