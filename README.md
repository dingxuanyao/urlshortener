### Tony's implementation of URL shortener

To start the app:
```
docker-compose up
```

To post a URL, send a POST request to `{url}:8000/urlshortener/submit` as follows (you can use postman or other API tools instead):
```
curl --location --request POST 'localhost:8000/urlshortener/submit/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "full_url": "https://facebook.com"
}'
```
A short_id will be returned

Enter the URL as follows to be redirected:
```
localhost:8000/urlshortener/{short_id}
```
To test:
```
python manage.py test
```
