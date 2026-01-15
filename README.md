# Weather API

A Django-based REST API that provides current weather information for cities worldwide using the WeatherAPI service.

## Features

- **Real-time Weather Data**: Get current weather conditions including temperature, humidity, wind speed, and more
- **Air Quality Index (AQI)**: Optional air quality information for supported locations
- **RESTful API**: Clean, simple REST endpoints
- **Error Handling**: Comprehensive error handling with appropriate HTTP status codes
- **Logging**: Built-in logging for debugging and monitoring
- **Environment Configuration**: Secure API key management using environment variables

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- A WeatherAPI account and API key (get one at [weatherapi.com](https://www.weatherapi.com/))

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd weather_api
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file:**
   Create a `.env` file in the project root with the following variables:
   ```
   DJANGO_SECRET_KEY=your-secret-key-here
   DEBUG=True
   WEATHER_API_KEY=your-weatherapi-key-here
   ```

5. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## API Usage

### Base URL
```
http://127.0.0.1:8000/api/
```

### Endpoints

#### GET /api/weather/

Get current weather data for a specific city.

**Parameters:**
- `city` (required): Name of the city (e.g., "London", "New York")
- `aqi` (optional): Include air quality index ("yes" or "no", default: "no")

**Example Request:**
```bash
curl "http://127.0.0.1:8000/api/weather/?city=London"
```

**Example Response:**
```json
{
  "location": {
    "name": "London",
    "region": "City of London, Greater London",
    "country": "United Kingdom",
    "lat": 51.52,
    "lon": -0.11,
    "tz_id": "Europe/London",
    "localtime_epoch": 1640995200,
    "localtime": "2022-01-01 12:00"
  },
  "current": {
    "last_updated_epoch": 1640995200,
    "last_updated": "2022-01-01 12:00",
    "temp_c": 5.0,
    "temp_f": 41.0,
    "is_day": 1,
    "condition": {
      "text": "Partly cloudy",
      "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
      "code": 1003
    },
    "wind_mph": 8.1,
    "wind_kph": 13.0,
    "wind_degree": 230,
    "wind_dir": "SW",
    "pressure_mb": 1015.0,
    "pressure_in": 29.97,
    "precip_mm": 0.0,
    "precip_in": 0.0,
    "humidity": 81,
    "cloud": 75,
    "feelslike_c": 1.5,
    "feelslike_f": 34.7,
    "vis_km": 10.0,
    "vis_miles": 6.0,
    "uv": 1.0,
    "gust_mph": 12.1,
    "gust_kph": 19.4
  }
}
```

**With AQI:**
```bash
curl "http://127.0.0.1:8000/api/weather/?city=London&aqi=yes"
```

### Error Responses

- **400 Bad Request**: Missing required `city` parameter
- **504 Gateway Timeout**: Weather API request timed out
- **500 Internal Server Error**: Unexpected error occurred

**Error Response Format:**
```json
{
  "error": "Error message description"
}
```

## Configuration

### Environment Variables

- `DJANGO_SECRET_KEY`: Django secret key for security
- `DEBUG`: Set to `True` for development, `False` for production
- `WEATHER_API_KEY`: Your WeatherAPI key

### WeatherAPI

This project uses [WeatherAPI](https://www.weatherapi.com/) as the weather data provider. You need to:

1. Sign up for a free account
2. Get your API key from the dashboard
3. Add it to your `.env` file

WeatherAPI offers a free tier with 1,000,000 calls per month.

## Project Structure

```
weather_api/
├── core/                    # Django project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── weather/                 # Weather app
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   └── migrations/
├── DOC/                     # Documentation
│   └── index.html
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Dependencies

- **Django 6.0.1**: Web framework
- **requests 2.32.5**: HTTP library for API calls
- **python-dotenv 1.2.1**: Environment variable management
- Other dependencies as listed in `requirements.txt`

## Development

### Running Tests

```bash
python manage.py test
```

### Code Style

This project follows PEP 8 Python style guidelines.

### Logging

Logs are configured in Django's logging system. Check the console output or Django logs for debugging information.

## Deployment

For production deployment:

1. Set `DEBUG=False` in environment variables
2. Configure `ALLOWED_HOSTS` in settings
3. Use a production-grade database (PostgreSQL recommended)
4. Set up proper logging
5. Use a WSGI server like Gunicorn
6. Consider using Docker for containerization

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues or questions:
- Create an issue on GitHub
- Check the WeatherAPI documentation for API-related questions

## API Rate Limits

WeatherAPI has rate limits depending on your plan:
- Free: 1,000,000 calls/month
- Startup: 2,000,000 calls/month
- Developer: 5,000,000 calls/month
- Professional: 10,000,000 calls/month

Monitor your usage in the WeatherAPI dashboard.