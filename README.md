# Runnable Assessment: Coding Agent with Orchestration

## Overview
This project provides a scalable, secure coding agent with sandboxing, context management, and an orchestration layer. It includes:
- **Agent Container**: Runs code, GUI automation, and exposes a VNC/noVNC interface.
- **Orchestration Server**: Schedules jobs, manages agent containers, and provides status/download endpoints.
- **Context Management**: File-based, pruned context for large tasks.

## Directory Structure
```
runnable_assesment/
├── agent/           # Agent Docker image and code
├── orchestrator/    # Orchestration server (FastAPI)
├── jobs/            # Output folders for each job
└── README.md
```

## Quickstart

### 1. Build and Run the Agent Container
```
cd agent
# Build the Docker image
sudo docker build -t coding-agent .
# Run the agent (for testing)
sudo docker run -p 6080:6080 -p 5901:5901 coding-agent
```

### 2. Start the Orchestration Server
```
cd orchestrator
pip install -r requirements.txt
python main.py
```

### 3. Schedule a Job
```
POST /schedule  # with a plain-text task
GET /status/:id # to check status and get download link
```

### 4. View the Agent
Open [http://localhost:6080](http://localhost:6080) for the noVNC interface.

---

## Security & Scalability
- Each job runs in an isolated container (can be extended to Firecracker VMs).
- Context is managed on disk and pruned for large tasks.
- Orchestration layer is stateless and horizontally scalable.

# (Paste the contents of orchestrator/README.md here) 