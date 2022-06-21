import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox
import geopandas as gpd
import pandas as pd
import momepy
import shapely

from random import random



def call(age:str, gender:str, ethnicity:str, religion:str, special_needs_visual:bool,special_needs_physical:bool, with_child:bool, formality:float, public_image:float, origin = (48.19, 16.362), destination = (48.20, 16.364), call_type='poi' ):
    '''takes in user profile and preferences and returns either preferred poi or generated route
    
    args:
    age         : Select from "young", "adult", "old"
    gender      : drop_down_options = ('male', 'female', 'other')
    ethnicity   : checkbox_options = ('afro_carribean', 'asian', middle_eastern', 'south_asian', 'latin_american', 'european_origin')
    religion    : drop_down options = ('christian', 'muslim', 'jewish', 'buddhist', 'hinduism', 'others', 'none' )#Multiple options allowed for ethnicity
    special_needs_visual    : Get boolean from a check box
    special_needs_physical  : Get boolean from a check box
    with_child  : Get boolean from a check box
    formality   : Slider with range of 0 to 1
    public_image    : Slider with range of 0 to 1

    returns : poi call returns geojson with Point geometry
    '''
    
    #-----------------------------------CITY STREETS DATAFRAME---------------------------------------#
    #GET PUBLIC IMAGE DATA
    urban_image_url = 'https://drive.google.com/file/d/1-6ze3N_dlBBNcixZK9a33Iu8WqAZCY9m/view?usp=sharing'
    urban_image_url='https://drive.google.com/uc?id=' + urban_image_url.split('/')[-2]
    urban_image = gpd.read_file(urban_image_url)

    #GET ACCESSIBILITY VISUAL DATA
    acc_visual_url = 'https://drive.google.com/file/d/1-F8eNxXaHHoGORyHbJk8zT0BLsu_aZdx/view?usp=sharing'
    acc_visual_url='https://drive.google.com/uc?id=' + acc_visual_url.split('/')[-2]
    acc_visual = gpd.read_file(acc_visual_url)

    #GET ACCESSIBILITY WHEELCHAIR DATA
    acc_wheelchair_url = 'https://drive.google.com/file/d/1-GOp9cvgg-j6Dn8kaThwsU1JzUDo64aj/view?usp=sharing'
    acc_wheelchair_url='https://drive.google.com/uc?id=' + acc_wheelchair_url.split('/')[-2]
    acc_wheelchair = gpd.read_file(acc_wheelchair_url)

    #GET CITY EDGES INFORMATION INTO ONE DATAFRAME
    city_edges = urban_image.loc[:, ['name', 'weighted_sum']]
    city_edges.weighted_sum = 1-city_edges.weighted_sum
    city_edges['blind_friendly'] = 1-acc_visual['visual_friendly_index']
    city_edges['wheelchair_friendly'] = 1-acc_wheelchair['wheelchair_friendly_index']
    city_edges['geometry'] = acc_wheelchair['geometry']
    city_edges = city_edges.rename(columns={'weighted_sum':'urban_image'})
    #-----------------------------------CITY STREETS DATAFRAME---------------------------------------#

    #-----------------------------------AFFECT STREET WEIGHTS WITH USER INPUT---------------------------------------#
    crs = 'epsg:4326'

    #create personalised dataframe
    routes_edges = city_edges.copy()

    #edit urban image
    routes_edges.urban_image = (1-public_image)*city_edges.urban_image

    #edit special_needs_visual
    if special_needs_visual:
        routes_edges.blind_friendly = city_edges.blind_friendly
    else:
        routes_edges.blind_friendly = 1.0

    #edit special_needs_physical
    if special_needs_physical:
        routes_edges.wheelchair_friendly = city_edges.wheelchair_friendly
    else:
        routes_edges.wheelchair_friendly = 1.0

    routes_edges['edge_weights'] = routes_edges.urban_image + routes_edges.blind_friendly + routes_edges.wheelchair_friendly
    #-----------------------------------AFFECT STREET WEIGHTS WITH USER INPUT---------------------------------------#

    


#DEFINE USER INPUTS FOR TESTING
#PROFILE
age = 'adult' # Select from "young", "adult", "old"
gender = 'female' #drop_down_options = ('male', 'female', 'other')
ethnicity = ['latin_american'] #checkbox_options = ('afro_carribean', 'asian', middle_eastern', 'south_asian', 'latin_american', 'european_origin')
religion = 'muslim' #drop_down options = ('christian', 'muslim', 'jewish', 'buddhist', 'hinduism', 'others', 'none' )
#Multiple options allowed for ethnicity
special_needs_visual = False #Get boolean from a check box
special_needs_physical = False # Get boolean from a check box
with_child = True # Get boolean from a check box

#PREFERENCES
formality = 0 #Slider with range of 0 to 1
public_image = 0.5 #Slider with range of 0 to 1

#CALL
call_type = 'poi'
call(age, gender, ethnicity, religion, special_needs_visual, special_needs_physical, with_child, formality, public_image)
