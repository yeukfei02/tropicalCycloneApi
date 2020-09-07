import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

def get_scrape_web_data(TropicalCyclone, db):
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

    # images
    images_list = [element for element in soup.find_all("img", {"src": True})]

    formatted_images_list = []
    for i, images in enumerate(images_list):
        if i > 2:
            image_src = 'https://rammb-data.cira.colostate.edu/' + images['src']
            formatted_images_list.append(image_src)

    # combined_list
    if places_list and formatted_description_text_list and formatted_images_list:
        combined_list = [list(e) for e in zip(places_list, formatted_description_text_list, formatted_images_list)]
        for item in combined_list:
            place = item[0]
            description_text = item[1]
            image = item[2]
            now = datetime.now()

            # add record to db
            existing_tropical_cyclone = TropicalCyclone.query.filter_by(description_text=description_text).first()
            if existing_tropical_cyclone is None:
                tropical_cyclone = TropicalCyclone(place, description_text, image, now, now)
                db.session.add(tropical_cyclone)
                db.session.commit()