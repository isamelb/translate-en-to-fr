from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from googletrans import Translator, LANGUAGES
import traceback

def get_translator():
    return Translator(service_urls=['translate.google.com'])

app = FastAPI()
app.mount("/static", StaticFiles(directory="api/static"), name="static")
templates = Jinja2Templates(directory="api/templates")
translator = get_translator()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/translate")
async def translate(request: Request):
    try:
        data = await request.form()
        text = data["text"]
        translated_text = translator.translate(text, src='en', dest='fr').text
        return {"translated_text": translated_text}
    except Exception as e:
        print(traceback.format_exc())
        return {"error": str(e)}
