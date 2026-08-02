from fastapi import FastAPI

app = FastAPI(
    title="CloudScale AI",
    version="1.0.0",
    description="Adaptive Predictive Auto-Scaling with Real-Time Feedback and Game-Theoretic Cost Optimization"
)

@app.get("/")
def home():
    return {
        "project": "CloudScale AI",
        "status": "Running",
        "version": "1.0.0"
    }

@app.get("/status")
def status():
    return {
        "servers": 5,
        "users": 100,
        "cpu": 45,
        "memory": 38,
        "latency": 20,
        "cost": 18.5
    }
