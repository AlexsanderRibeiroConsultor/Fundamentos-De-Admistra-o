CLIENT_ID = "8950442066920082"
CLIENT_SECRET = "seu secret aqui"
REDIRECT_URI = "https://ml-backend-kndd.onrender.com/callback"
@app.get("/me")
def me():
    token = "COLE_SEU_ACCESS_TOKEN_AQUI"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get("https://api.mercadolibre.com/users/me", headers=headers)
    return response.json()
