from fastapi import FastAPI
from Routes.StudentRoutes import router
from fastapi.middleware.cors import CORSMiddleware

app  = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origin=["*"],
    access_control_allow_origin=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

app.include_router(router)


@app.get("/")
def greet():
    return {"message":"hello"}