from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
import requests

app = FastAPI()

CLIENT_ID = "8950442066920082"
CLIENT_SECRET = "Pqce6DEJ6EWxGw1C2WFufCek3MflBueG"
REDIRECT_URI = "https://ml-backend-kndd.onrender.com/callback"

@app.get("/")
def home():
    return {"status": "ok"}

@app.get("/login")
def login():
    url = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    return RedirectResponse(url)

@app.get("/callback")
def callback(code: str):
    url = "https://api.mercadolibre.com/oauth/token"

    payload = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)
    return response.json()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    return {"ok": True}
