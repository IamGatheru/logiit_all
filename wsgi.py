# Set path

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app1 import create_app 
application = create_app
app = application

#if __name__ == "__main__":
#    app.run()
