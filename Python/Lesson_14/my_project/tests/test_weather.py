from my_project.weather import check_weather
import pytest

'''

# passed
def test_check_weather():
    assert check_weather(21.00) == 'hot', 'temperature greater then 20 degree must be consider as hot'


# failed
def test_check_weather2():
    assert check_weather(5.00) == 'average', 'temperature between 10 and 20 degree must be consider as average temperature'


# passed
def test_check_weather3():
    assert check_weather(5.00) == 'cold', 'temperature lower then 10 degree must be consider as cold'


# passed
def test_check_weather4():
    assert check_weather(13.00) == 'average', 'temperature between 10 and 20 degree must be consider as average temperature'

# failed because every def test_function() is consider a single test
def test_check_weather5():
    assert check_weather(30.00) == 'hot', 'temperature greater then 20 degree must be consider as hot'
    assert check_weather(11.00) == 'cold', 'temperature lower then 10 degree must be consider as cold'

'''

@pytest.mark.parametrize('temperature, expected', [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])

def test_check_weather(temperature, expected):
    assert check_weather(temperature) == expected