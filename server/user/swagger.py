from drf_yasg import openapi

# Request Parameter
rp_id = openapi.Parameter('id', openapi.IN_PATH, type=openapi.TYPE_INTEGER,
                          description='cloth id')
rp_gender = openapi.Parameter('gender', openapi.IN_PATH, type=openapi.TYPE_INTEGER, enum=[0, 1],
                              description='gender to wear cloth\nfemale=0\nmale=1')

# User Model Schema
ums_id = openapi.Schema(type=openapi.TYPE_INTEGER,
                        description='user id')
ums_password = openapi.Schema(type=openapi.TYPE_STRING,
                              description='user password\nthis value is encrypted')
ums_email = openapi.Schema(type=openapi.TYPE_STRING,
                           description='user email\nemail format')
ums_name = openapi.Schema(type=openapi.TYPE_STRING,
                          description='user name\ndefault value is null')
ums_gender = openapi.Schema(type=openapi.TYPE_STRING,
                          description='user gender\ndefault value is unisex')
ums_is_staff = openapi.Schema(type=openapi.TYPE_BOOLEAN,
                              description='staff status')
ums_is_superuser = openapi.Schema(type=openapi.TYPE_BOOLEAN,
                                  description='administrator status')
ums_last_login = openapi.Schema(type=openapi.FORMAT_DATETIME,
                                description='user last login')
ums_date_joined = openapi.Schema(type=openapi.FORMAT_DATETIME,
                                 description='user date joined')

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

# Token Schema
ts_access_token = openapi.Schema(type=openapi.TYPE_STRING,
                              description='Access-Token')
ts_refresh_token = openapi.Schema(type=openapi.TYPE_STRING,
                               description='refresh-Token')

# Header Schema
access_token = openapi.Schema(type=openapi.IN_HEADER,
                              description='Access-Token')
refresh_token = openapi.Schema(type=openapi.IN_HEADER,
                               description='refresh-Token')
