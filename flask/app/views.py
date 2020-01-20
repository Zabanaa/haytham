from app import app


@app.route('/')
def index():
    return f'Hello, thanks for using barred'

