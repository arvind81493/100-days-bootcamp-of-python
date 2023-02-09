travel_log=[
{
    "country":"france",
    "cities_visited":["paris","lille","dijon"],
    "total_visited":12
},
{
    "country":"germany",
    "cities_visited":["berlin","hamburg","stuttgart"],
    "tota_visiters":12

},
] 
def add_new_country(country_visited,times_visited,cities_visited):
   new_country={}
   new_country["country"]=country_visited
   new_country["country"]=times_visited
   new_country["country"]=cities_visited
   travel_log.append(new_country)

add_new_country("Russia",2,["moscow","saint petersburg"])
print(travel_log)
      
       
