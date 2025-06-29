#!/bin/bash
set -e

# Start Xvfb
Xvfb :1 -screen 0 1024x768x16 &
export DISPLAY=:1

# Start fluxbox window manager
fluxbox &

# Start VNC server
vncserver :1 -geometry 1024x768 -depth 16 -SecurityTypes None &

# Start noVNC
/opt/novnc/utils/novnc_proxy --vnc localhost:5901 --listen 6080 &

# Start Jupyter notebook
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password='' &

# Run agent if TASK is set
if [ ! -z "$TASK" ]; then
  python3 /app/agent.py
fi

wait 