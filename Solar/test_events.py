import pytest

class Sensor:
    def __init__(self, initial_value):
        self.value = initial_value
        self.listeners = []

    def add_listener(self, listener):
        self.listeners.append(listener)

    def update_value(self, new_value):
        self.value = new_value
        for listener in self.listeners:
            listener(self.value)

class EventManager:
    def __init__(self):
        self.handlers = {}

    def register_handler(self, event, handler):
        if event not in self.handlers:
            self.handlers[event] = []
        self.handlers[event].append(handler)

    def trigger_event(self, event):
        if event in self.handlers:
            for handler in self.handlers[event]:
                handler()

@pytest.fixture
def sensor_values():
    return {
        "snow": Sensor(0),
        "wind": Sensor(0),
        "flood": Sensor(0)
    }

@pytest.fixture
def event_manager():
    return EventManager()

@pytest.fixture
def triggered_events():
    return []

def test_snow_sensor_event(event_manager, sensor_values, triggered_events):
    def snow_handler():
        triggered_events.append("Snow Event")

    event_manager.register_handler("snow_event", snow_handler)
    sensor_values["snow"].add_listener(lambda value: event_manager.trigger_event("snow_event"))

    sensor_values["snow"].update_value(5)

    assert "Snow Event" in triggered_events

def test_wind_sensor_event(event_manager, sensor_values, triggered_events):
    def wind_handler():
        triggered_events.append("Wind Event")

    event_manager.register_handler("wind_event", wind_handler)
    sensor_values["wind"].add_listener(lambda value: event_manager.trigger_event("wind_event"))

    sensor_values["wind"].update_value(20)

    assert "Wind Event" in triggered_events

def test_flood_sensor_event(event_manager, sensor_values, triggered_events):
    def flood_handler():
        triggered_events.append("Flood Event")

    event_manager.register_handler("flood_event", flood_handler)
    sensor_values["flood"].add_listener(lambda value: event_manager.trigger_event("flood_event"))

    sensor_values["flood"].update_value(2.5)

    assert "Flood Event" in triggered_events

if __name__ == "__main__":
    pytest.main()

OUTPUT:
-----
PS D:\ZC4\tests> pytest -v -s .\test_events1.py             
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.11.4, pytest-7.4.0, pluggy-1.2.0 -- C:\Users\Vaishali\AppData\Local\Programs\Python\Python311\python.exe
cachedir: .pytest_cache
rootdir: D:\ZC4\tests
collected 3 items                                                                                                                                   

test_events1.py::test_snow_sensor_event PASSED
test_events1.py::test_wind_sensor_event PASSED
test_events1.py::test_flood_sensor_event PASSED

================================================================ 3 passed in 0.02s ================================================================ 
PS D:\ZC4\tests> 
