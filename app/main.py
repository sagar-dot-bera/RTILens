from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routes import (
    accountability,
    analysis,
    appeals,
    applications,
    compliance,
    datasets,
    extraction,
    ministries,
    overview,
    rejections,
    reports,
    tables,
)
from app.core.config import settings
from app.db.database import create_tables


@asynccontextmanager
async def lifespan(_: FastAPI):
    await create_tables()
    yield


app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])
app.include_router(extraction.router, prefix="/api/extraction", tags=["extraction"])
app.include_router(tables.router, prefix="/api/tables", tags=["tables"])
app.include_router(datasets.router, prefix="/api/datasets", tags=["datasets"])
app.include_router(overview.router, prefix="/api/overview", tags=["overview"])
app.include_router(applications.router, prefix="/api/applications", tags=["applications"])
app.include_router(ministries.router, prefix="/api/ministries", tags=["ministries"])
app.include_router(rejections.router, prefix="/api/rejections", tags=["rejections"])
app.include_router(appeals.router, prefix="/api/appeals", tags=["appeals"])
app.include_router(accountability.router, prefix="/api/accountability", tags=["accountability"])
app.include_router(compliance.router, prefix="/api/compliance", tags=["compliance"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["analysis"])


@app.get("/health", tags=["system"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
