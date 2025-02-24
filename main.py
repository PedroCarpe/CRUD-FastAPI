from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates= Jinja2Templates(directory="templates")

@app.get("/",response_class=HTMLResponse)
def show_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/submit_form/")
def submit_form(name: str = Form(...), email: str = Form()):
    return {"name": name, "email": email}