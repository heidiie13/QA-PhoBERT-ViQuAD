import sys
import os
sys.path.insert(0, (os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))))
import app.core_ai.qa as qa
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    question: str
    context: str

@app.post("/predict")
async def predict(query: Query):
    answer = qa.get_answer(query.question, query.context)
    if answer is None:
        raise HTTPException(status_code=404, detail="Not found answer....")
    return {
        "question": query.question,
        "context": query.context,
        "answer": answer
    }
