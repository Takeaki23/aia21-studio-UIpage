import matplotlib.pyplot as plt
import networkx as nx
import osmnx as ox
import geopandas as gpd
import shapely

from time import sleep
from random import random




def call(age:str, gender:str, ethnicity:str, religion:str, special_needs_visual:bool,special_needs_physical:bool, with_child:bool, formality:float, origin = (48.19, 16.362) ):
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
    origin      : Starting location specified as a tuple of (lat, lon)

    returns : poi call returns geojson with Point geometry, route call returns geojson with Linestring geometry
    '''
    

    #-----------------------------------POI DATAFRAME---------------------------------------#
    #GET POI DATA
    poi_url = 'https://drive.google.com/file/d/1-6ze3N_dlBBNcixZK9a33Iu8WqAZCY9m/view?usp=sharing'
    poi_url='https://drive.google.com/uc?id=' + poi_url.split('/')[-2]
    poi_data = gpd.read_file(poi_url)
    poi_data = poi_data.drop(columns = ['tourism', 'shop'])
    poi_data = poi_data[poi_data.geometry.type == 'Point']
    print(poi_data)
    #-----------------------------------POI DATAFRAME---------------------------------------#


    #-----------------------------------AFFECT POI WEIGHTS WITH USER INPUT---------------------------------------#
    #create personalised dataframe
    poi = poi_data.copy()
    poi['young'] = 1

    parameters = ['formality']

    #age & with_child
    if (age == 'young') | (with_child == True):
        a = 1-(poi['amenity'].astype(str).str.contains(('bar|casino|pub|nightclub|biergarten|gambling|stripclub|brothel|swingerclub|public_bath')))
        a2 = 1-(poi['leisure'].astype(str).str.contains(('adult_gaming_centre|sauna|shooting_ground|gambling')))
        poi['young'] = (a+a2)>0
        parameters.append('young')

    #gender
    if gender == 'others'.lower(): 
        parameters.append('lgbtq_friendly')
    else:
        parameters.append('male', 'female')

    #ethnicity
    for i in ethnicity:
        if i.lower() == 'afro_carribean': parameters.append('afro_carribean')
        elif i.lower() == 'asian': parameters.append('asian')
        elif i.lower() == 'middle_eastern': parameters.append('mid_east')
        elif i.lower() == 'south_asian': parameters.append('south_asian')
        elif i.lower() == 'latin_american': parameters.append('latinx')
        elif i.lower() == 'european_origin': parameters.append('european')

    #religion
    if religion.lower() == 'muslim':parameters.append('muslim_friendly')
    if religion.lower() == 'jewish':parameters.append('jewish')
    if religion.lower() == 'buddhist':parameters.append('buddhist')

    #special_needs
    if special_needs_physical == True: parameters.append('wheelchair')

    #formality
    if formality <=0.5: 
        b = (poi['amenity'].astype(str).str.contains((
            'fast_food|ice_cream|cafe|cinema|bar|pub|biergarten|None|kindergarten|nightclub|stripclub|brothel|swingerclub'))) 
        c = (poi['leisure'].astype(str).str.contains(('None|indoor_play|swimming_pool|outdoor_seating|playground|bowling_alley\
            |scouts|marina|track|amusement_arcade|park|hackerspace|slipway|pitch|dog_park|yes|halfpipe|escape_game|Parklet\
            |miniature_golf|garden|parklet|trampoline_park|picnic_table|ice_rink|water_park|golf_course|nature_reserve|swimming_area\
            |common|stadium|maze|recreation_ground|green|proposed|high_ropes_course|resort'))) 
    else :
        b = (poi['amenity'].astype(str).str.contains(('restaurant|casino|gambling|dancing_school|college|doctors|public_bath\
            |university|parking|school|dojo|fountain|None')))
        c = (poi['leisure'].astype(str).str.contains(('sports_centre|horse_riding|sports_hall|disc_golf_course\
            |fitness_centre|dance|yoga|gambling|tanning_salon|sauna|adult_gaming_centre|fitness_station|shooting_ground')))
    poi['formality'] = b+c




    #compile data with parameters
    poi_selected = poi.loc[:, parameters]
    if age == 'young':
        poi_selected['boolean'] = (poi_selected.sum(axis=1) > 0) * poi.young
    else:
        poi_selected['boolean'] = poi_selected.sum(axis=1) > 0

    poi_selected['name'] = poi['name']
    poi_selected['addr:street'] = poi['addr:street']
    poi_selected['geometry'] = poi['geometry']
    poi_selected = poi_selected[poi_selected['boolean']]
    poi_selected = poi_selected.replace([True, False],['Yes', '-'])
    poi_selected.drop([col for col in poi_selected.columns if col in ['boolean', 'formality', 'european']], inplace = True, axis=1)

    #-----------------------------------AFFECT POI WEIGHTS WITH USER INPUT---------------------------------------#



    #-----------------------------------REDCUE POI OPTIONS TO A CERTAIN RANGE---------------------------------------#
    origin2 = gpd.GeoSeries(shapely.geometry.Point(origin[1], origin[0]))
    origin2 = origin2.set_crs('epsg:4326')
    origin_proj = ox.project_gdf(origin2, to_crs = 'epsg:3857')
    poi_proj = ox.project_gdf(poi_selected, to_crs = 'epsg:3857')
    nearest =origin_proj .sindex.nearest(poi_proj.geometry, max_distance = 1000, return_distance = True)

    poi_output = poi_selected.iloc[nearest[0][0], :]
    poi_output_json = poi_output.to_json()

    return poi_output_json 
     #-----------------------------------REDCUE POI OPTIONS TO A CERTAIN RANGE---------------------------------------#