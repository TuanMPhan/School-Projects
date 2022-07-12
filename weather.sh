#!/bin/sh

newark="https://forecast.weather.gov/MapClick.php?CityName=Newark&state=NJ"
princeton="https://forecast.weather.gov/MapClick.php?CityName=Princeton&state=NJ"
hoboken="https://forecast.weather.gov/MapClick.php?CityName=Hoboken&state=NJ"
trenton="https://forecast.weather.gov/MapClick.php?CityName=Trenton&state=NJ"
hackensack="https://forecast.weather.gov/MapClick.php?CityName=Hackensack&state=NJ"

wget $newark -O newark.html
wget $princeton -O princeton.html
wget $hoboken -O hoboken.html
wget $trenton -O trenton.html
wget $hackensack -O hackensack.html

java -jar tagsoup-1.2.1.jar --files newark.html
java -jar tagsoup-1.2.1.jar --files princeton.html
java -jar tagsoup-1.2.1.jar --files hoboken.html
java -jar tagsoup-1.2.1.jar --files trenton.html
java -jar tagsoup-1.2.1.jar --files hackensack.html

python3 parser.py

find . -name "*.html" | xargs rm
find . -name "*.xhtml" | xargs rm

