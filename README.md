# ESP32 Web Server Project

This project creates a web server on ESP32 WROOM using Arduino, serving a structured website with:
- Main page
- Admin section
- Quest section
- Factions
- Herbarium
- Announcements
- Multimedia pages (user photo uploads)

## Features
- JSON-based data storage
- Modular HTML templates
- User-friendly navigation

## Getting Started
1. Flash `main.ino` to your ESP32.
2. Place `database.json` and HTML templates on SPIFFS or LittleFS.
3. Connect ESP32 to WiFi and access via browser.

## Requirements
- ESP32 WROOM
- Arduino IDE
- ArduinoJson library
- ESPAsyncWebServer library

## License
MIT


main.ino

database.json

templates/

README.md

ROADMAP.md