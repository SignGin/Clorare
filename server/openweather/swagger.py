from drf_yasg import openapi

# Weather Model Schema
wms_id = openapi.Schema(type=openapi.TYPE_INTEGER,
                        description='weather data id')
wms_weather = openapi.Schema(type=openapi.TYPE_STRING,
                             description='weather when you request')
wms_temperature = openapi.Schema(type=openapi.FORMAT_FLOAT,
                                 description='temperature when you request')
wms_feels_like = openapi.Schema(type=openapi.FORMAT_FLOAT,
                                description='feels like temperature when you request')
wms_daily_high = openapi.Schema(type=openapi.FORMAT_FLOAT,
                                description='daily high temperature when you request')
wms_daily_low = openapi.Schema(type=openapi.FORMAT_FLOAT,
                               description='daily low temperature when you request')
wms_humidity = openapi.Schema(type=openapi.TYPE_INTEGER,
                              description='humidity when you request')
wms_wind_speed = openapi.Schema(type=openapi.FORMAT_FLOAT,
                                description='wind speed when you request')
wms_time = openapi.Schema(type=openapi.FORMAT_DATETIME,
                          description='time when you request')

# System Message Schema
sms_400 = openapi.Schema(type=openapi.TYPE_STRING,
                         description='400 error message')
sms_500 = openapi.Schema(type=openapi.TYPE_STRING,
                         description='500 error message')