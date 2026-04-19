from fastapi import FastAPI

app = FastAPI(title="DevOps Project API")


@app.get("/")
def health_check():
    return {"status": "ok", "message": "DevOps pipeline started 🚀"}
