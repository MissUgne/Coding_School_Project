from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=f9217c96f6b17b9407ecb45285fd0009'
        response = requests.get(url.format(city)).json()

        weather = {
            'city': response['name'],
            'country': response['sys']['country'],
            'temp': str(int(response['main']['temp'])),
            'l_temp': str(int(response['main']['temp_min'])),
            'h_temp': str(int(response['main']['temp_max'])),
            'main': response['weather'][0]['main'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon']
        }

        return render_template('weather.html', weather=weather)

    return render_template('index.html')


@app.errorhandler(500)
def internal_error(error):
    return render_template('error_500.html')


if __name__ == '__main__':
    app.run(port=5001)
