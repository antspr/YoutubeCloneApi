SECRET_KEY = 'django-insecure-yq=+9%@^6d&k1uwzacy_vkuv9xq#pa_u-m-0=woh(hzw&aaih='

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'youtube_clone_comments',
        'USER': 'root',
        'PASSWORD': 'd3WK0DEckaMP',
        'HOST':'127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}