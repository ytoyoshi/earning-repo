import googlemaps
from datetime import datetime

apikey = 'AIzaSyAxr8-uTwltTPZH6iwYH8rSRjKcbTJXu0E'
gmaps = googlemaps.Client(key=apikey)
geocode_result = gmaps.geocode('ブランドール川治')

ll = geocode_result[0]["geometry"]["location"]
print("Latitude : ",ll["lat"])
print("Longitude : ",ll["lng"])

