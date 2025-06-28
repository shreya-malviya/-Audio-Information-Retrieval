from fastapi import FastAPI,UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

print("this is running...")

@app.get("/")
async def fetch():
    try:
        return JSONResponse(
            status_code=200,
            content={"success": "yoo thats  working"}
        )
    except Exception:
        return JSONResponse(
            status_code=500,
            content={"success": False}
        )


@app.post("/analyze")
async def analyze_audio(file: UploadFile = File(...)):
    try:
        # Access file metadata
        filename = file.filename
        content_type = file.content_type

        if content_type not in ['audio/mpeg', 'audio/wav']:
            return JSONResponse(status_code=400, content={"error": "Invalid file type"})

        # Read file bytes (if needed)
        # contents = await file.read()

        # Placeholder for real analysis
        result = {"filename": filename, "type": content_type, "matches": 1}

        return JSONResponse(content=result)

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})