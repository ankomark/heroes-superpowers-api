from flask_sqlalchemy import SQLAlchemy # type: ignore

db = SQLAlchemy()

# Importing models that will be used in the project
from .hero import Hero
from .power import Power
from .hero_power import HeroPower
