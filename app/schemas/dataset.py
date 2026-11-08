from pydantic import BaseModel


class DatasetResponse(BaseModel):
    report_id: int
    tables: int
    rows: int
