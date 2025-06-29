# Agent Container

This container provides:
- Xvfb (virtual display)
- fluxbox (window manager)
- xdotool (GUI automation)
- Jupyter notebook (code execution)
- VNC server and noVNC (web-based GUI)
- Context management (context_manager.py)

## Usage

Build the image:
```
docker build -t coding-agent .
```

Run the container:
```
docker run -p 6080:6080 -p 5901:5901 -v $(pwd)/workspace:/workspace coding-agent
```

Access the GUI at [http://localhost:6080](http://localhost:6080)

## Context Management

The agent persists context to `/workspace/context.json` and prunes old entries if the context exceeds 1M tokens (approx chars). 