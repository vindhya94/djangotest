from Django import Django 

app = Django(__name__)


@app.route('/')
def counter():
    return 'Hello django!!!'
