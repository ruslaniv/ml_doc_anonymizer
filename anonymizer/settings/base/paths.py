import os
from pathlib import Path

import anonymizer as app

# location of manage.py
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# location of settings file or folder
# PROJECT_DIR = os.path.dirname(os.path.realpath(app.__file__)) # old style using os.path module
PROJECT_DIR = Path(app.__file__).resolve().parent

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
