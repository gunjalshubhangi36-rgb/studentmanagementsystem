from fastapi import FastAPI
from Routes.StudentRoutes import router
from fastapi.middleware.cors import CORSMiddleware

app  = FastAPI()

app.include_router(router)

app.add_middleware(
CORSMiddleware,
allow_credentials=True,
allow_headers=["*"],
allow_methods=["*"],
allow_origin=["*"]
)

@app.get("/")
def greet():
    return {"message":"hello"}