from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel

app = FastAPI()

class ScheduleRequest(BaseModel):
    task: str

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
    <head>
        <title>Coding Agent API</title>
        <style>
            body { font-family: 'Segoe UI', Arial, sans-serif; background: #f4f6fb; color: #222; margin: 0; padding: 0; }
            .container { max-width: 600px; margin: 60px auto; background: #fff; border-radius: 16px; box-shadow: 0 4px 24px rgba(0,0,0,0.08); padding: 40px 32px; }
            h1 { color: #3b82f6; font-size: 2.5rem; margin-bottom: 0.5em; }
            p { font-size: 1.2rem; margin-bottom: 1.5em; }
            a.button { display: inline-block; background: #3b82f6; color: #fff; padding: 12px 28px; border-radius: 8px; text-decoration: none; font-weight: 600; font-size: 1.1rem; transition: background 0.2s; }
            a.button:hover { background: #2563eb; }
            .endpoints { margin-top: 2em; }
            .endpoint { background: #f1f5f9; border-radius: 8px; padding: 12px 18px; margin-bottom: 10px; }
            .endpoint span { font-family: monospace; color: #2563eb; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Coding Agent API</h1>
            <p>Welcome! This is a cloud-based coding agent API.<br>Use the endpoints below to schedule jobs and check their status.</p>
            <a class="button" href="/docs">View Interactive API Docs</a>
            <div class="endpoints">
                <div class="endpoint"><b>POST</b> <span>/schedule</span> <br> <small>Body: {'{"task": "your task here"}'}</small></div>
                <div class="endpoint"><b>GET</b> <span>/status/&#123;job_id&#125;</span></div>
            </div>
        </div>
    </body>
    </html>
    """

@app.get("/docs", include_in_schema=False)
def custom_docs():
    return RedirectResponse(url="/redoc")

@app.post("/schedule")
def schedule_job(req: ScheduleRequest):
    # Return a dummy job id
    return {"job_id": "dummy-job-id"}

@app.get("/status/{job_id}")
def get_status(job_id: str):
    # Return a dummy status and output link
    return {"status": "complete", "output_link": "https://example.com/dummy.zip"} 