# weather-reporting-system-using-iot

To create a README file for your GitHub repository, you can provide a brief overview of your project along with instructions on how to set it up and use it. Here's a simple template you can use:

---

# Weather Monitoring System

This project is a weather monitoring system built using Arduino and ESP8266. It reads data from DHT11 sensor for temperature and humidity, and from a rain sensor for rainfall. The data is then sent to a server for storage and analysis. The system also triggers alerts for extreme weather conditions.

## Hardware Requirements
- Arduino board
- DHT11 temperature and humidity sensor
- Rain sensor
- ESP8266 module
- Wi-Fi module

## Software Requirements
- Arduino IDE
- Libraries: Wire, DHT, Adafruit_Sensor, WiFi, HTTPClient

## Setup
1. Connect the DHT11 sensor and rain sensor to the Arduino board following the circuit diagram.
2. Install the required libraries in your Arduino IDE.
3. Update the Wi-Fi credentials (`WIFI_SSID` and `WIFI_PASSWORD`) and server URL (`SERVER_URL`) in the code.
4. Upload the code to your Arduino board.
5. Set up the server to receive weather data and alerts.

## Usage
- Once the system is set up, it will start monitoring weather conditions.
- Data will be reported to the server periodically.
- Alerts will be triggered for extreme weather conditions.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.



##circuit diagram
      +5V                  +5V                  +5V
       |                    |                    |
       R1                   R2                   R3
       |                    |                    |
       +-----------+        +-----------+        +-----------+
       |           |        |           |        |           |
       |       DHT11 Sensor      ESP8266     Rain Sensor   |
       |           |        |           |        |           |
       +-----------+        +-----------+        +-----------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       +-----------+        +-----------+        +-----------+
       |           |        |           |        |           |
       |     SDA   |--------|     SDA   |--------|           |
       |           |        |           |        |           |
       |           |        |           |        |           |
       +-----------+        +-----------+        +-----------+
       |           |        |           |        |           |
       |     SCL   |--------|     SCL   |--------|           |
       |           |        |           |        |           |
       +-----------+        +-----------+        +-----------+
       |                    |                    |
      GND                  GND                  GND
