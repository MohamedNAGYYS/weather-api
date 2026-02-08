# Weather API

**Project URL:** [https://github.com/MohamedNAGYYS/weather-api](https://github.com/MohamedNAGYYS/weather-api)

A Django REST Framework project that allows logged-in users to get current weather information for a city.  
Weather data is fetched from the OpenWeatherMap API and saved in the database for each user.

---

## Features

- User authentication required
- Fetch weather for any city
- Save weather queries in the database
- Cache responses for 5 minutes to reduce API calls
- Includes temperature, description, humidity, pressure, wind speed, and country

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MohamedNAGYYS/weather-api.git
cd weather-api
