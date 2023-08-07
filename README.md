# apod-api-NASA--1-
#APOD: Astronomy Picture of the Day using NASA's API downloaded from NASA website https://github.com/nasa/apod-api (I have made some modifications for completing the project)
This web application retrieves and displays the Astronomy Picture of the Day (APOD) using data from NASA's API. To enable this functionality, an API key from NASA has been obtained and integrated into the application.

Tools
Python
HTML
CSS
MongoDB
Flask
Instructions
This project is organized into two main parts:

Scraping (contained in the file apod_object_parser.py)
MongoDB and Flask Application (apod_spp2.py)
Part 1: Scraping
The application employs tools like , BeautifulSoup, Python, and Requests/Splinter for data scraping.

A file named apod_object_parser.py conducts all the necessary scraping and analysis tasks.
NASA APOD Data
The latest Astronomy Picture of the Day and its relevant information are collected from NASA's APOD Website.
Part 2: MongoDB and Flask Application
The project utilizes MongoDB along with Flask templating to create dynamic HTML pages that showcase the retrieved APOD data.

The Python script apod_spp2.py includes a function named scrape(). This function executes the scraping code from the Jupyter notebook and returns a Python dictionary containing the scraped data.

A Flask route /scrape imports the apod_spp2.py script and invokes the scrape() function. The returned data is stored as a Python dictionary in the MongoDB database.

The index route / queries the MongoDB database and transfers the APOD data to an HTML template for rendering.

The template HTML file index.html processes the APOD data dictionary and displays it within the appropriate HTML elements.

This comprehensive project not only provides a visually appealing representation of the Astronomy Picture of the Day but also demonstrates the integration of various technologies to create an engaging and informative web application. The utilization of NASA's APOD API further enriches the content and keeps users updated with captivating images and information about our universe.


#We want to assure you that your data privacy is of utmost importance to us. Just as the Apache License governs the terms and conditions for the use, reproduction, and distribution of software, we have taken similar care in handling your data. We have followed the principles of transparency and accountability, ensuring that your information is used responsibly and securely. Just as the License grants specific permissions and limitations, we have maintained clear guidelines for data usage, protecting your rights and interests. Our commitment to data privacy aligns with the ethos of the Apache License, and we uphold these standards in every aspect of our operations. Your trust is valuable to us, and we're dedicated to upholding the highest standards in safeguarding your data, as exemplified in the License's provisions.

