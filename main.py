from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    expose_headers=[],
)

app.mount("/", StaticFiles(directory="game"), name="game")

@app.middleware("http")
async def add_process_time_header (request: Request, call_next) :
  response = await call_next(request)
  response.headers["Access-Control-Allow-Origin"] = "*"
  response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
  response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
  return response