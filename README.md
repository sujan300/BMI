# BMI Project
Body Mass Index (BMI) is a measure to understand whether your body weight is healthy as per your height.



## Authors

- [@sujan300](https://github.com/sujan300)


## Live Demo  https://bmi-web-django.herokuapp.com/

## Tech Stack

**Client:** HTML, CSS, Javascript,Bootstrap

**Server:** python,Django


## Run Locally

Clone the project

```bash
  git clone git@github.com:sujan300/BMI.git
```

Go to the project directory

```bash
  cd BMI
```

Install dependencies

```bash
  pip install django
  pip install requests
```

create super user

```bash
    python manage.py createsuperuser
```


migrate and migrations

```bash
    python manage.py makemigrations
    python manage.py migrate
```


## Optimizations
## Add on settings.py 

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST          = 'smtp.gmail.com'

EMAIL_PORT          = 587

EMAIL_HOST_USER     = 'Your Email'

EMAIL_HOST_PASSWORD = "Your Email Password"

EMAIL_USE_TLS       = True

### Don't Forget turn Your less secure app on your email account

Start the server

```bash
  python manage.py runserver
```

### GO localhost:8000 


## Features

- It can save Our Bmi
- Send Email on Our register email
- Full Authentication of Django
- BMI calculation
- Give Suggestion etc ..
