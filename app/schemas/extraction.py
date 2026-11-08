from pydantic import BaseModel, Field


class ExtractionRequest(BaseModel):
    report_id: int
    extractor: str = Field(default="pdfplumber", min_length=1)


class ExtractionResponse(BaseModel):
    id: int
    report_id: int
    extractor: str
    status: str
