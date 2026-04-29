from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/login")
def login():
    return {"msg": "login funcionando"}

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    return {"ok": True}
