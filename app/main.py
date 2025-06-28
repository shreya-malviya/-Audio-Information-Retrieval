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


@app.get("/search")
async def searchAudio():
    result = 1;
    return {"matches" : result}