release: python manage.py makemigrations app_gallery
release: python manage.py migrate

web: gunicorn project_gallery.wsgi --log-file -