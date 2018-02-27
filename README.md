### Frosty

Frosty is a simple tool. It sends an email with the low temperature as the subject and a chart of the next few hours of temperature data.

### Software Requirements

Frosty has been built and tested on Python 3.5.

The charting requires matplotlib and TK.
`sudo pip install matplotlib`
`sudo apt-get install python3-tk`

The email is sent via the python-emails library:
`sudo pip install python-emails`

### API(s)

The weather data is acquired via the [OpenWeatherMap](https://openweathermap.org/api) "5 day / 3 hour forecast" free API. You will need to setup an account, add your key to the config.py (see below), and find your [location id](http://bulk.openweathermap.org/sample/).

### Configuration

Copy config.template.py and name it config.py and fill in your values. You can use gmail (tested) or another smtp server for the email configuration (mailgun also tested).

### License

Frosty is freely available under the MIT license.
