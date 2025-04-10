import os

import uvicorn

import app


if __name__ == '__main__':
    # https://github.com/encode/uvicorn/blob/4fdfec4adf1ba6da5e65c8422321e203b6050052/uvicorn/main.py#L464
    uvicorn.run(
        app="app.main:app",
        host='0.0.0.0',
        port=os.environ.get('PORT', 8000),
        reload=True
    )
