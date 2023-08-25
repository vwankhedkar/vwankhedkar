import pytest
import time

class EventManager:
    def __init__(self):
        self.channels = {}

    def register_channel(self, channel_name):
        self.channels[channel_name] = []

    def subscribe(self, channel_name, listener):
        self.channels[channel_name].append(listener)

    def publish(self, channel_name, data):
        for listener in self.channels.get(channel_name, []):
            listener(data)

@pytest.fixture
def event_manager():
    return EventManager()

@pytest.fixture
def sensor():
    class Sensor:
        def __init__(self, name):
            self.name = name
            self.value = None

        def set_value(self, value):
            self.value = value

    return Sensor

@pytest.fixture
def triggered_events():
    return []

def test_snow_sensor_event(event_manager, sensor, triggered_events):
    snow_sensor = sensor("snow")
    event_manager.register_channel("snow_channel")
    event_manager.subscribe("snow_channel", lambda value: triggered_events.append(f"Snow Event: {value}"))

    snow_sensor.set_value(5)
    event_manager.publish("snow_channel", snow_sensor.value)

    assert "Snow Event: 5" in triggered_events

def test_wind_sensor_event(event_manager, sensor, triggered_events):
    wind_sensor = sensor("wind")
    event_manager.register_channel("wind_channel")
    event_manager.subscribe("wind_channel", lambda value: triggered_events.append(f"Wind Event: {value}"))

    wind_sensor.set_value(20)
    event_manager.publish("wind_channel", wind_sensor.value)

    assert "Wind Event: 20" in triggered_events

def test_flood_sensor_event(event_manager, sensor, triggered_events):
    flood_sensor = sensor("flood")
    event_manager.register_channel("flood_channel")
    event_manager.subscribe("flood_channel", lambda value: triggered_events.append(f"Flood Event: {value}"))

    flood_sensor.set_value(2.5)
    event_manager.publish("flood_channel", flood_sensor.value)

    assert "Flood Event: 2.5" in triggered_events

if __name__ == "__main__":
    pytest.main()

OUTPUT:
------
PS D:\ZC4\tests> pytest -v -s .\test_eventManager.py
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0 -- C:\Users\Vaishali\AppData\Local\Programs\Python\Python311\python.exe
cachedir: .pytest_cache
rootdir: D:\ZC4\tests
collected 3 items

test_eventManager.py::test_snow_sensor_event PASSED
test_eventManager.py::test_wind_sensor_event PASSED
test_eventManager.py::test_flood_sensor_event PASSED
================================================================ 3 passed in 0.04s ================================================================ 
PS D:\ZC4\tests>                           
