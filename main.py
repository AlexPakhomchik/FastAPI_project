from fastapi import FastAPI

from FastAPI_project.search_info import search_info

app = FastAPI()
app.include_router(search_info)


