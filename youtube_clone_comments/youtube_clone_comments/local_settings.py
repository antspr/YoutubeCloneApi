SECRET_KEY = 'django-insecure-yq=+9%@^6d&k1uwzacy_vkuv9xq#pa_u-m-0=woh(hzw&aaih='

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone_comments',
        'USER': 'root',
        'PASSWORD': 'DevCodeCamp123',
        'HOST':'127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}