"""Define the api application."""

from flask import Blueprint, jsonify, request

from core.services.weather_service import WeatherService

urls_blueprint = Blueprint("api_urls", __name__)


@urls_blueprint.route("/", methods=["GET"])
def home_default():
    """Define a test page to check the webservice is up and running at root url."""
    return "Page par defaut", 200


@urls_blueprint.route("/weather-app-api/api/v0.0.1a", methods=["GET"])
def home():
    """Define a test page to check the webservice is up and running at ws url."""
    return (
        "Welcome to this weather forecast application.",
        200,
    )


@urls_blueprint.route(
    "/weather-app-api/api/v0.0.1a/get-weather", methods=["POST"]
)
def get_weather():
    """Define the method to set an email as a spam or a ham."""
    payload = request.get_json(force=True)

    if "town" not in payload.keys():
        result = {"status": "ko", "message": "The town must be indicated !"}
        return jsonify(result), 200

    if "country" not in payload.keys():
        result = {"status": "ko", "message": "The country must be indicated !"}
        return jsonify(result), 200

    weather_service = WeatherService()
    payload_response = weather_service.get_forecast(
        **{
            "location": "",
            "town": payload["town"],
            "country": payload["country"],
            "week": False,
        }
    )

    return jsonify(payload_response), 200
