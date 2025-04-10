import os

import uvicorn

import app


if __name__ == '__main__':
    # https://github.com/encode/uvicorn/blob/master/uvicorn/main.py#L469
    PORT: str = os.environ.get('PORT', '8000')
    uvicorn.run(
        app="app.main:app",
        host='0.0.0.0',
        port=int(PORT),
        reload=True
    )
