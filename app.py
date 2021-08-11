from __init__ import app
from api.classifier import classifier

app.register_blueprint(classifier, url_prefix='/classifier')

if __name__ == "__main__":
    app.run('localhost', 8080)
