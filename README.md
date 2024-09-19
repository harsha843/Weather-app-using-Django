

# Weather App using Django

This is a simple weather application built using Django that fetches real-time weather data for a given city using the OpenWeatherMap API.

## Features

- Fetches current weather conditions for any city in the world.
- Displays temperature, weather conditions, wind speed, and other details.
- Easy-to-use interface with a search function.
- Responsive design for both mobile and desktop.
.
## Screenshots

![Home Page](path_to_image)  
*Weather results for a city*

## Prerequisites

To run this project locally, you'll need:

- Python 3.x
- Django 3.x or above
- An API key from [OpenWeatherMap](https://openweathermap.org/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/harsha843/Weather-app-using-Django.git
   ```

2. Navigate into the project directory:

   ```bash
   cd Weather-app-using-Django
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Obtain your OpenWeatherMap API key by signing up [here](https://openweathermap.org/).

5. In the project folder, create a `.env` file and add your API key:

   ```bash
   API_KEY=your_openweathermap_api_key
   ```

6. Apply migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Open your browser and go to `http://127.0.0.1:8000/` to use the app.

## Usage

1. Enter a city name in the search bar.
2. Press "Search" to view the current weather information for the selected city.

## Technologies Used

- Django
- HTML/CSS
- JavaScript
- OpenWeatherMap API

## Contributing

Feel free to open issues or submit pull requests. Contributions are always welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
