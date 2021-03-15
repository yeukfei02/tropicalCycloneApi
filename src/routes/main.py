from flask import make_response
from app import app


@app.route('/', methods=['GET'])
def main():
    data = {
        "message": "tropicalCyclone api",
    }
    return make_response(data, 200)
