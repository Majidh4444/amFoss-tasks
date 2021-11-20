import argparse
import requests
from urllib.request import urlopen
from PIL import Image

my_parser = argparse.ArgumentParser()
my_parser.add_argument('--date', action='store', type=str, required=True)
my_parser.add_argument('--id', action='store', type=int, required=True)
args = my_parser.parse_args()

url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date="+args.date+"&api_key=kSbUjJPHIhaj5C1wZyuzaLs2zZj9psVOGxzTcTZs"
source = requests.get(url).json()

selectedObject = source["photos"]
obj = [x for x in selectedObject if x["id"]==args.id]
img = Image.open(urlopen(obj[0]["img_src"]))
img.show()