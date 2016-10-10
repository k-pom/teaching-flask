from flask import Flask

# Any application level configuration (like where your images and
# css files live) can be made at this level. For the most part, you
# can ignore this for now.

app = Flask(__name__,
            static_folder='static',
            static_url_path='/static')
