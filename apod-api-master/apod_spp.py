from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# Replace 'YOUR_NASA_API_KEY' with your actual NASA API key
NASA_API_KEY = '1LBk0d7kU2OClCH2f9zSjfgZZkqhmosGvqdgkesH'

def get_apod_data():
    url = f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/')
def index():
    apod_data = get_apod_data()
    
    template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>APOD - Astronomy Picture of the Day</title>
    </head>
    <body>
        <h1>Astronomy Picture of the Day</h1>
        <img src="{{ apod_data.url }}" alt="APOD">
        <p>{{ apod_data.title }}</p>
        <p>{{ apod_data.explanation }}</p>
    </body>
    </html>
    """
    
    return render_template_string(template, apod_data=apod_data)

if __name__ == '__main__':
    app.run(debug=True)


