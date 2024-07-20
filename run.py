#run.py
#import the create_app function to initialize the Flask application
from app import create_app

#create an instance of the Flask application
app = create_app()

#run the application in debug mode
if __name__=='__main__':
    app.run(debug=True)
