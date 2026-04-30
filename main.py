from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import requests

app = FastAPI()

CLIENT_ID = "8950442066920082"
CLIENT_SECRET = "Pqce6DEJ6EWxGw1C2WFufCek3MflBueG"
REDIRECT_URI = "https://ml-backend-kndd.onrender.com/callback"

ACCESS_TOKEN = "APP_USR-8950442066920082-042921-721cc933987d8a8b7e1c5f64d7e568b6"
SELLER_ID = "2563305389"

@app.get("/")
def home():
    return {"status": "ok"}


@app.get("/login")
def login():
    url = (
        "https://auth.mercadolivre.com.br/authorization"
        f"?response_type=code"
        f"&client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
    )
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


@app.get("/items")
def items():
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(
        "https://api.mercadolibre.com/users/me/items/search",
        headers=headers
    )

    return response.json()


@app.get("/orders")
def orders():
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }

    response = requests.get(
        f"https://api.mercadolibre.com/orders/search?seller={SELLER_ID}",
        headers=headers
    )

    return response.json()
