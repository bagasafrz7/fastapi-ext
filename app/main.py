from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.routes.notes import notes_router

app = FastAPI()


app.include_router(notes_router)


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
