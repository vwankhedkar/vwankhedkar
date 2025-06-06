test_loggins.py

import logging
LOGGER = logging.getLogger(__name__)
def test_myloggings():
    LOGGER.info("Info logs")
    LOGGER.warning("Warning Logs")
    LOGGER.error("Error Logs")
    LOGGER.critical("Critical Logs")
    assert True

pytest.ini
[pytest]
markers =
    smoke: smoke tests
    sanity: sanity tests
    str
    strtest
# this cli for console log only
log_cli = 1
log_cli_level = ERROR
log_cli_format = %(message)s

log_file = log/pytesting.log
log_file_level = DEBUG
log_file_format = %(asctime)s [%(levelname)8s] %(message)s %(filenames)s:%(lineno)s)
log_file_date_format = %Y-%m-%d %H-%M-%S

(.venv) PS C:\Users\vwank\PycharmProjects\PytestFramework\AppPetsStoreTests\py_assertions> pytest -v -s
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.13.1, pytest-8.3.5, pluggy-1.5.0 -- C:\Trainings\RobotFramework\RobotFramework\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vwank\PycharmProjects\PytestFramework
configfile: pytest.ini
collected 1 item                                                                                                                                   

test_loggins.py::test_myloggings 
------------------------------------------------------------------ live log call ------------------------------------------------------------------ 
Error Logs
PASSED

================================================================ 1 passed in 0.02s ================================================================ 
(.venv) PS C:\Users\vwank\PycharmProjects\PytestFramework\AppPetsStoreTests\py_assertions> 
