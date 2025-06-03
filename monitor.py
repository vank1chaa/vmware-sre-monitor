from prometheus_client import start_http_server, Gauge
import requests
import time

while True:
    time.sleep(10)

# URLs to monitor
URLS = ["https://httpstat.us/503", "https://httpstat.us/200"]

# Prometheus metric: is the URL up? (1 = yes, 0 = no)
up_metric = Gauge('sample_external_url_up', 'Availability of URL', ['url'])

# Prometheus metric: response time in milliseconds
response_time_metric = Gauge('sample_external_url_response_ms', 'Response time in ms', ['url'])

# Function to check each URL
def check_urls():
    for url in URLS:
        try:
            start = time.time()
            response = requests.get(url)
            latency = (time.time() - start) * 1000  # convert to ms
            response_time_metric.labels(url=url).set(latency)

            if response.status_code == 200:
                up_metric.labels(url=url).set(1)
            else:
                up_metric.labels(url=url).set(0)
        except Exception:
            # Any exception means the URL is down/unreachable
            up_metric.labels(url=url).set(0)
            response_time_metric.labels(url=url).set(0)

# Main function
if __name__ == "__main__":
    # Start HTTP server on port 8000 for Prometheus to scrape
    start_http_server(8000, addr="0.0.0.0")
    while True:
        check_urls()
        time.sleep(5)  # Check every 5 seconds
