from flask import Flask
from create_tables import commit

app = Flask(__name__)


@app.route('/')
def hello_world():
    commit()  # This function commits the data to the database
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
