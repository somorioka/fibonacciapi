from fastapi.testclient import TestClient

from app.main import app
client = TestClient(app)

#nに1以上の整数値が与えられた場合
def test_fib():
    response = client.get("/fib?n=99")
    assert response.status_code == 200
    assert response.json() == {"result": 218922995834555169026}

#nに0以下の整数値が与えられた場合
def test_fib_bad_number():
    response = client.get("/fib?n=-3")
    assert response.status_code == 400
    assert response.json() == {
        "status":"400",
        "message": "1以上の整数を入力してください"
        }

#nにstr型の値が与えられた場合
def test_fib_bad_request():
    response = client.get("/fib?n=a")
    assert response.status_code == 400
    assert response.json() == {
        "status":"400",
        "message": "Bad request"
        }