from __init__ import app
from api.classifier import classifier
from api.detector import detector

app.register_blueprint(classifier, url_prefix='/classifier')
app.register_blueprint(detector, url_prefix='/detector')

if __name__ == "__main__":
    app.run('localhost', 8080)
