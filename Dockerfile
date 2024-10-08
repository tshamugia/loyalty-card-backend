FROM python:3.11-slim


ENV PYTHONUNBUFFERED=1
# ENV PYTHODONTWRITEBYTECODE=1


WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y curl && apt-get clean
COPY . /app/

CMD python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='root').exists() or User.objects.create_superuser('root', 'root@example.com', 'root')" \
    && python manage.py runserver 0.0.0.0:8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    