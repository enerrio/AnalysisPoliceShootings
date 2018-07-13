#!/usr/bin/env python

from geopy.geocoders import Nominatim
import time
import numpy as np
import pandas as pd


def get_coordinates(data):
    """
    Use geocoding to get lat/lon coordinates from city, state

    Args:
        data: Pandas dataframe of WaPo dataset
    Returns:
        Original dataframe with 2 extra latitude/longitude columns
    """
    # Restrict geocoding to recognize locations ONLY in USA
    geolocator = Nominatim(format_string="%s, United States of America", user_agent="my-application")

    coordinates = {}
    cities_skip = []
    for (city, state), row in data.groupby(['city', 'state']):
        city_state = "%s, %s" % (city, state)
        if city_state in cities_skip:
            latitude = np.nan
            longitude = np.nan
        else:
            try:
                _, (latitude, longitude) = geolocator.geocode(city_state, timeout=5)
            # If address cannot be found, set it to NaN and find coordinates manually
            except:
                print("Error", city_state)
                cities_skip.append(city_state)
                latitude = np.nan
                longitude = np.nan
        coordinates[city_state] = [latitude, longitude]
        # Sleep to avoid sending too many requests to Nominatim servers at once
        time.sleep(1)
    # Iterate over dictionary and assign coordinates to correct city/state pair
    for city_state in coordinates.keys():
        latitude = coordinates[city_state][0]
        longitude = coordinates[city_state][1]
        city, state = [x.strip() for x in city_state.split(',')]
        data.loc[(data['city'] == city) & (data['state'] == state), 'lat'] = latitude
        data.loc[(data['city'] == city) & (data['state'] == state), 'lon'] = longitude
    return data


def add_coordinates(data):
    """
    Add coordinates to cities that weren't geocoded

    Args:
        data: Pandas DataFrame containing original data and lat/lon data
    Returns:
        None, but the original data is updated with new coordinates
    """
    # Update NaN lat/lon values with actual coordinates
    data.loc[(data['city'] == "Maricopa") & (data['state'] == "AZ"), 'lat'] = 33.058106
    data.loc[(data['city'] == "Maricopa") & (data['state'] == "AZ"), 'lon'] = -112.047642

    data.loc[(data['city'] == "Eaton Rapids Township") & (data['state'] == "MI"), 'lat'] = 42.568147
    data.loc[(data['city'] == "Eaton Rapids Township") & (data['state'] == "MI"), 'lon'] = -84.752448

    data.loc[(data['city'] == "Green Bay") & (data['state'] == "WI"), 'lat'] = 44.513319
    data.loc[(data['city'] == "Green Bay") & (data['state'] == "WI"), 'lon'] = -88.013296

    data.loc[(data['city'] == "Roxand Township") & (data['state'] == "MI"), 'lat'] = 42.729993
    data.loc[(data['city'] == "Roxand Township") & (data['state'] == "MI"), 'lon'] = -84.877639

    data.loc[(data['city'] == "San Antonio") & (data['state'] == "TX"), 'lat'] = 29.424122
    data.loc[(data['city'] == "San Antonio") & (data['state'] == "TX"), 'lon'] = -98.493628

    data.loc[(data['city'] == "Red Valley") & (data['state'] == "AZ"), 'lat'] = 36.603994
    data.loc[(data['city'] == "Red Valley") & (data['state'] == "AZ"), 'lon'] = -109.060383

    data.loc[(data['city'] == "Straban Township") & (data['state'] == "PA"), 'lat'] = 39.871606
    data.loc[(data['city'] == "Straban Township") & (data['state'] == "PA"), 'lon'] = -77.173531

    data.loc[(data['city'] == "South El Monte") & (data['state'] == "CA"), 'lat'] = 34.051955
    data.loc[(data['city'] == "South El Monte") & (data['state'] == "CA"), 'lon'] = -118.046734

    data.loc[(data['city'] == "St. Petersburg") & (data['state'] == "FL"), 'lat'] = 27.767601
    data.loc[(data['city'] == "St. Petersburg") & (data['state'] == "FL"), 'lon'] = -82.640291

    data.loc[(data['city'] == "Watsonsville") & (data['state'] == "CA"), 'lat'] = 36.910231
    data.loc[(data['city'] == "Watsonsville") & (data['state'] == "CA"), 'lon'] = -121.756895

    data.loc[(data['city'] == "Pinion Hills") & (data['state'] == "CA"), 'lat'] = 34.433237
    data.loc[(data['city'] == "Pinion Hills") & (data['state'] == "CA"), 'lon'] = -117.646792

    data.loc[(data['city'] == "Palm Beach Gardens") & (data['state'] == "FL"), 'lat'] = 26.823395
    data.loc[(data['city'] == "Palm Beach Gardens") & (data['state'] == "FL"), 'lon'] = -80.138655

    data.loc[(data['city'] == "West Goshen") & (data['state'] == "CA"), 'lat'] = 36.351062
    data.loc[(data['city'] == "West Goshen") & (data['state'] == "CA"), 'lon'] = -119.420120

    data.loc[(data['city'] == "North Laredo") & (data['state'] == "TX"), 'lat'] = 27.530567
    data.loc[(data['city'] == "North Laredo") & (data['state'] == "TX"), 'lon'] = -99.480324

    data.loc[(data['city'] == "Mountain Pine") & (data['state'] == "AR"), 'lat'] = 34.572035
    data.loc[(data['city'] == "Mountain Pine") & (data['state'] == "AR"), 'lon'] = -93.173240

    data.loc[(data['city'] == "South Greensburg") & (data['state'] == "PA"), 'lat'] = 40.278403
    data.loc[(data['city'] == "South Greensburg") & (data['state'] == "PA"), 'lon'] = -79.544762

    data.loc[(data['city'] == "Pueblo of Laguna") & (data['state'] == "NM"), 'lat'] = 35.035654
    data.loc[(data['city'] == "Pueblo of Laguna") & (data['state'] == "NM"), 'lon'] = -107.386223

    data.loc[(data['city'] == "Benton") & (data['state'] == "IL"), 'lat'] = 37.996716
    data.loc[(data['city'] == "Benton") & (data['state'] == "IL"), 'lon'] = -88.920069

    data.loc[(data['city'] == "Fayetteville") & (data['state'] == "AR"), 'lat'] = 36.082156
    data.loc[(data['city'] == "Fayetteville") & (data['state'] == "AR"), 'lon'] = -94.171854

    data.loc[(data['city'] == "El Paso") & (data['state'] == "TX"), 'lat'] = 31.761878
    data.loc[(data['city'] == "El Paso") & (data['state'] == "TX"), 'lon'] = -106.485022

    data.loc[(data['city'] == "St. Martin") & (data['state'] == "MS"), 'lat'] = 30.437976
    data.loc[(data['city'] == "St. Martin") & (data['state'] == "MS"), 'lon'] = -88.868085

    data.loc[(data['city'] == "Jacksonville") & (data['state'] == "FL"), 'lat'] = 30.332184
    data.loc[(data['city'] == "Jacksonville") & (data['state'] == "FL"), 'lon'] = -81.655651

    data.loc[(data['city'] == "Lake Asbury") & (data['state'] == "FL"), 'lat'] = 30.049129
    data.loc[(data['city'] == "Lake Asbury") & (data['state'] == "FL"), 'lon'] = -81.821487

    data.loc[(data['city'] == "Lake City") & (data['state'] == "SC"), 'lat'] = 33.870996
    data.loc[(data['city'] == "Lake City") & (data['state'] == "SC"), 'lon'] = -79.755345

    data.loc[(data['city'] == "McKinneyville") & (data['state'] == "CA"), 'lat'] = 40.946515
    data.loc[(data['city'] == "McKinneyville") & (data['state'] == "CA"), 'lon'] = -124.100620

    data.loc[(data['city'] == "East Hollywood") & (data['state'] == "CA"), 'lat'] = 34.091341
    data.loc[(data['city'] == "East Hollywood") & (data['state'] == "CA"), 'lon'] = -118.293589

    data.loc[(data['city'] == "Weeki Wachi") & (data['state'] == "FL"), 'lat'] = 28.515551
    data.loc[(data['city'] == "Weeki Wachi") & (data['state'] == "FL"), 'lon'] = -82.572877

    data.loc[(data['city'] == "Logan Canyon") & (data['state'] == "UT"), 'lat'] = 41.740209
    data.loc[(data['city'] == "Logan Canyon") & (data['state'] == "UT"), 'lon'] = -111.793831

    data.loc[(data['city'] == "Springdale") & (data['state'] == "AR"), 'lat'] = 36.186744
    data.loc[(data['city'] == "Springdale") & (data['state'] == "AR"), 'lon'] = -94.128814

    data.loc[(data['city'] == "Muckleshoot Indian Reservation") & (data['state'] == "WA"), 'lat'] = 47.251720
    data.loc[(data['city'] == "Muckleshoot Indian Reservation") & (data['state'] == "WA"), 'lon'] = -122.115322

    data.loc[(data['city'] == "North St. Louis") & (data['state'] == "MO"), 'lat'] = 38.606842
    data.loc[(data['city'] == "North St. Louis") & (data['state'] == "MO"), 'lon'] = -90.250129

    data.loc[(data['city'] == "Simpsonsville") & (data['state'] == "KY"), 'lat'] = 38.222570
    data.loc[(data['city'] == "Simpsonsville") & (data['state'] == "KY"), 'lon'] = -85.355235

    data.loc[(data['city'] == "Forks Township") & (data['state'] == "PA"), 'lat'] = 40.734543
    data.loc[(data['city'] == "Forks Township") & (data['state'] == "PA"), 'lon'] = -75.212900

    data.loc[(data['city'] == "Lancaster City") & (data['state'] == "PA"), 'lat'] = 40.037875
    data.loc[(data['city'] == "Lancaster City") & (data['state'] == "PA"), 'lon'] = -76.305514

    data.loc[(data['city'] == "Golden Shores") & (data['state'] == "AZ"), 'lat'] = 34.786283
    data.loc[(data['city'] == "Golden Shores") & (data['state'] == "AZ"), 'lon'] = -114.474120

    data.loc[(data['city'] == "Grand Prarie") & (data['state'] == "TX"), 'lat'] = 32.745964
    data.loc[(data['city'] == "Grand Prarie") & (data['state'] == "TX"), 'lon'] = -96.997785

    data.loc[(data['city'] == "Corning") & (data['state'] == "WI"), 'lat'] = 45.261851
    data.loc[(data['city'] == "Corning") & (data['state'] == "WI"), 'lon'] = -89.962337

    data.loc[(data['city'] == "Barona Indian Reservation") & (data['state'] == "CA"), 'lat'] = 32.946258
    data.loc[(data['city'] == "Barona Indian Reservation") & (data['state'] == "CA"), 'lon'] = -116.861586

    data.loc[(data['city'] == "Lower Mount Bethel") & (data['state'] == "PA"), 'lat'] = 40.807747
    data.loc[(data['city'] == "Lower Mount Bethel") & (data['state'] == "PA"), 'lon'] = -75.166212

    data.loc[(data['city'] == "Franklin") & (data['state'] == "TN"), 'lat'] = 35.925064
    data.loc[(data['city'] == "Franklin") & (data['state'] == "TN"), 'lon'] = -86.868890

    data.loc[(data['city'] == "Crescent City") & (data['state'] == "FL"), 'lat'] = 29.430251
    data.loc[(data['city'] == "Crescent City") & (data['state'] == "FL"), 'lon'] = -81.510629

    data.loc[(data['city'] == "North Branch") & (data['state'] == "MN"), 'lat'] = 45.510213
    data.loc[(data['city'] == "North Branch") & (data['state'] == "MN"), 'lon'] = -92.993105

    data.loc[(data['city'] == "Saginaw") & (data['state'] == "MI"), 'lat'] = 43.419470
    data.loc[(data['city'] == "Saginaw") & (data['state'] == "MI"), 'lon'] = -83.950807

    data.loc[(data['city'] == "Blue Summit") & (data['state'] == "MO"), 'lat'] = 39.088673
    data.loc[(data['city'] == "Blue Summit") & (data['state'] == "MO"), 'lon'] = -94.481243

    data.loc[(data['city'] == "Frederickstown") & (data['state'] == "WA"), 'lat'] = 39.365658
    data.loc[(data['city'] == "Frederickstown") & (data['state'] == "WA"), 'lon'] = -75.882690

    data.loc[(data['city'] == "Watagua") & (data['state'] == "TX"), 'lat'] = 32.857906
    data.loc[(data['city'] == "Watagua") & (data['state'] == "TX"), 'lon'] = -97.254737

    data.loc[(data['city'] == "Columbua") & (data['state'] == "IN"), 'lat'] = 39.201440
    data.loc[(data['city'] == "Columbua") & (data['state'] == "IN"), 'lon'] = -85.921380

    data.loc[(data['city'] == "Canton Township") & (data['state'] == "PA"), 'lat'] = 40.218128
    data.loc[(data['city'] == "Canton Township") & (data['state'] == "PA"), 'lon'] = -80.310168

    data.loc[(data['city'] == "Fort Smith") & (data['state'] == "OK"), 'lat'] = 35.385924
    data.loc[(data['city'] == "Fort Smith") & (data['state'] == "OK"), 'lon'] = -94.398548

    data.loc[(data['city'] == "Standing Rock Reservation") & (data['state'] == "ND"), 'lat'] = 45.750275
    data.loc[(data['city'] == "Standing Rock Reservation") & (data['state'] == "ND"), 'lon'] = -101.200415

    data.loc[(data['city'] == "Rudioso") & (data['state'] == "NM"), 'lat'] = 33.367252
    data.loc[(data['city'] == "Rudioso") & (data['state'] == "NM"), 'lon'] = -105.658848

    data.loc[(data['city'] == "300 block of State Line Road") & (data['state'] == "TN"), 'lat'] = 36.502580
    data.loc[(data['city'] == "300 block of State Line Road") & (data['state'] == "TN"), 'lon'] = -88.743449

    data.loc[(data['city'] == "Blackman Township") & (data['state'] == "MI"), 'lat'] = 42.279917
    data.loc[(data['city'] == "Blackman Township") & (data['state'] == "MI"), 'lon'] = -84.459270

    data.loc[(data['city'] == "Lone Rock") & (data['state'] == "AR"), 'lat'] = 36.180625
    data.loc[(data['city'] == "Lone Rock") & (data['state'] == "AR"), 'lon'] = -92.344602

    data.loc[(data['city'] == "Lower Macungie Township") & (data['state'] == "PA"), 'lat'] = 40.540989
    data.loc[(data['city'] == "Lower Macungie Township") & (data['state'] == "PA"), 'lon'] = -75.562604

    data.loc[(data['city'] == "Hackett") & (data['state'] == "AR"), 'lat'] = 35.190373
    data.loc[(data['city'] == "Hackett") & (data['state'] == "AR"), 'lon'] = -94.411049

    data.loc[(data['city'] == "Cottonwood") & (data['state'] == "AZ"), 'lat'] = 34.739188
    data.loc[(data['city'] == "Cottonwood") & (data['state'] == "AZ"), 'lon'] = -112.009879

    data.loc[(data['city'] == "Tiverton") & (data['state'] == "RI"), 'lat'] = 41.625921
    data.loc[(data['city'] == "Tiverton") & (data['state'] == "RI"), 'lon'] = -71.213423

    data.loc[(data['city'] == "Poway") & (data['state'] == "CA"), 'lat'] = 32.962823
    data.loc[(data['city'] == "Poway") & (data['state'] == "CA"), 'lon'] = -117.035865

    data.loc[(data['city'] == "Kenner") & (data['state'] == "LA"), 'lat'] = 29.994092
    data.loc[(data['city'] == "Kenner") & (data['state'] == "LA"), 'lon'] = -90.241743

    data.loc[(data['city'] == "Okmulgee County") & (data['state'] == "OK"), 'lat'] = 35.679587
    data.loc[(data['city'] == "Okmulgee County") & (data['state'] == "OK"), 'lon'] = -95.983258

    data.loc[(data['city'] == "Homestead") & (data['state'] == "FL"), 'lat'] = 25.468722
    data.loc[(data['city'] == "Homestead") & (data['state'] == "FL"), 'lon'] = -80.477557

    data.loc[(data['city'] == "Antioch") & (data['state'] == "TN"), 'lat'] = 36.059718
    data.loc[(data['city'] == "Antioch") & (data['state'] == "TN"), 'lon'] = -86.671595

    data.loc[(data['city'] == "Naples") & (data['state'] == "FL"), 'lat'] = 26.142036
    data.loc[(data['city'] == "Naples") & (data['state'] == "FL"), 'lon'] = -81.794810

    data.loc[(data['city'] == "Knox") & (data['state'] == "IN"), 'lat'] = 41.295875
    data.loc[(data['city'] == "Knox") & (data['state'] == "IN"), 'lon'] = -86.625014

    data.loc[(data['city'] == "Monroe") & (data['state'] == "NC"), 'lat'] = 34.985428
    data.loc[(data['city'] == "Monroe") & (data['state'] == "NC"), 'lon'] = -80.549511

    data.loc[(data['city'] == "North Shore") & (data['state'] == "HI"), 'lat'] = 21.561657
    data.loc[(data['city'] == "North Shore") & (data['state'] == "HI"), 'lon'] = -158.071598
    return


def fix_coordinates(data):
    """
    Fix coordinates that were geocoded incorrectly

    Args:
        data: Pandas DataFrame containing original data and lat/lon data
    Returns:
        None, but the original data is updated with fixed coordinates
    """
    # Fix incorrect coordinates
    data.loc[(data['city'] == "South Gate") & (data['state'] == "CA"), 'lat'] = 33.954737
    data.loc[(data['city'] == "South Gate") & (data['state'] == "CA"), 'lon'] = -118.212016

    data.loc[(data['city'] == "Westminister") & (data['state'] == "CO"), 'lat'] = 39.836653
    data.loc[(data['city'] == "Westminister") & (data['state'] == "CO"), 'lon'] = -105.037205

    data.loc[(data['city'] == "Sylvania Township") & (data['state'] == "OH"), 'lat'] = 41.689896
    data.loc[(data['city'] == "Sylvania Township") & (data['state'] == "OH"), 'lon'] = -83.741163

    data.loc[(data['city'] == "Colebrook Township") & (data['state'] == "OH"), 'lat'] = 41.535773
    data.loc[(data['city'] == "Colebrook Township") & (data['state'] == "OH"), 'lon'] = -80.762615

    data.loc[(data['city'] == "Nevada") & (data['state'] == "MO"), 'lat'] = 37.839205
    data.loc[(data['city'] == "Nevada") & (data['state'] == "MO"), 'lon'] = -94.354672

    data.loc[(data['city'] == "Big Bear") & (data['state'] == "MO"), 'lat'] = 36.556754
    data.loc[(data['city'] == "Big Bear") & (data['state'] == "MO"), 'lon'] = -93.271757

    data.loc[(data['city'] == "Buffalo") & (data['state'] == "MO"), 'lat'] = 37.643929
    data.loc[(data['city'] == "Buffalo") & (data['state'] == "MO"), 'lon'] = -93.092409

    data.loc[(data['city'] == "Aurora") & (data['state'] == "MO"), 'lat'] = 36.970891
    data.loc[(data['city'] == "Aurora") & (data['state'] == "MO"), 'lon'] = -93.717979

    data.loc[(data['city'] == "Lebanon") & (data['state'] == "MO"), 'lat'] = 37.680597
    data.loc[(data['city'] == "Lebanon") & (data['state'] == "MO"), 'lon'] = -92.663787

    data.loc[(data['city'] == "Vancouver") & (data['state'] == "WA"), 'lat'] = 45.635515
    data.loc[(data['city'] == "Vancouver") & (data['state'] == "WA"), 'lon'] = -122.557830

    data.loc[(data['city'] == "Ridgefield") & (data['state'] == "WA"), 'lat'] = 45.815695
    data.loc[(data['city'] == "Ridgefield") & (data['state'] == "WA"), 'lon'] = -122.702895

    data.loc[(data['city'] == "Des Moines") & (data['state'] == "WA"), 'lat'] = 47.401766
    data.loc[(data['city'] == "Des Moines") & (data['state'] == "WA"), 'lon'] = -122.324290

    data.loc[(data['city'] == "Rochester") & (data['state'] == "WA"), 'lat'] = 46.828064
    data.loc[(data['city'] == "Rochester") & (data['state'] == "WA"), 'lon'] = -123.075530

    data.loc[(data['city'] == "Beaver") & (data['state'] == "WA"), 'lat'] = 48.057425
    data.loc[(data['city'] == "Beaver") & (data['state'] == "WA"), 'lon'] = -124.347757

    data.loc[(data['city'] == "Frederickson") & (data['state'] == "WA"), 'lat'] = 47.096211
    data.loc[(data['city'] == "Frederickson") & (data['state'] == "WA"), 'lon'] = -122.358731

    data.loc[(data['city'] == "West Knox") & (data['state'] == "TN"), 'lat'] = 35.970360
    data.loc[(data['city'] == "West Knox") & (data['state'] == "TN"), 'lon'] = -83.955185

    data.loc[(data['city'] == "Washington Park") & (data['state'] == "IL"), 'lat'] = 38.635050
    data.loc[(data['city'] == "Washington Park") & (data['state'] == "IL"), 'lon'] = -90.092885

    data.loc[(data['city'] == "Forest Park") & (data['state'] == "IL"), 'lat'] = 41.879476
    data.loc[(data['city'] == "Forest Park") & (data['state'] == "IL"), 'lon'] = -87.813670

    data.loc[(data['city'] == "Stockton") & (data['state'] == "IL"), 'lat'] = 42.349736
    data.loc[(data['city'] == "Stockton") & (data['state'] == "IL"), 'lon'] = -90.006792

    data.loc[(data['city'] == "Lawndale") & (data['state'] == "IL"), 'lat'] = 40.218097
    data.loc[(data['city'] == "Lawndale") & (data['state'] == "IL"), 'lon'] = -89.282592

    data.loc[(data['city'] == "Harvey") & (data['state'] == "IL"), 'lat'] = 41.610034
    data.loc[(data['city'] == "Harvey") & (data['state'] == "IL"), 'lon'] = -87.646713

    data.loc[(data['city'] == "Hurst") & (data['state'] == "IL"), 'lat'] = 37.833106
    data.loc[(data['city'] == "Hurst") & (data['state'] == "IL"), 'lon'] = -89.142857

    data.loc[(data['city'] == "Dalton") & (data['state'] == "IL"), 'lat'] = 41.638924
    data.loc[(data['city'] == "Dalton") & (data['state'] == "IL"), 'lon'] = -87.607268

    data.loc[(data['city'] == "Nokomis") & (data['state'] == "IL"), 'lat'] = 39.301157
    data.loc[(data['city'] == "Nokomis") & (data['state'] == "IL"), 'lon'] = -89.285085

    data.loc[(data['city'] == "Joilet") & (data['state'] == "IL"), 'lat'] = 41.525031
    data.loc[(data['city'] == "Joilet") & (data['state'] == "IL"), 'lon'] = -88.081725

    data.loc[(data['city'] == "Lansing") & (data['state'] == "IL"), 'lat'] = 41.564757
    data.loc[(data['city'] == "Lansing") & (data['state'] == "IL"), 'lon'] = -87.538931

    data.loc[(data['city'] == "Arcola") & (data['state'] == "IL"), 'lat'] = 39.684755
    data.loc[(data['city'] == "Arcola") & (data['state'] == "IL"), 'lon'] = -88.306437

    data.loc[(data['city'] == "Homer") & (data['state'] == "LA"), 'lat'] = 32.791813
    data.loc[(data['city'] == "Homer") & (data['state'] == "LA"), 'lon'] = -93.055718

    data.loc[(data['city'] == "Converse") & (data['state'] == "LA"), 'lat'] = 31.781558
    data.loc[(data['city'] == "Converse") & (data['state'] == "LA"), 'lon'] = -93.693794

    data.loc[(data['city'] == "Crowley") & (data['state'] == "LA"), 'lat'] = 30.214093
    data.loc[(data['city'] == "Crowley") & (data['state'] == "LA"), 'lon'] = -92.374576

    data.loc[(data['city'] == "Harvey") & (data['state'] == "LA"), 'lat'] = 29.903539
    data.loc[(data['city'] == "Harvey") & (data['state'] == "LA"), 'lon'] = -90.077294

    data.loc[(data['city'] == "Cade") & (data['state'] == "LA"), 'lat'] = 30.088707
    data.loc[(data['city'] == "Cade") & (data['state'] == "LA"), 'lon'] = -91.906276

    data.loc[(data['city'] == "Bernice") & (data['state'] == "LA"), 'lat'] = 32.822088
    data.loc[(data['city'] == "Bernice") & (data['state'] == "LA"), 'lon'] = -92.657930

    data.loc[(data['city'] == "Monroe") & (data['state'] == "LA"), 'lat'] = 32.509311
    data.loc[(data['city'] == "Monroe") & (data['state'] == "LA"), 'lon'] = -92.119301

    data.loc[(data['city'] == "Franklin") & (data['state'] == "LA"), 'lat'] = 29.796040
    data.loc[(data['city'] == "Franklin") & (data['state'] == "LA"), 'lon'] = -91.501500

    data.loc[(data['city'] == "Pride") & (data['state'] == "LA"), 'lat'] = 30.693796
    data.loc[(data['city'] == "Pride") & (data['state'] == "LA"), 'lon'] = -90.978159

    data.loc[(data['city'] == "Gibson") & (data['state'] == "LA"), 'lat'] = 29.686876
    data.loc[(data['city'] == "Gibson") & (data['state'] == "LA"), 'lon'] = -90.990653

    data.loc[(data['city'] == "Covington") & (data['state'] == "LA"), 'lat'] = 30.475470
    data.loc[(data['city'] == "Covington") & (data['state'] == "LA"), 'lon'] = -90.100911

    data.loc[(data['city'] == "Raceland") & (data['state'] == "LA"), 'lat'] = 29.727433
    data.loc[(data['city'] == "Raceland") & (data['state'] == "LA"), 'lon'] = -90.598976

    data.loc[(data['city'] == "Slidell") & (data['state'] == "LA"), 'lat'] = 30.275195
    data.loc[(data['city'] == "Slidell") & (data['state'] == "LA"), 'lon'] = -89.781175

    data.loc[(data['city'] == "Alexandria") & (data['state'] == "LA"), 'lat'] = 31.311294
    data.loc[(data['city'] == "Alexandria") & (data['state'] == "LA"), 'lon'] = -92.445137

    data.loc[(data['city'] == "Lakes Charles") & (data['state'] == "LA"), 'lat'] = 30.226595
    data.loc[(data['city'] == "Lakes Charles") & (data['state'] == "LA"), 'lon'] = -93.217376

    data.loc[(data['city'] == "Gretna") & (data['state'] == "LA"), 'lat'] = 29.914649
    data.loc[(data['city'] == "Gretna") & (data['state'] == "LA"), 'lon'] = -90.053960

    data.loc[(data['city'] == "Winnsboro") & (data['state'] == "LA"), 'lat'] = 32.163208
    data.loc[(data['city'] == "Winnsboro") & (data['state'] == "LA"), 'lon'] = -91.720681

    data.loc[(data['city'] == "Killeen") & (data['state'] == "AL"), 'lat'] = 34.862864
    data.loc[(data['city'] == "Killeen") & (data['state'] == "AL"), 'lon'] = -87.537525

    data.loc[(data['city'] == "Boonville") & (data['state'] == "IN"), 'lat'] = 38.049213
    data.loc[(data['city'] == "Boonville") & (data['state'] == "IN"), 'lon'] = -87.274172

    data.loc[(data['city'] == "Geneva") & (data['state'] == "WI"), 'lat'] = 42.638605
    data.loc[(data['city'] == "Geneva") & (data['state'] == "WI"), 'lon'] = -88.459767

    data.loc[(data['city'] == "Algoma Township") & (data['state'] == "MI"), 'lat'] = 43.149293
    data.loc[(data['city'] == "Algoma Township") & (data['state'] == "MI"), 'lon'] = -85.622930

    data.loc[(data['city'] == "Cato Township") & (data['state'] == "MI"), 'lat'] = 43.443107
    data.loc[(data['city'] == "Cato Township") & (data['state'] == "MI"), 'lon'] = -85.251548

    data.loc[(data['city'] == "Columbia Township") & (data['state'] == "MI"), 'lat'] = 42.114211
    data.loc[(data['city'] == "Columbia Township") & (data['state'] == "MI"), 'lon'] = -84.291076

    data.loc[(data['city'] == "Union Township") & (data['state'] == "MI"), 'lat'] = 43.587807
    data.loc[(data['city'] == "Union Township") & (data['state'] == "MI"), 'lon'] = -84.825510

    data.loc[(data['city'] == "Holland Township") & (data['state'] == "MI"), 'lat'] = 42.812810
    data.loc[(data['city'] == "Holland Township") & (data['state'] == "MI"), 'lon'] = -86.088390

    data.loc[(data['city'] == "Manila") & (data['state'] == "AR"), 'lat'] = 35.880073
    data.loc[(data['city'] == "Manila") & (data['state'] == "AR"), 'lon'] = -90.167039

    data.loc[(data['city'] == "Sims") & (data['state'] == "AR"), 'lat'] = 34.659264
    data.loc[(data['city'] == "Sims") & (data['state'] == "AR"), 'lon'] = -93.691029

    data.loc[(data['city'] == "Little Rock") & (data['state'] == "AR"), 'lat'] = 34.746481
    data.loc[(data['city'] == "Little Rock") & (data['state'] == "AR"), 'lon'] = -92.289595

    data.loc[(data['city'] == "Sheridan") & (data['state'] == "AR"), 'lat'] = 34.307041
    data.loc[(data['city'] == "Sheridan") & (data['state'] == "AR"), 'lon'] = -92.401265

    data.loc[(data['city'] == "Benton") & (data['state'] == "AR"), 'lat'] = 34.564537
    data.loc[(data['city'] == "Benton") & (data['state'] == "AR"), 'lon'] = -92.586828

    data.loc[(data['city'] == "Farmington") & (data['state'] == "AR"), 'lat'] = 36.042025
    data.loc[(data['city'] == "Farmington") & (data['state'] == "AR"), 'lon'] = -94.247151

    data.loc[(data['city'] == "Austin") & (data['state'] == "AR"), 'lat'] = 34.998421
    data.loc[(data['city'] == "Austin") & (data['state'] == "AR"), 'lon'] = -91.983755

    data.loc[(data['city'] == "Romance") & (data['state'] == "AR"), 'lat'] = 35.240713
    data.loc[(data['city'] == "Romance") & (data['state'] == "AR"), 'lon'] = -92.051904

    data.loc[(data['city'] == "Marion") & (data['state'] == "AR"), 'lat'] = 35.214534
    data.loc[(data['city'] == "Marion") & (data['state'] == "AR"), 'lon'] = -90.196483

    data.loc[(data['city'] == "Clarksville") & (data['state'] == "AR"), 'lat'] = 35.471472
    data.loc[(data['city'] == "Clarksville") & (data['state'] == "AR"), 'lon'] = -93.466573

    data.loc[(data['city'] == "Ozark") & (data['state'] == "AR"), 'lat'] = 35.487029
    data.loc[(data['city'] == "Ozark") & (data['state'] == "AR"), 'lon'] = -93.827697

    data.loc[(data['city'] == "Pine Bluff") & (data['state'] == "AR"), 'lat'] = 34.228431
    data.loc[(data['city'] == "Pine Bluff") & (data['state'] == "AR"), 'lon'] = -92.003196

    data.loc[(data['city'] == "Mulberry") & (data['state'] == "AR"), 'lat'] = 35.500642
    data.loc[(data['city'] == "Mulberry") & (data['state'] == "AR"), 'lon'] = -94.051592

    data.loc[(data['city'] == "Cabot") & (data['state'] == "AR"), 'lat'] = 34.974532
    data.loc[(data['city'] == "Cabot") & (data['state'] == "AR"), 'lon'] = -92.016534

    data.loc[(data['city'] == "Jonesboro") & (data['state'] == "AR"), 'lat'] = 35.842297
    data.loc[(data['city'] == "Jonesboro") & (data['state'] == "AR"), 'lon'] = -90.704279

    data.loc[(data['city'] == "Perryville") & (data['state'] == "AR"), 'lat'] = 35.004810
    data.loc[(data['city'] == "Perryville") & (data['state'] == "AR"), 'lon'] = -92.802667

    data.loc[(data['city'] == "Dover") & (data['state'] == "AR"), 'lat'] = 35.401471
    data.loc[(data['city'] == "Dover") & (data['state'] == "AR"), 'lon'] = -93.114341

    data.loc[(data['city'] == "Mena") & (data['state'] == "AR"), 'lat'] = 34.586217
    data.loc[(data['city'] == "Mena") & (data['state'] == "AR"), 'lon'] = -94.239655

    data.loc[(data['city'] == "Russellville") & (data['state'] == "AR"), 'lat'] = 35.278417
    data.loc[(data['city'] == "Russellville") & (data['state'] == "AR"), 'lon'] = -93.133786
    return


def serialize_data(data):
    """
    Serialize data to pickle file for easy loading

    Args:
        data: Pandas dataframe to be saved
    Returns:
        None
    """
    pd.to_pickle(data, "fatal-police-shootings-data-coordinates.pkl")


def load_data():
    """
    Load in previously serialized data

    Args:
        None
    Returns:
        Pandas dataframe containing original data plus latitude/longitude data
    """
    data = pd.read_pickle("fatal-police-shootings-data-coordinates.pkl")
    return data
