
# CSV Upload and Query - Backend



## Documentation for endpoints:

### Upload CSV
I have learned that we will receive a sample CSV beforehand. With this information, I have decided to utilize SQL to create tables for storing predefined information and leverage its powerful querying capabilities.

> Columns as well as data types and format in final csv will remain same as the sample csv.


Along with CSV file link, its data type needs to be passed along to correctly parse and save in database.

![alt text](<screenshots/upload-csv.png>)

### Upload CSV Response


CSV Files are downloaded at a background task with Celery.

Task downloads a CSV file from a provided link, processes it in chunks, parses date fields, and stores each row of data. Updates the upload status of the associated file upon completion or failure.


![alt text](<screenshots/upload-csv-response.png>)



### Cities API Endpoint Documentation

![alt text](<screenshots/cities-filter-fields.png>)

## Endpoint: `/api/cities/`

### GET Method

**Description:** Retrieves cities data from a CSV file based on query parameters.

**Query Parameters:**

- `name`: Search by city name (substring match).
- `description`: Search by city description (substring match).
- `population`: Search by exact population number.
- `established_at`: Search by exact establishment date (YYYY-MM-DD format).

**Example Usage:**

- Search by city name:
  - `/api/cities/?name=Raj` (Matches cities with names like "Raj", "Rajesh", "Rajan", etc.)

- Search by population:
  - `/api/cities/?population=1000000` (Returns cities with exactly 1,000,000 population)

- Search by establishment date:
  - `/api/cities/?established_at=2020-01-01` (Returns cities established on January 1, 2020)

### BONUS Features:

- **Aggregate Searches:**
  - To get cities where population > 1,000,000:
    - `/api/cities/?population_range_min=1000000`
  - To get cities where population < 1,000,000:
    - `/api/cities/?population_range_max=1000000`

- **Date Range Searches:**
  - To get cities established after a specific date:
    - `/api/cities/?established_after=2020-01-01`

  - To get cities established before a specific date:
    - `/api/cities/?established_before=2020-01-01`

**Notes:**

- All queries support substring matching for string fields and exact matching for numerical and date fields.
- Date fields (`established_at`) support greater than (`_after`) and less than (`_before`) comparisons.

### Cities Response
![alt text](<screenshots/cities-response.png>)
# Tech Stack
Project Language: Python 3.10


Project Framework: Django 5.0.6


### Installation Steps:
```bash
git  clone

pip install poetry

poetry install

poetry shell
```

### Database Migrations
```bash
python manage.py migrate
```

### Running Server
```bash
python manage.py runserver
```


### Running Server with Docker Compose
```bash
docker compose -f docker/docker-compose.dev.yaml up --build
```

### Running Tests
```bash
python manage.py test
```


### Running Tests with Docker Compose
```bash

docker compose -f docker/docker-compose.test.yaml up --build--abort-on-container-exit

```



## Architecture



**api** - contain logic for accepting request data and passing to schemas and services



**serializers** - contain logic for validating if request data is clean, exists and of proper format and shape.



**selectors** - reusable code that queries database



**services** - reusable code that delivers fine-grained business logic.



**models** - contain data and object presentation logic



**config** - project base settings folder





### Environment variables

| Name                                    | Description                                      | Default value |
| --------------------------------------- | ------------------------------------------------ | ------------- |
| DJANGO_SETTINGS_MODULE                              | Django Settings Environment to run the server with                                       | config.settings.dev            |
| SECRET_KEY                              | Secret key                                       | -             |
| DB_NAME                                 | Database name                                    | -             |
| DB_USER                                 | Database user                                    | -             |
| DB_PASSWORD                             | Database password                                | -             |
| DB_HOST                                 | Database host                                    | -             |
| DB_PORT                                 | Database port                                    | -             |
| DEBUG                                   | Debug mode                                       | True          |
| REDIS_HOST                              | Redis DB Host                                    | -             |
| REDIS_PORT                              | Redis DB Port                                    | 6379          |



## How create superadmin?



```shell

python manage.py createsuperuser

```
