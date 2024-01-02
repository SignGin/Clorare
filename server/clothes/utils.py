def time():
    import datetime
    time_format = '%Y%m%d'
    return datetime.datetime.now().strftime(time_format)


def dec_b64_img(dict_data):
    import base64
    from django.conf import settings

    if dict_data['image']:
        header, data = dict_data['image'].split(';base64,')
        data_format, ext = header.split('/')

        image_name = time() + '_' + dict_data['cloth_type']
        dec_data = base64.b64decode(data)
        image_root = f'{settings.MEDIA_ROOT}\\clothes\\{image_name}.{ext}'

        with open(image_root, 'wb') as f:
            f.write(dec_data)

        return f'/{image_name}.{ext}'
    return None
