import requests
import json
import argparse
import webbrowser
parser = argparse.ArgumentParser('GeoLocator', description='Gives location info from an IP address')
parser.add_argument('address', nargs='?', default='')
args = parser.parse_args()
ip = args.address
c = requests.get(f"https://ipinfo.io/{ip}/json")
if c.status_code == 200:
    js = json.loads(c.content)
    print(f"City: {js['city']}")
    print(f"Region: {js['region']}")
    print(f"Country: {js['country']}")
    print(f"Location: {js['loc']}")
    print(f"Timezone: {js['timezone']}")
    print(f"ASN: {js['org']}")
    print(f"Maps: https://google.com/maps/?q={js['loc']}")
