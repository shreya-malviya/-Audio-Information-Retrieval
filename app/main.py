from fastapi import FastAPI,UploadFile,File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import shutil
import uuid
import os
from .retrieval import retrieve_similar

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # This ensures the folder is created if missing


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
        if file.content_type not in ["audio/mpeg", "audio/wav"]:
            return JSONResponse(status_code=400, content={"error": "Invalid file type"})

        # Save file to disk temporarily
        file_ext = ".mp3" if file.content_type == "audio/mpeg" else ".wav"
        unique_filename = f"{uuid.uuid4()}{file_ext}"
        temp_file_path = os.path.join(UPLOAD_DIR, unique_filename)

        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Use your pretrained model for retrieval
        matches = retrieve_similar(temp_file_path)

        # Optionally delete temp file
        os.remove(temp_file_path)

        return JSONResponse(content={"matches": matches})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# @app.post("/analyze")
# async def analyze_audio(file: UploadFile = File(...)):
#     try:
#         # Access file metadata
#         filename = file.filename
#         content_type = file.content_type

#         if content_type not in ['audio/mpeg', 'audio/wav']:
#             return JSONResponse(status_code=400, content={"error": "Invalid file type"})

#         # Read file bytes (if needed)
#         # contents = await file.read()

#         # Placeholder for real analysis
#         result = {"filename": filename, "type": content_type, "matches": 1}

#         return JSONResponse(content=result)

#     except Exception as e:
#         return JSONResponse(status_code=500, content={"error": str(e)})