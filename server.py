from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def index():
    return FileResponse("index.html", media_type="text/html")

@app.get("/api/some-pdf-file")
def read_root():
    return FileResponse("example_pdf.pdf", media_type="application/json")