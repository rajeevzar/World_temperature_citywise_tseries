#!/usr/bin/env python
# coding: utf-8

# In[12]:


from geopy.geocoders import Nominatim

def get_city_coordinates(city_name, bounds = 0.5 ): # bound is a box area in degrees around City region, Default = 0.5
    """
    Fetches the latitude and longitude of a given city name using Geopy.

    Args:
        city_name (str): Name of the city.

    Returns:
        tuple: (latitude, longitude) of the city.
    """
    # Initialize the geolocator object
    geolocator = Nominatim(user_agent="city_locator")  # Must be inside the function
    location = geolocator.geocode(city_name)
    if location:
        lat_min = location.latitude - bounds
        lat_max = location.latitude + bounds
        long_min = location.longitude - bounds
        long_max = location.longitude + bounds
        return location.latitude, location.longitude, lat_min, lat_max, long_min, long_max
    else:
        raise ValueError(f"Could not find coordinates for city: {city_name}")


# In[ ]:





# In[ ]:




