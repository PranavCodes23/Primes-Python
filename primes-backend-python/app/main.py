from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import dashboard

app = FastAPI(title="PRIMES Dashboard API", version="1.0.0")

# Configure CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For dev, allow all. In prod, restrict to specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to PRIMES API"}
