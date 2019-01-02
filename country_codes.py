from pygal.maps.world import COUNTRIES

# for country_code in sorted(COUNTRIES.keys()):
#    print(country_code, COUNTRIES[country_code])


def get_country_code(country_name):
    """Returns the Pygal 2-digit country code for a given country name"""

    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    # If country not found return none
    return None


#print(get_country_code("Andorra"))
#print(get_country_code("United Arab Emirates"))
#print(get_country_code("South Africa"))