from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from googletrans import Translator

app = FastAPI()
app.mount("/static", StaticFiles(directory="api/static"), name="static")
templates = Jinja2Templates(directory="api/templates")
translator = Translator()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate")
async def translate(request: Request):
    data = await request.form()
    text = data["text"]
    translated_text = translator.translate(text, src='en', dest='fr').text
    return {"translated_text": translated_text}
