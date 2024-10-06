from . import db

class Hero(db.Model):
    __tablename__ = 'heroes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name
        }

    def to_dict_with_powers(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
            'hero_powers': [
                {
                    'hero_id': hp.hero_id,
                    'id': hp.id,
                    'strength': hp.strength,
                    'power': hp.power.to_dict()
                }
                for hp in self.hero_powers
            ]
        }
