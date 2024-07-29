#app/__init__
from chat import routes

app = routes.app

if __name__ == '__main__':
    app.run(debug=True)