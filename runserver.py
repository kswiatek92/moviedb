import uvicorn

from moviedb import settings

if __name__ == "__main__":
    uvicorn.run(
        "moviedb.app:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        debug=settings.DEBUG,
        reload=settings.DEBUG,
    )
