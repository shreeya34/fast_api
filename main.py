from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/')
async def root():
    return {'example':'this is an example','data':888}

@app.get('/random')
async def get_random():
    rn:int=random.randint(0,200)
    return{'number':rn,'limit':200}