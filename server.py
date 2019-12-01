from waitress import serve
from app import app, db

if __name__ == '__main__':
  serve(app, port=80, host='0.0.0.0')
