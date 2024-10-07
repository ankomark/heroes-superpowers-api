from flask import Flask, jsonify, request #type: ignore
from models import db, Hero, Power, HeroPower
from flask_migrate import Migrate #type: ignore

# Initializing Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing SQLAlchemy and Flask-Migrate
db.init_app(app)
migrate = Migrate(app, db)

# Defining routes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict_with_powers())
    return jsonify({"error": "Hero not found"}), 404

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    return jsonify({"error": "Power not found"}), 404

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    try:
        # Check if required fields exist in the request data
        if 'strength' not in data or 'hero_id' not in data or 'power_id' not in data:
            raise ValueError("Missing required fields")

        # Find hero and power
        hero = Hero.query.get(data['hero_id'])
        power = Power.query.get(data['power_id'])
        if not hero or not power:
            raise ValueError("Hero or Power not found")

        # Validate strength and create HeroPower
        hero_power = HeroPower(strength=data['strength'], hero_id=data['hero_id'], power_id=data['power_id'])
        HeroPower.validate_strength(data['strength'])
        db.session.add(hero_power)
        db.session.commit()

        # Return the new HeroPower data with related hero and power information
        return jsonify({
            "id": hero_power.id,
            "hero_id": hero_power.hero_id,
            "power_id": hero_power.power_id,
            "strength": hero_power.strength,
            "hero": {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            },
            "power": {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
        }), 201
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400


@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    data = request.json
    try:
        # Check if 'description' exists in the request data
        if 'description' not in data:
            raise ValueError("Description is required")

        power.description = data['description']

        # Assuming you have a validate method in the Power model
        power.validate()
        db.session.commit()

        # Return the updated Power object with id and name
        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        })
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400


if __name__ == '__main__':
    app.run(port=5555, debug=True)  # Setting the port to 5555
