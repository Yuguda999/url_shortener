
# URL Shortener API

This is a simple RESTful API for a URL shortening service, built using Django and Django Rest Framework (DRF). The API allows users to shorten URLs, retrieve the original URL from a shortcode, update and delete short URLs, and view statistics on how many times a short URL has been accessed.
https://roadmap.sh/projects/url-shortening-service

## Features

- **Create a Short URL**: Generate a short URL for a given long URL.
- **Retrieve Original URL**: Retrieve the original URL using the short code.
- **Update Short URL**: Update an existing short URL with a new long URL.
- **Delete Short URL**: Delete a short URL from the database.
- **URL Statistics**: Get access statistics for a short URL, including the number of times it has been accessed.

## Endpoints

### 1. Create Short URL
- **URL**: `/api/shorten/`
- **Method**: `POST`
- **Payload**: 
  ```json
  {
    "url": "https://www.example.com/some/long/url"
  }
  ```
- **Response**:
  ```json
  {
    "id": "1",
    "url": "https://www.example.com/some/long/url",
    "shortCode": "abc123",
    "createdAt": "2021-09-01T12:00:00Z",
    "updatedAt": "2021-09-01T12:00:00Z"
  }
  ```

### 2. Retrieve Original URL
- **URL**: `/api/shorten/<shortCode>/`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "id": "1",
    "url": "https://www.example.com/some/long/url",
    "shortCode": "abc123",
    "createdAt": "2021-09-01T12:00:00Z",
    "updatedAt": "2021-09-01T12:00:00Z",
    "accessCount": 5
  }
  ```

### 3. Update Short URL
- **URL**: `/api/shorten/<shortCode>/update/`
- **Method**: `PUT`
- **Payload**:
  ```json
  {
    "url": "https://www.example.com/updated/url"
  }
  ```
- **Response**:
  ```json
  {
    "id": "1",
    "url": "https://www.example.com/updated/url",
    "shortCode": "abc123",
    "createdAt": "2021-09-01T12:00:00Z",
    "updatedAt": "2021-09-01T12:30:00Z",
    "accessCount": 5
  }
  ```

### 4. Delete Short URL
- **URL**: `/api/shorten/<shortCode>/delete/`
- **Method**: `DELETE`
- **Response**: `204 No Content`

### 5. Get URL Statistics
- **URL**: `/api/shorten/<shortCode>/stats/`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "id": "1",
    "url": "https://www.example.com/some/long/url",
    "shortCode": "abc123",
    "createdAt": "2021-09-01T12:00:00Z",
    "updatedAt": "2021-09-01T12:00:00Z",
    "accessCount": 10
  }
  ```

## Setup and Installation

### Prerequisites
- Python 3.x
- Django
- Django Rest Framework
- drf-yasg (for Swagger documentation)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/url-shortener.git
   cd url-shortener
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

5. Access the API at `http://127.0.0.1:8000/api/`.

### API Documentation
Swagger and Redoc documentation are available:
- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- Redoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Running Tests

To run tests, use:
```bash
python manage.py test
```

## Example Usage with `curl`

**Create Short URL**:
```bash
curl -X POST http://127.0.0.1:8000/api/shorten/ -H "Content-Type: application/json" -d '{"url": "https://www.example.com/some/long/url"}'
```

**Retrieve Original URL**:
```bash
curl -X GET http://127.0.0.1:8000/api/shorten/abc123/
```

**Update Short URL**:
```bash
curl -X PUT http://127.0.0.1:8000/api/shorten/abc123/update/ -H "Content-Type: application/json" -d '{"url": "https://www.example.com/updated/url"}'
```

**Delete Short URL**:
```bash
curl -X DELETE http://127.0.0.1:8000/api/shorten/abc123/delete/
```

**Get URL Statistics**:
```bash
curl -X GET http://127.0.0.1:8000/api/shorten/abc123/stats/
```

## License
This project is licensed under the MIT License.
