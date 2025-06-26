from enum import Enum
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi import status
import pandas as pd

app = FastAPI()

class Supported_State(str, Enum):
    Vic = "Vic"
    NSW = "NSW"
    QLD = "QLD"
    SA = "SA"
    TAS = "TAS"

@app.get("/")
async def hello_world():
    return JSONResponse(
        status_code=200,
        content={
            "message": "Hello World"
        }
    )

@app.get("/mean-price")
async def get_mean_price(state: Supported_State):
    df = pd.read_csv("data/coding_challenge_prices.csv")

    filtered = df[df['state'] == state]

    if filtered.empty:
        return JSONResponse(
            status_code=404,
            content={
                "error": f"No data found for state: {state.value}",
        }
    )
    
    mean_price = filtered['price'].mean()

    return JSONResponse(
        status_code=200,
        content={
            "state": state,
            "mean_price": round(mean_price, 2)
        }
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    # Default fallback for other validation errors
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"error": f"Invalid state value. Supported states: {[s.value for s in Supported_State]}"}
    )
