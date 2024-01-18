#!usr/bin/env python 3

import requests

URL = "http://api.open-notify.org/iss-now.json"

def main():
    response= requests.get(URL).json()

    long= response["iss_position"]["longitude"]
    lat= response["iss_position"]["latitude"]
        
    print (f"""Current location of ISS: \n
            Lon: {long} \n
            Lat: {lat}
           """)

if __name__ == "__main__":
    main()
