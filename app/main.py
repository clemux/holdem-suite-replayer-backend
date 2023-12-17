from typing import Annotated

from fastapi import FastAPI, File
from holdem_suite_parser import parse_hands

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload")
async def upload(file: Annotated[bytes, File()]):
    print("coucou")
    hand_info = parse_hands(file.decode(encoding="utf-8"))
    print(hand_info.blinds.ante)
    return {"parsed_hand": "coucou"}