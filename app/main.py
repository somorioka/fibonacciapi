from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

#インスタンス化
app = FastAPI()

#fastapiのエラー内容を上書き
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        {
            "status":"400",
            "message": "Bad request"
        },
        status_code=400
        )

@app.get("/fib/")
async def fib(n: int):
    if n <= 0:
        return JSONResponse(
            {
                "status":"400",
                "message": "1以上の整数を入力してください"
            },
            status_code=400
            )

    a, b = 1, 0
    for _ in range(n):
        a, b = a + b, a
    return {"result": b}