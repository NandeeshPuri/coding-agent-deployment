FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-dev \
    nodejs npm \
    xvfb xdotool fluxbox \
    tigervnc-standalone-server \
    supervisor wget curl git \
    net-tools x11vnc \
    && rm -rf /var/lib/apt/lists/*

# Install Jupyter
RUN pip3 install jupyter

# Install noVNC
RUN git clone https://github.com/novnc/noVNC.git /opt/novnc && \
    git clone https://github.com/novnc/websockify /opt/novnc/utils/websockify

# Copy startup script
COPY start.sh /start.sh
RUN chmod +x /start.sh

# Copy agent code and requirements
COPY agent.py context_manager.py package.json tsconfig.json requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN npm install

EXPOSE 6080 5901
CMD ["/start.sh"] 