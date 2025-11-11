from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from .services import utilities

app = FastAPI()


@app.get('/')
async def list_tasks():
    try:
        result = await utilities.get_all_tasks_or_not_found()
        if 'tasks' in result:
            return JSONResponse(content=result, status_code=200)
        return JSONResponse(content=result, status_code=404)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not resolve request: {e}")


@app.get('/title/{title}')
async def read_task_by_title(title: str):
    try:
        result = await utilities.get_task_by_title_or_not_found(title)
        if 'tasks' in result:
            return JSONResponse(content=result, status_code=200)
        return JSONResponse(content=result, status_code=404)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not resolve request: {e}")


@app.get('/deadline/{deadline}')
async def read_tasks_by_deadline(deadline: str):
    try:
        result = await utilities.get_tasks_by_deadline_or_not_found(deadline)
        if 'tasks' in result:
            return JSONResponse(content=result, status_code=200)
        return JSONResponse(content=result, status_code=404)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not resolve request: {e}")


@app.post('/create')
async def create_new_task(request: Request):
    try:
        payload = await request.json()
        result = await utilities.create_task_or_fail(payload.get('title'), payload.get('deadline'))
        if 'tasks' in result:
            return JSONResponse(content=result, status_code=201)
        return JSONResponse(content=result, status_code=400)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not resolve request: {e}")


@app.put('/update')
async def update_task(request: Request):
    try:
        payload = await request.json()
        result = await utilities.update_task_or_fail(
            payload.get('title'), 
            payload.get('deadline'), 
            payload.get('new_title')
        )
        if result.get('tasks'):
            return JSONResponse(content=result, status_code=200)
        elif result.get('message') == 'task not found':
            return JSONResponse(content=result, status_code=404)
        return JSONResponse(content=result, status_code=400)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not resolve request: {e}")


@app.delete('/delete')
async def delete_task(request: Request):
    try:
        payload = await request.json()
        result = await utilities.delete_task_or_fail(payload.get('title'))
        if result.get('message') == 'task deleted':
            return JSONResponse(content=result, status_code=200)
        elif result.get('message') == 'task not found':
            return JSONResponse(content=result, status_code=404)
        return JSONResponse(content=result, status_code=400)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Could not resolve request: {e}")
