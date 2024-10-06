from models import db, Hero, Power, HeroPower
from app import app

# You must import the `app` object so the seed script can access the app context and database

with app.app_context():
    # Drop all tables and recreate them (useful for resetting the database)
    db.drop_all()
    db.create_all()

    # Create some heroes
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra")
    ]

    # Add heroes to the session
    db.session.add_all(heroes)
    db.session.commit()

    # Create some powers
    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths")
    ]

    # Add powers to the session
    db.session.add_all(powers)
    db.session.commit()

    # Create some hero-powers relationships
    hero_powers = [
        HeroPower(strength="Strong", hero_id=1, power_id=2),  # Kamala Khan with flight
        HeroPower(strength="Weak", hero_id=2, power_id=1),    # Doreen Green with super strength
        HeroPower(strength="Average", hero_id=3, power_id=4), # Gwen Stacy with elasticity
        HeroPower(strength="Strong", hero_id=4, power_id=3),  # Janet Van Dyne with super human senses
        HeroPower(strength="Strong", hero_id=5, power_id=1)   # Wanda Maximoff with super strength
    ]

    # Add hero powers to the session
    db.session.add_all(hero_powers)
    db.session.commit()

    print("Database seeded successfully!")
