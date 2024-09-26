from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Initialize FastAPI app
app = FastAPI()

# Serve the static files (JS, CSS, images) from the React build
# Adjust the directory to match your actual React build directory
app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")

# Set up Jinja2 template folder (to serve the initial HTML)
templates = Jinja2Templates(directory="templates")

# API route to serve data (this will be fetched by React)
@app.get("/api/data")
async def get_data():
    # Data that you want to send to React
    return {"message": "Hello from FastAPI!", "items": [1, 2, 3, 4, 5]}

# Root route that serves the React app (index.html)
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Serve the main HTML page which will load the React app
    return templates.TemplateResponse("index.html", {"request": request})
