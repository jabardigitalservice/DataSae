import os
from os.path import join, dirname

from dotenv import load_dotenv
from fastapi import FastAPI, Form, Header
import uvicorn
import jwt


def get_secret():
    try:
        dotenv_path = join(dirname(__file__), '.env')
        print(dotenv_path)
        load_dotenv(dotenv_path)
        jwt_secret = os.environ['jwt_secret']
        jwt_algorithm = os.environ['jwt_algorithm']
    except Exception as e:
        print(e)
        return None

    return jwt_secret, jwt_algorithm


app = FastAPI(
    version='0.1.10',
    title='API data quality framework',
    description='API private for generating satudata quality result'
)


@app.post('/generate-data-quality-satudata')
async def generate_data_quality_satudata(username: str = Form(), authorization: str = Header(None)):
    try:
        decoded = secure(authorization)
        if decoded is None:
            return {'message': 'update your .env in the project'}

        # core.quality()
    except Exception as e:
        print(e)
        return "Unauthorized Access!"
    return {'username': username}


def secure(token):
    try:
        if get_secret() is not None:
            jwt_secret, jwt_algorithm = get_secret()
            # encoded = jwt.encode({"hello": "jds"}, jwt_secret, algorithm=jwt_algorithm)
            decoded_token = jwt.decode(token, jwt_secret, algorithms=jwt_algorithm)
            return decoded_token
    except Exception as e:
        print(e)

    return None


# development mode
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5024, debug=True)
