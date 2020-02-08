from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.routing import Route, Mount

templates = Jinja2Templates(directory='templates')

async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request})


async def unus(request):
    return JSONResponse({'cheese': 'naks'})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/unus', unus),
])