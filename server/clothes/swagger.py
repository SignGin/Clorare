from drf_yasg import openapi

# Request Parameter
rp_id = openapi.Parameter('id', openapi.IN_PATH, type=openapi.TYPE_INTEGER,
                          description='cloth id')

# Cloth Model Schema
cms_id = openapi.Schema(type=openapi.TYPE_INTEGER,
                        description='cloth id')
cms_category = openapi.Schema(type=openapi.TYPE_STRING, enum=['top', 'bottom', 'coat'],
                              description='cloth category\nmax_length:6')
cms_cloth_type = openapi.Schema(type=openapi.TYPE_STRING,
                                description='cloth name\nex) t-shirts, sweater, jeans')
cms_season = openapi.Schema(type=openapi.TYPE_STRING, enum=['spring', 'summer', 'autumn', 'winter'],
                            description='season to wear')
cms_gender = openapi.Schema(type=openapi.TYPE_STRING, enum=['female', 'male', 'unisex'],
                            description='gender to wear cloth')
cms_image = openapi.Schema(type=openapi.TYPE_FILE,
                           description='cloth image')

# Weather Model Schema
wms_weather = openapi.Schema(type=openapi.TYPE_STRING,
                             description='weather when you request')
wms_temperature = openapi.Schema(type=openapi.TYPE_NUMBER,
                                 description='temperature when you request')
wms_feels_like = openapi.Schema(type=openapi.TYPE_NUMBER,
                                description='feels like temperature when you request')
wms_daily_high = openapi.Schema(type=openapi.TYPE_NUMBER,
                                description='daily high temperature when you request')
wms_daily_low = openapi.Schema(type=openapi.TYPE_NUMBER,
                               description='daily low temperature when you request')
wms_humidity = openapi.Schema(type=openapi.TYPE_INTEGER,
                              description='humidity when you request')
wms_wind_speed = openapi.Schema(type=openapi.TYPE_NUMBER,
                                description='wind speed when you request')

# System Message Schema
sms_200 = openapi.Schema(type=openapi.TYPE_STRING,
                         description='200 Success message')
sms_202 = openapi.Schema(type=openapi.TYPE_STRING,
                         description='202 accepted message')
sms_400 = openapi.Schema(type=openapi.TYPE_STRING,
                         description='400 error message')
sms_403 = openapi.Schema(type=openapi.TYPE_STRING,
                         description='403 error message')
sms_404 = openapi.Schema(type=openapi.TYPE_STRING,
                         description='404 error message')
sms_500 = openapi.Schema(type=openapi.TYPE_STRING,
                         description='500 error message')

# Header Schema
csrf_token = openapi.Schema(type=openapi.IN_HEADER,
                       description='CSRF-Token')

# key str
del_key = openapi.Schema(type=openapi.TYPE_STRING,
                         description='The key for clean up all clothes data is\n(delete all clothes data)')
