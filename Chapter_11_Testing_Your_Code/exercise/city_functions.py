
def get_city_country_names(city, country, population=0):
    """ Function returns city and country name in formatted way."""
    if population:
        formatted_string = f"{city}, {country} - population {population}"
    else:
        formatted_string = f"{city}, {country}"
    
    return formatted_string.title()



    