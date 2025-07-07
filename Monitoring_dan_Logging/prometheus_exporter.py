from prometheus_client import start_http_server, Summary, Counter
import time
import random

REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('inference_request_count', 'Total number of inference requests')
ERROR_COUNT = Counter('inference_error_count', 'Total number of inference errors')

@REQUEST_TIME.time()
def simulate_inference(success=True):
    REQUEST_COUNT.inc()

    time.sleep(random.uniform(0.1, 0.5))
    
    if not success:
        ERROR_COUNT.inc()

if __name__ == '__main__':
    start_http_server(9000)
    print("Prometheus metrics server running on :9000")

    while True:
        if random.random() < 0.7:
            simulate_inference(success=True)
        else:
            simulate_inference(success=False)
        
        time.sleep(2)
