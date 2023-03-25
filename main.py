from fastapi import FastAPI
import uvicorn
from summarize import summarize_text

app = FastAPI()

@app.get("/summary")
async def summarize(text: str):
    summary = summarize_text(text)
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)