from waitress import serve
from app import app, db
from app.models import User, Contact

if __name__ == '__main__':
  serve(app, port=80, host='0.0.0.0')
