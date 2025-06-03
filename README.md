# vmware-sre-monitor
SRE test project for Cloud Service Platform at VMware

- Features:
  
Monitors specified URLs for availability and response time.

Exposes metrics at /metrics for Prometheus scraping.

Containerized using Docker.

Deployable to Kubernetes using Helm.


- Prerequisites:
  
Docker installed and running.

Kubernetes cluster set up.

Helm installed.

Access to GitHub Container Registry (GHCR) for pushing images.

- Local Testing:
  
Clone the repository:

git clone https://github.com/vank1chaa/vmware-sre-monitor.git

cd vmware-sre-monitor

Build the Docker image:

docker build -t ghcr.io/vank1chaa/vmware-sre-monitor:latest .

Run the container locally:

docker run -p 8000:8000 ghcr.io/vank1chaa/vmware-sre-monitor:latest

- Access metrics:
  
Open your browser and navigate to http://localhost:8000/metrics.
