from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from app import get_response

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

MODEL_NAMES=["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"] 

app=FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API endpoint to intract with the chatbot using LangGraph and search tools
    it dynamically selects the model specified in the request
    """
    if request.model_name not in MODEL_NAMES:
        return {"error": "Invalid model name."}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
    
    response=get_response(llm_id, query, allow_search, system_prompt, provider)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)