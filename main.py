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
            form { margin-top: 2em; }
            label { font-weight: 600; }
            input[type="text"], textarea { width: 100%; padding: 10px; margin: 8px 0 16px 0; border-radius: 6px; border: 1px solid #d1d5db; font-size: 1rem; }
            button { background: #3b82f6; color: #fff; border: none; padding: 10px 22px; border-radius: 6px; font-size: 1rem; font-weight: 600; cursor: pointer; transition: background 0.2s; }
            button:hover { background: #2563eb; }
            .result, .status-result { background: #f1f5f9; border-radius: 8px; padding: 12px 18px; margin-top: 12px; font-family: monospace; }
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
            <form id="schedule-form">
                <label for="task">Schedule a Job</label>
                <textarea id="task" name="task" rows="2" placeholder="Enter your task here" required></textarea>
                <button type="submit">Submit Task</button>
                <div id="schedule-result" class="result" style="display:none;"></div>
            </form>
            <form id="status-form">
                <label for="job_id">Check Job Status</label>
                <input type="text" id="job_id" name="job_id" placeholder="Enter job id" required />
                <button type="submit">Check Status</button>
                <div id="status-result" class="status-result" style="display:none;"></div>
            </form>
        </div>
        <script>
            // Schedule form
            document.getElementById('schedule-form').onsubmit = async function(e) {
                e.preventDefault();
                const task = document.getElementById('task').value;
                const resultDiv = document.getElementById('schedule-result');
                resultDiv.style.display = 'none';
                resultDiv.innerText = '';
                try {
                    const res = await fetch('/schedule', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ task })
                    });
                    const data = await res.json();
                    resultDiv.innerText = 'Job ID: ' + data.job_id;
                    resultDiv.style.display = 'block';
                } catch (err) {
                    resultDiv.innerText = 'Error: ' + err;
                    resultDiv.style.display = 'block';
                }
            };
            // Status form
            document.getElementById('status-form').onsubmit = async function(e) {
                e.preventDefault();
                const job_id = document.getElementById('job_id').value;
                const resultDiv = document.getElementById('status-result');
                resultDiv.style.display = 'none';
                resultDiv.innerText = '';
                try {
                    const res = await fetch('/status/' + encodeURIComponent(job_id));
                    const data = await res.json();
                    resultDiv.innerText = 'Status: ' + data.status + (data.output_link ? '\nOutput: ' + data.output_link : '');
                    resultDiv.style.display = 'block';
                } catch (err) {
                    resultDiv.innerText = 'Error: ' + err;
                    resultDiv.style.display = 'block';
                }
            };
        </script>
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