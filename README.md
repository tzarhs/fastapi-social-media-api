# FastAPI Social Media API

## Overview

A REST API built with Python and FastAPI that supports post management, user registration, authentication, and voting.

The application uses PostgreSQL for data storage and SQLAlchemy for database interactions. Pydantic handles data validation and response schemas, while Alembic manages database migrations. The project also covers automated testing with Pytest, containerization with Docker, and CI/CD using GitHub Actions.

## Features

- **User Registration:** Create user accounts and securely hash passwords.
- **Authentication:** Authenticate users using JWT access tokens and OAuth2.
- **Post Management:** Create, retrieve, update, and delete posts.
- **Authorization:** Restrict post modifications to their owners.
- **Voting System:** Implement voting functionality for posts.
- **Database Relationships:** Connect users, posts, and votes using foreign keys and SQLAlchemy relationships.
- **Data Validation:** Validate request data and define API response models using Pydantic.
- **Database Migrations:** Manage database schema changes with Alembic.
- **Automated Testing:** Test application functionality and API endpoints with Pytest.
- **Containerization:** Use Docker and Docker Compose.
- **CI/CD:** Automate testing and deployment using GitHub Actions.
- **Deployment:** Configure and deploy the application to production environments.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| PostgreSQL | Relational database |
| SQLAlchemy | Object-relational mapping |
| Pydantic | Data validation and serialization |
| Alembic | Database migrations |
| JWT and OAuth2 | Authentication |
| Pytest | Automated testing |
| Postman | API request testing |
| Docker and Docker Compose | Containerization |
| Git and GitHub | Version control |
| GitHub Actions | CI/CD automation |
| Gunicorn | Application serving |
| NGINX | Reverse proxy |
| Ubuntu | Server environment |

## Core API Functionality

### Users
- Register users.
- Hash passwords.
- Authenticate users and generate access tokens.
- Retrieve user information.
- Identify authenticated users on protected routes.

### Posts
- Create posts.
- Retrieve all posts or individual posts.
- Update posts.
- Delete posts.
- Associate posts with their owners.
- Enforce ownership restrictions on modifications and retrieval.

### Votes
- Create votes associated with users and posts.
- Manage voting through API routes.
- Retrieve related information using SQL joins and SQLAlchemy relationships.

## Database

The application uses PostgreSQL and SQLAlchemy to manage persistent data.

Database topics covered in the implementation include:

- Creating database tables and schemas.
- Performing CRUD operations.
- Defining foreign keys and relationships.
- Querying related records with SQL joins.
- Managing schema changes with Alembic migrations.
- Configuring a separate database for testing.

## Testing

Pytest is used to test application functionality, including:

- API endpoints and response status codes.
- User registration and authentication.
- Token validation.
- Database operations.
- Error handling and exceptions.
- Fixtures and parameterized tests.
- FastAPI endpoints using `TestClient`.

## Deployment and CI/CD

The project covers:

- Configuring environment variables.
- Deploying to Heroku.
- Deploying to an Ubuntu server.
- Running the application with Gunicorn.
- Configuring NGINX and HTTPS.
- Containerizing the application with Docker.
- Running PostgreSQL with Docker Compose.
- Automating tests, Docker builds, and deployment with GitHub Actions.

## Technologies Summary

The project combines API development, relational database management, authentication, automated testing, containerization, and deployment automation in a Python backend application.
