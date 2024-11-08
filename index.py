from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/fetch-data")
def fetch_data(api_url: str):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data", "status_code": response.status_code}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
