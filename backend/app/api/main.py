from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.stats import router as stats_router
from app.api.routes.flows import router as flows_router
from app.api.routes.blocked import router as blocked_router

app = FastAPI(title="DPI Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(stats_router)
app.include_router(flows_router)
app.include_router(blocked_router)