from http.client import HTTPException

from fastapi import FastAPI, HTTPException
from starlette.responses import Response

import uvicorn
app = FastAPI()
@app.get("/")

def root():
    return {"message": "Fast API in python"}


@app.post("/add")
def add(a,b):
    a= float(a)
    b= float(b)
    return a+b

@app.post("/sub")
def sub(a,b):
    a = float(a)
    b = float(b)
    c=a-b
    return c

if __name__== "__main__":
    #print("this is the initialization of my AI journey")
    #print(sub(a=6, b=3))
    #print(add(a=4, b=8))
    uvicorn.run(app,port=5001)