import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def get_scrape_web_data(TropicalCyclone, ForecastTrack, TrackHistory, db):
    URL = 'http://rammb.cira.colostate.edu/products/tc_realtime/index.asp'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    # places
    places_list = [element.text for element in soup.find_all("h3")]

    # description text
    description_text_list = [element.text for element in soup.find_all("a", {"href": True})]
    
    formatted_description_text_list = []
    for i, description_text in enumerate(description_text_list):
        if i > 6 and description_text is not None:
            if "AL" in description_text or "EP" in description_text or "WP" in description_text or "CP" in description_text or "NIO" in description_text or "SH" in description_text:
                new_description_text = re.sub('\s+', ' ', description_text).strip()
                formatted_description_text_list.append(new_description_text)
    
    # description id
    description_id_list = []
    if formatted_description_text_list:
        for formatted_description_text in formatted_description_text_list:
            description_id = formatted_description_text[:8].strip()
            description_id_list.append(description_id)

    # images
    images_list = [element for element in soup.find_all("img", {"src": True})]

    formatted_images_list = []
    for i, images in enumerate(images_list):
        if i > 2:
            image_src = 'https://rammb-data.cira.colostate.edu/' + images['src']
            formatted_images_list.append(image_src)

    # combined_list
    if places_list and formatted_description_text_list and description_id_list and formatted_images_list:
        combined_list = [list(e) for e in zip(places_list, formatted_description_text_list, description_id_list, formatted_images_list)]
        for item in combined_list:
            place = item[0]
            description_text = item[1]
            description_id = item[2]
            image = item[3]
            now = datetime.now()

            # add record to db
            existing_tropical_cyclone = TropicalCyclone.query.filter_by(description_id=description_id).first()
            if existing_tropical_cyclone is None:
                tropical_cyclone = TropicalCyclone(place, description_id, description_text, image, now, now)
                db.session.add(tropical_cyclone)
                db.session.commit()
    
    # forecast_track table, track_history table
    if description_id_list:
        for description_id in description_id_list:
            URL = 'https://rammb-data.cira.colostate.edu/tc_realtime/storm.asp?storm_identifier={}'.format(description_id)
            page = requests.get(URL)
            
            soup = BeautifulSoup(page.content, 'html.parser')
            
            table = soup.find_all('table')
            if table and len(table) == 2:
                forecast_track_table = table[0]
                rows = forecast_track_table.find_all('tr')
                for i, row in enumerate(rows):
                    if i > 0:
                        cols = row.find_all('td')
                        cols = [e.text.strip() for e in cols]

                        forecast_hour = cols[0]
                        latitude = float(cols[1])
                        longitude = float(cols[2])
                        intensity = cols[3]
                        now = datetime.now()

                        forecast_track = ForecastTrack(description_id, forecast_hour, latitude, longitude, intensity, now, now)
                        db.session.add(forecast_track)
                        db.session.commit()

                track_history_table = table[1]
                rows = track_history_table.find_all('tr')
                for i, row in enumerate(rows):
                    if i > 0:
                        cols = row.find_all('td')
                        cols = [e.text.strip() for e in cols]
                        
                        synoptic_time = cols[0]
                        latitude = float(cols[1])
                        longitude = float(cols[2])
                        intensity = cols[3]
                        now = datetime.now()

                        track_history = TrackHistory(description_id, synoptic_time, latitude, longitude, intensity, now, now)
                        db.session.add(track_history)
                        db.session.commit()