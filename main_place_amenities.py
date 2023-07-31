#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity


# creation of 2 Places
place_1 = Place(user_id="72bd56f2-23cc-4552-b6c4-ccb4aa4b34000", city_id="469331a2-9608-46bc-8fdc-609e2cfdedf0", name="House 1")
place_1.save()
place_2 = Place(user_id="72bd56f2-23cc-4552-b6c4-ccb4aa4b34000", city_id="469331a2-9608-46bc-8fdc-609e2cfdedf0", name="House 2")
place_2.save()

# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable")
amenity_2.save()
amenity_3 = Amenity(name="Oven")
amenity_3.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

storage.save()

print("OK")

