#Cathy Doherty
import dbm
photo_category = dbm.open ("photos", "c")
photo_category["animals.png"] = "birds in nature"
photo_category["cars.png"] = "Ford Broncos"
photo_category["family.png"] = "my dad and brother"

print(photo_category)
