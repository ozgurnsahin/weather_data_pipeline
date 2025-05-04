CREATE TABLE weather_data IF NOT EXISTS(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    temperature DECIMAL(4,1) NOT NULL,
    feels_like DECIMAL(4,1) NOT NULL,
    humidity DECIMAL(4,1) NOT NULL,
    precipitation DECIMAL(3,1) NOT NULL,
    wind_speed DECIMAL(4,1) NOT NULL
);