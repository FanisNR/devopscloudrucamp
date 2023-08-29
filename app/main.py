import os
import socket

from fastapi import FastAPI

app = FastAPI()


@app.get("/hostname")
async def get_hostname():
    val = socket.gethostname()
    return {"hostname": val}


@app.get("/author")
async def get_author():
    val = os.environ.get('AUTHOR')
    return {"author": val}


@app.get("/id")
async def get_uuid():
    val = os.environ.get('UUID')
    return {"id": val}

