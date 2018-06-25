import requests

running = True

def LatLong():
    session = requests.Session()
    response = session.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    response = response.json()
    return [response["iss_position"]['latitude'], response['iss_position']['longitude']]

print("press CTRL+C to exit")
while running:
    try:
        position = LatLong()
    except:
        print("\rExited Program", end="")
        exit()
    print("\nCurrent ISS Position")
    print("Latitude: ", end = "")
    print(position[0])
    print("Longitude: ", end="")
    print(position[1], end="")
    print("\033[3A\r", end="")
