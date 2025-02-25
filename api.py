from fastapi import FastAPI, HTTPException, Header, Request
import jwt
import time
import uuid
from pydantic import BaseModel

# Configuración
API_KEY = "2f5ae96c-b558-4c7b-a590-a501ae1c3f6c"
SECRET_KEY = "mysecret"

app = FastAPI()

# Modelo de datos esperado
class MessageRequest(BaseModel):
    message: str
    to: str
    from_: str  
    timeToLifeSec: int

# Función para generar JWT
def generate_jwt():
    payload = {
        "jti": str(uuid.uuid4()),
        "iat": int(time.time()),
        "exp": int(time.time()) + 60  # Expira en 60 segundos
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

@app.post("/DevOps")
def devops_endpoint(
    request_data: MessageRequest,
    x_parse_rest_api_key: str = Header(None),
    x_jwt_kwy: str = Header(None)
):
    # Validación de la API Key
    if x_parse_rest_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    
    # Generar un nuevo JWT por cada transacción
    new_jwt = generate_jwt()
    
    response = {
        "message": f"Hello {request_data.to} your message will be sent"
    }
    return response

@app.get("/DevOps")
def invalid_method():
    raise HTTPException(status_code=405, detail="ERROR")

@app.put("/DevOps")
def invalid_method():
    raise HTTPException(status_code=405, detail="ERROR")

@app.delete("/DevOps")
def invalid_method():
    raise HTTPException(status_code=405, detail="ERROR")
