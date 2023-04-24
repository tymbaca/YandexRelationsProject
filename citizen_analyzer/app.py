from aiohttp.web import Application
from sqlalchemy import create_engine

from citizen_analyzer.settings import DATABASE_URL
from citizen_analyzer.api.urls import setup_routes

class App:
    def __init__(self, 
                 web_app: Application,
                 database_engine
                 ) -> None:
        self.web_app = web_app
        self.database_engine = database_engine
    
app = App(web_app=Application,
          database_engine=create_engine(DATABASE_URL))
setup_routes(app)
