# RTI EDA API

FastAPI starter project for RTI data exploration, reporting, and statistical analysis.

The application is organized into:

- `app/api/routes/` - overview, applications, ministries, rejections, appeals, accountability, compliance, and analysis endpoints
- `app/analysis/` - descriptive, correlation, trend, and statistical analysis helpers
- `app/models/`, `app/schemas/`, `app/services/`, and `app/repositories/` - application layers
- `data/raw/` and `data/processed/` - source and processed datasets
- `notebooks/` - exploratory analysis notebooks
- `alembic/` - database migration workspace

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open the API documentation at `http://127.0.0.1:8000/docs`.

Run tests with:

```powershell
pytest
```
