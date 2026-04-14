from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from agent import analyze_symptoms

app = FastAPI()

# tell FastAPI where templates are
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/check")
def check(symptoms: str):
    result = analyze_symptoms(symptoms)

    return {
        "symptoms": symptoms,
        "analysis": result
    }