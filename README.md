# aia21-studio-UIpage

static layers

line documentation
https://docs.mapbox.com/mapbox-gl-js/style-spec/layers/#paint-line-line-blur

fill documentation
https://docs.mapbox.com/mapbox-gl-js/style-spec/layers/#paint-fill-fill-antialias

symbol documentation
https://docs.mapbox.com/mapbox-gl-js/style-spec/layers/#symbol

gradient line doc
https://docs.mapbox.com/mapbox-gl-js/example/line-gradient/


## Structure for Static layer

* BIO  
    * &ensp;Age  
        &emsp;Adult  
            &emsp;&ensp;adult.geojson  
            &emsp;&ensp;style.json  
        &emsp;Old  
            &emsp;&ensp;old.geojson  
            &emsp;&ensp;style.json  
        &emsp;Young  
            &emsp;&ensp;young.geojson  
            &emsp;&ensp;style.json  
    * &ensp;Ethnic diversity  
        &emsp;div_ethnic_diversity_index.geojson (Show as geo: "diversity_index" , Attributes: "afro_ratio", "asian_ratio", "mid_east_ratio", "south_asian_ratio", "latinx_ratio", "european_ratio")  
        &emsp;style.json  
            &emsp;Afro Carribean  
                &emsp;&ensp;div_afro_carribean_heatmap.geojson  
                &emsp;&ensp;style.json  
            &emsp;Asian  
                &emsp;&ensp;div_asian_heatmap.geojson  
                &emsp;&ensp;style.json  
            &emsp;Europian  
                &emsp;&ensp;div_european_origin_heatmap.geojson  
                &emsp;&ensp;style.json  
            &emsp;Latinx  
                &emsp;&ensp;div_latin_american_heatmap.geojson  
                &emsp;&ensp;style.json  
            &emsp;Mid_east  
                &emsp;&ensp;div_mid_east_heatmap.geojson  
                &emsp;&ensp;style.json  
            &emsp;South_asian  
                &emsp;&ensp;div_south_asian_heatmap.geojson  
                &emsp;&ensp;style.json  
            &emsp;LGBTQ  
                &emsp;&ensp;div_lgbtq_heatmap.geojson  
                &emsp;&ensp;style.json  
    * &ensp;Income  
        &emsp;Income.geojson (Show as geo: "INC_TOT_VALUE" , Attributes: "INC_MAL_VALUE", "INC_FEM_VALUE")  
        &emsp;style.json  
    * &ensp;Population  
        &emsp;Population.geojson (Show as geo: "total_pop" , Attributes: tot_m"en, "tot_wom", "tot_aus_ratio", &emsp;"tot_foreign_ratio", "density")  
        &emsp;style.json  
    * &ensp;Religion  
        &emsp;Religion.geojson (Show as geo: "rom-cath" , Attributes: "evang", "jew", "islam", "ortho", "other", "without")  
        &emsp;style.json  
    
* Urban Diversity  
    * &ensp;Greeness  
        &emsp;trees.geojson (Show as geo: "tree_index" , Attributes: "name", "tree_counts")  
        &emsp;style.json  
    * &ensp;Public Image
        &emsp;public_image.geojson (Show as geo: "weighted_sum" , Attributes: "name", "tree_index", "public_toilets", "drinking_fountain")  
        &emsp;style.json  
    * &ensp;Urban Density  
        &emsp;urban_density.geojson (Show as geo: "urban_density")  
        &emsp;style.json  

* Accessibility  
    * &ensp;Physical  
        &emsp;acc_wheelchair_friendly.geojson (Show as geo: "wheelchair_friendly_index" , Attributes: "name", "elevators", "low_sidewalk", "sidewalk_width", "disabled_parking")  
        &emsp;style.json  
    * &ensp;Visual  
        &emsp;acc_visual_friendly.geojson (Show as geo: "visual_friendly_index" , Attributes: "name", "acoustic_lights", "tactile_sidewalks", "low_sidewalk")  
        &emsp;style.json  


## Structure for live layer

* POIselector
    * &ensp;geo.geojson  
    * &ensp;POI_live_layer.py  
    * &ensp;requirements.txt  
    * &ensp;style.json  
    * &ensp;near_me.svg  
        

* RouteGenerator  
    * &ensp;geo.geojson  
    * &ensp;ROUTE_live_layer.py  
    * &ensp;requirements.txt  
    * &ensp;style.json  
