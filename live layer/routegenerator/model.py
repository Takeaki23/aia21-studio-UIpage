from time import sleep
from random import random

import numpy  # example import to add to requirements.txt

def call(lon1, lat1, lon2, lat2, Age, Gender, Ethnicities, SpecialNeedsVisual, SpecialNeedsPhysical, WithChild, Formality, Locality, Greenness, UrbanDensity):
    sleep(1)  # mimicking computation time...

    start_point = (lon1, lat1) # These are from user inputs as a point 
    end_point = (lon2, lat2) # These are from user inputs as a point
    Age = "adult" # Select from "young", "adult", "old"
    Gender = "male" # Select from "male", "female", "other"
    Ethnicities = "Asian" # Select from "Afro", "Asian", "Europian", "Latinx", "Mid East", "South Asian"
    SpecialNeedsVisual = False # Get boolean from a check box
    SpecialNeedsPhysical = False # Get boolean from a check box
    WithChild = True # Get boolean from a check box
    Formality = 80 # get a number from integer slider 1 to 100
    Locality = 20 # get a number from integer slider 1 to 100
    Greenness = 80 # get a number from integer slider 1 to 100
    UrbanDensity = 20 # get a number from integer slider 1 to 100

    # coding to get route geometry as line
    
    route = [
        {
            "type": "Feature",
            "geometry": {
                "type": "line",
                "coordinates": [
                    16.3738 + random() / 10 - 0.05,
                    48.2082 + random() / 10 - 0.05,
                    0.0
                ]
            }
        }
    ]
    return route