def dec_b64_img(dict_data):
    if dict_data['image']:
        import base64
        import datetime
        from django.conf import settings

        header, data = dict_data['image'].split(';base64,')
        data_format, ext = header.split('/')
        time_format = '%y%m%d%H%M%S'

        image_name = datetime.datetime.now().strftime(time_format) + '_' + dict_data['cloth_type']
        dec_data = base64.b64decode(data)
        image_root = f'{settings.MEDIA_ROOT}\\clothes\\{image_name}.{ext}'

        with open(image_root, 'wb') as f:
            f.write(dec_data)

        return f'{image_name}.{ext}'
    return None


def modifying_image_path(dict_data):
    image = dict_data['image']
    if dict_data['image']:
        from django.conf import settings

        file_name = dict_data['image']
        image = f'{settings.MEDIA_ROOT}\\clothes\\{file_name}'

    context = {
        'category': dict_data['category'],
        'cloth_type': dict_data['cloth_type'],
        'season': dict_data['season'],
        'gender': dict_data['gender'],
        'image': image
    }
    return context
