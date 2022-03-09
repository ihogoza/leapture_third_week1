from flask import Flask

app = Flask(__name__)

def create_app(testing: bool = True):
    
    
    @app.route('/')
    def index():
        return f'Hello World<br>Testing: {testing}'
    
    return app

create_app()