from project import app  # __init__ files are a good place to look

# Load all of our routes
from project.routes import home, register

# Actually run the application
if __name__ == '__main__':
    app.run(debug=True, port=3000)
