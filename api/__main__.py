from api import *

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, port=8000) 
