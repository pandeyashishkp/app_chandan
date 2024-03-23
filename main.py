from fastapi import FastAPI
from fastapi.responses import JSONResponse
from query import QueryBigquery

qbq = QueryBigquery()
app = FastAPI()

@app.get("/admin/merge_run")
def merge():
    return JSONResponse(qbq.run_merge_scripts())

@app.get("/{report_name}")
async def root(report_name: str):
    return JSONResponse(qbq.query_selector(report_name))
