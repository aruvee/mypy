from flask import Flask
from flask_cors import CORS

python = Flask(__name__)
CORS(python)
from python import enter
from python import entertrade
from python import enterwatch
from python import entergann
from python import entergannpop
from python import tradedao
from python import index
from python import enterportfolio
from python import enterchange
from python import WatchRestService