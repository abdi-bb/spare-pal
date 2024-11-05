
---

# SparePal

SparePal is a platform that connects users with genuine, high-quality parts from trusted suppliers.

## ER Diagram
![ER Diagram](./spare-pal/static/img/ERDiagram.png)

## Project Structure
```
spare-pal/
├── apps
│   ├── accounts
│   └── suppliers
├── core
├── db.sqlite3
├── docker-compose.yml
├── docker-compose.prod.yml
├── Dockerfile
├── entrypoint.sh
├── manage.py
├── requirements.txt
├── static
└── venv
```

## Running the Django App

### 1. Using Docker

#### Prerequisites
- Docker and Docker Compose installed.

#### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/abdi-bb/spare-pal.git
   cd spare-pal
   ```

2. **Set Up Environment Variables**
   - Copy `.env.example` to `.env` and update with your configuration:
     ```bash
     cp .env.example .env
     ```
   - Ensure `.env` contains required variables, e.g., `DB_USERNAME`, `DB_PASSWORD`, `DB_NAME`, and `NGINX_PORT`.

3. **Build and Start Services**
   Use `docker-compose` to build and start all containers.
   ```bash
   docker-compose up --build
   ```

4. **Run Migrations**
   Once containers are up, apply migrations to set up the database.
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Create a Superuser (Optional)**
   Create a superuser to access the Django admin interface.
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Access the Application**
   - **API Documentation**: [http://localhost:8000/api](http://localhost:8000/api)
   - **Swagger UI**: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
   - **ReDoc Documentation**: [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)

7. **Stopping Services**
   To stop the containers, use:
   ```bash
   docker-compose down
   ```

### 2. Running Without Docker

If you prefer to run the Django app without Docker, follow these steps.

1. **Clone the Repository**
   ```bash
   git clone https://github.com/abdi-bb/spare-pal.git
   cd spare-pal
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   - **API Documentation**: [http://localhost:8000/api](http://localhost:8000/api)
   - **Swagger UI**: [http://localhost:8000/api/schema/swagger-ui/](http://localhost:8000/api/schema/swagger-ui/)
   - **ReDoc Documentation**: [http://localhost:8000/api/schema/redoc/](http://localhost:8000/api/schema/redoc/)

--- 