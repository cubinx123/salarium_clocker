import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

salarium_creds = {'email': os.environ.get("email"),
                  'password': os.environ.get("password")
                  }

driver_details = {
                  'driver': os.environ.get("driver_name")
                  }
