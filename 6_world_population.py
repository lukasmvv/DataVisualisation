import json
from country_codes import get_country_code
import pygal.maps.world
from pygal.style import LightColorizedStyle, RotateStyle


# Load data into list
filename = "chapter_16/population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data
# Adding 3 population groups to better distinguish population sizes
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

# Print 2010 pop data for each country
# We read in a list that contains many 4 key-value dictionaries
for pop_dict in pop_data:
    if pop_dict["Year"] == "2010":
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            #print(code + ": " + str(population))
            if population < 10000000:
                cc_pops_1[code] = population
            elif population < 100000000:
                cc_pops_2[code] = population
            else:
                cc_pops_3[code] = population
        else:
            print("ERROR - " + country_name)
        #print(country_name + ": " + str(population))

#wm_style = RotateStyle("#336699")
#wm_style = RotateStyle("#336699", base_style=LightColorizedStyle)
#wm = pygal.maps.world.World(style=wm_style)

wm = pygal.maps.world.World()  # this pygal library works with 2-digit country codes
wm.title = "World Population 2010"

wm.add("0-10m", cc_pops_1)
wm.add("10m-100m", cc_pops_2)
wm.add("100m+", cc_pops_3)

wm.render_to_file("world_population_2010.svg")
