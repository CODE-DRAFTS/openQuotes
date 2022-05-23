from fastapi import FastAPI
import psycopg2
from  psycopg2.extras  import RealDictCursor
from app import env
from app.routers import authors ,quotes
from time import sleep

while True:
    try:
        conn = psycopg2.connect( host= env.DATABASE_HOST, user= env.DATABASE_USER , database= env.DATABASE_NAME , password= env.DATABASE_PASSWORD , cursor_factory= RealDictCursor)
        cursor = conn.cursor()
        print(" db connection ok")
        break
    except Exception as error:
        sleep(1)

        
app = FastAPI()

app.include_router( quotes.router)
app.include_router( authors.router)

@app.get('/')
def root():
    return {
        "app": "Q Qoutes",
        "version": "1.0.0",
        "developer": "Bernard Njeru  Mtwaiti"
    }