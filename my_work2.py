Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> import pwowm
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import pwowm
ImportError: No module named 'pwowm'
>>> import pyowm
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    import pyowm
ImportError: No module named 'pyowm'
>>> import pyowm
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import pyowm
ImportError: No module named 'pyowm'
>>> 
>>> i = 12
>>> while(i < 20):
	if i / 2 == 0:
		print(i)
		i = i + 1
	else: i = i + 1
        i = i + 1
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> i = 12
>>> while(i < 20):
	if i / 2 == 0:
		print(i)
		i = i + 1
	else: i = i + 1

	
>>> import pyowm
>>> 
>>> owm = pyowm.OWM('{23fff117d9b3bc82f1d973f919957ed4}')
>>> observation = owm.weather_at_place('Cape Coast,Ghana')
Traceback (most recent call last):
  File "/usr/local/lib/python3.5/dist-packages/pyowm/commons/weather_client.py", line 55, in _lookup_cache_or_invoke_API
    response = urlopen(API_full_url, None, timeout)
  File "/usr/lib/python3.5/urllib/request.py", line 163, in urlopen
    return opener.open(url, data, timeout)
  File "/usr/lib/python3.5/urllib/request.py", line 472, in open
    response = meth(req, response)
  File "/usr/lib/python3.5/urllib/request.py", line 582, in http_response
    'http', request, response, code, msg, hdrs)
  File "/usr/lib/python3.5/urllib/request.py", line 510, in error
    return self._call_chain(*args)
  File "/usr/lib/python3.5/urllib/request.py", line 444, in _call_chain
    result = func(*args)
  File "/usr/lib/python3.5/urllib/request.py", line 590, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 401: Unauthorized

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    observation = owm.weather_at_place('Cape Coast,Ghana')
  File "/usr/local/lib/python3.5/dist-packages/pyowm/webapi25/owm25.py", line 231, in weather_at_place
    'lang': self._language})
  File "/usr/local/lib/python3.5/dist-packages/pyowm/commons/weather_client.py", line 94, in call_API
    return self._lookup_cache_or_invoke_API(self._cache, url, timeout)
  File "/usr/local/lib/python3.5/dist-packages/pyowm/commons/weather_client.py", line 58, in _lookup_cache_or_invoke_API
    raise unauthorized_error.UnauthorizedError('Invalid API key')
pyowm.exceptions.unauthorized_error.UnauthorizedError: Your API subscription level does not allow to perform this operation
Reason: Invalid API key
>>> owm = pyowm.OWM('23fff117d9b3bc82f1d973f919957ed4')
>>> observation = owm.weather_at_place('Cape Coast,Ghana')
>>> w = observation.get_weather()
>>> w.get_wind()
{'deg': 262.5, 'speed': 1.81}
>>> w.get_humidity()
83
>>> w.get_temperature()
{'temp': 299.764, 'temp_min': 299.764, 'temp_max': 299.764, 'temp_kf': None}
>>> w.get_pressure()
{'press': 1016.57, 'sea_level': 1028.51}
>>> 
>>> owm = pyowm.OWM('23fff117d9b3bc82f1d973f919957ed4')
>>> observation = owm.weather_at_place('Hong Kong, China')
>>> w = observation.get_weather()
>>> w.get_wind()
{'deg': 190, 'speed': 4.6}
>>> w.get_humidity()
70
>>> w.get_relative_humidity()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    w.get_relative_humidity()
AttributeError: 'Weather' object has no attribute 'get_relative_humidity'
>>> dir(owm)
['OWM_API_VERSION', '_API_key', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__metaclass__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_api', '_assert_is_string', '_assert_is_string_or_unicode', '_encode_string', '_language', '_parsers', '_pollapi', '_retrieve_station_history', '_subscription_type', '_uvapi', 'city_id_registry', 'coindex_around_coords', 'daily_forecast', 'daily_forecast_at_coords', 'daily_forecast_at_id', 'get_API_key', 'get_API_version', 'get_language', 'get_subscription_type', 'get_version', 'is_API_online', 'no2index_around_coords', 'ozone_around_coords', 'set_API_key', 'set_language', 'so2index_around_coords', 'station_at_coords', 'station_day_history', 'station_hour_history', 'station_tick_history', 'stations_manager', 'three_hours_forecast', 'three_hours_forecast_at_coords', 'three_hours_forecast_at_id', 'uvindex_around_coords', 'weather_around_coords', 'weather_at_coords', 'weather_at_id', 'weather_at_ids', 'weather_at_place', 'weather_at_places', 'weather_at_station', 'weather_at_stations_in_bbox', 'weather_at_zip_code', 'weather_history_at_coords', 'weather_history_at_id', 'weather_history_at_place']
>>> dir(weather_at_place)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    dir(weather_at_place)
NameError: name 'weather_at_place' is not defined
>>> dir(owm.weather_at_place)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> dir(observation.get_weather)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__func__', '__ge__', '__get__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> 
>>> owm = pyowm.OWM('23fff117d9b3bc82f1d973f919957ed4')
>>> observation = owm.weather_at_place('Tokyo')
>>> w = observation.get_weather()
>>> w.get_wind()
{'deg': 220, 'gust': 8.2, 'speed': 5.7}
>>> w.get_air_pressure()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    w.get_air_pressure()
AttributeError: 'Weather' object has no attribute 'get_air_pressure'
>>> observation = owm.weather_at_place('Koforidua')
>>> w = observation.get_weather()
>>> w.get_windspeed()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    w.get_windspeed()
AttributeError: 'Weather' object has no attribute 'get_windspeed'
>>> w.get_wind()
{'deg': 250, 'speed': 4.1}
>>> observation = owm.language('Koforidua')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    observation = owm.language('Koforidua')
AttributeError: 'OWM25' object has no attribute 'language'
>>> w.get_language()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    w.get_language()
AttributeError: 'Weather' object has no attribute 'get_language'
>>> observation = owm.get_language('Koforidua')
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    observation = owm.get_language('Koforidua')
TypeError: get_language() takes 1 positional argument but 2 were given
>>> w.get_sunrise_time()
1530769907
>>> w.get_sunset_time()
1530814782
>>> while(i < 20):
    range(12,20,2)
    print(i)

    
>>> 
>>> i = 12
>>> while(i < 20):
	if i % 2 == 0:
		print(i)
		i = i + 1
	else: i = i + 1
        i = i + 1

SyntaxError: inconsistent use of tabs and spaces in indentation
>>> i = 12
>>> while(i < 20):
	if i % 2 == 0:
		print(i)
		i = i + 1
	else: i = i + 1

	
12
14
16
18
>>> 
>>> def evens():
    a = int(input("First value: "))
    b = int(input("Second value: "))
    while(a < b):
        if a % 2 == 0:
            print(a)
            a = a + 1
        else: a = a + 1

        
>>> evens()
First value: 3
Second value: 7
4
6
>>> evens()
First value: 1
Second value: 90
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> 
>>> dir(reverse)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    dir(reverse)
NameError: name 'reverse' is not defined
>>> 
>>> def evens():
    a = int(input("First value: "))
    b = int(input("Second value: "))
    while(a < b):
        if a % 2 == 0:
            print(a)[::-1]
            a = a + 1
        else: a = a + 1

        
>>> evens()
First value: 3
Second value: 90
4
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    evens()
  File "<pyshell#66>", line 6, in evens
    print(a)[::-1]
TypeError: 'NoneType' object is not subscriptable
>>> 
>>> def evens():
    a = int(input("First value: "))
    b = int(input("Second value: "))
    while(a < b):
        if a % 2 == 0:
            print(a)
            a = a + 1
        else: a = a + 1
        [::-1]
        
SyntaxError: invalid syntax
>>> 
>>> 
>>> def evens():
    a = int(input("First value: "))
    b = int(input("Second value: "))
    while(a < b):
        if a % 2 == 0:
            print(a)
            a = a + 1
        else: a = a + 1
        print(a[::-1])

        
>>> evens
<function evens at 0x7415f5d0>
>>> 
>>> def evens():
    a = int(input("First value: "))
    b = int(input("Second value: "))
    mylist = []
    while(a < b):
        if a % 2 == 0:
            mylist.append(a)
            a = a + 1
        else: a = a + 1
        print(mylist[::-1])

        
>>> evens()
First value: 3
Second value: 90
[]
[4]
[4]
[6, 4]
[6, 4]
[8, 6, 4]
[8, 6, 4]
[10, 8, 6, 4]
[10, 8, 6, 4]
[12, 10, 8, 6, 4]
[12, 10, 8, 6, 4]
[14, 12, 10, 8, 6, 4]
[14, 12, 10, 8, 6, 4]
[16, 14, 12, 10, 8, 6, 4]
[16, 14, 12, 10, 8, 6, 4]
[18, 16, 14, 12, 10, 8, 6, 4]
[18, 16, 14, 12, 10, 8, 6, 4]
[20, 18, 16, 14, 12, 10, 8, 6, 4]
[20, 18, 16, 14, 12, 10, 8, 6, 4]
[22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
[88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4]
>>> 
>>> 
>>> def evens():
    a = int(input("First value: "))
    b = int(input("Second value: "))
    mylist = []
    while(a < b):
        if a % 2 == 0:
            mylist.append(a)
            a = a + 1
        else: a = a + 1
    print(mylist[::-1])

    
>>> evens()
First value: 2
Second value: 90
[88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
>>> 
>>> for i in range(1,11):
    print(1)

    
1
1
1
1
1
1
1
1
1
1
>>> 
>>> for i in range(1,11):
    print(i)

    
1
2
3
4
5
6
7
8
9
10
>>> 
>>> for j in [1, 2, 3]:
	print j
	
SyntaxError: Missing parentheses in call to 'print'
>>> for j in [1, 2, 3]
SyntaxError: invalid syntax
>>> for j in [1, 2, 3]:
	print(j)

	
1
2
3
>>> for i in range(1,4):
	print(i)

	
1
2
3
>>> 
>>> mylist = []
>>> for i in range(0,19):
	if i % 2 == 0:
		mylist.apend(i)
		i = i + 1
	print(mylist)

	
Traceback (most recent call last):
  File "<pyshell#109>", line 3, in <module>
    mylist.apend(i)
AttributeError: 'list' object has no attribute 'apend'
>>> for i in range(0,19):
	if i % 2 == 0:
		mylist.append(i)
		i = i + 1
	print(mylist)

	
[0]
[0]
[0, 2]
[0, 2]
[0, 2, 4]
[0, 2, 4]
[0, 2, 4, 6]
[0, 2, 4, 6]
[0, 2, 4, 6, 8]
[0, 2, 4, 6, 8]
[0, 2, 4, 6, 8, 10]
[0, 2, 4, 6, 8, 10]
[0, 2, 4, 6, 8, 10, 12]
[0, 2, 4, 6, 8, 10, 12]
[0, 2, 4, 6, 8, 10, 12, 14]
[0, 2, 4, 6, 8, 10, 12, 14]
[0, 2, 4, 6, 8, 10, 12, 14, 16]
[0, 2, 4, 6, 8, 10, 12, 14, 16]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
>>> 
>>> for i in range(0,19):
	if i % 2 == 0:
		mylist.append(i)
		i = i + 1
    print(mylist)
    
SyntaxError: unindent does not match any outer indentation level
>>> 
>>> for i in range(0,19):
	if i % 2 == 0:
		mylist.append(i)
		i = i + 1
print(mylist)
SyntaxError: invalid syntax
>>> for i in range(0,19):
	if i % 2 == 0:
		mylist.append(i)
		i = i + 1
print(mylist)
SyntaxError: invalid syntax
>>> 
>>> for i in range(0,19):
	if i % 2 == 0:
		mylist.append(i)
		i = i + 1
	else: i = i + 1
    print(mylist)

SyntaxError: unindent does not match any outer indentation level
>>> 
>>> for i in range(0,19):
	if i % 2 == 0:
		mylist.append(i)
		i = i + 1
print(mylist)
SyntaxError: invalid syntax
>>> for i in range(0,19):
	if i % 2 == 0:
		mylist.append(i)
		i = i + 1
    print(mylist)
    
SyntaxError: unindent does not match any outer indentation level
>>> 

