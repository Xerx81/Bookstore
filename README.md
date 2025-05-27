# Bookstore

A Django-powered web application for managing bookstore operations, featuring user authentication, book cataloging, and media integration.

## Tech Stack

**Backend:** Python, Django

**Frontend:** Html, CSS, Javascript

**Database:** Postgresql

**Containerization:** Docker, Docker Compose


## Features

- **User Authentication:** Secure login and registration system made using "Allauth".
- **Book Catalogs:** Browse through a collection of books with category filters or using search.
- **Review:** Write reviews for books and see other reviews.
- **Admin Panel:** Administration panel for managing users and books.
- **Responsive Design:** User friendly interface accessible on various devices.


## Run Locally

Clone the project

```bash
git clone https://github.com/Xerx81/Bookstore.git
```

Go to the project directory

```bash
cd Bookstore
```

Build and start server

```bash
docker compose up -d --build
```

Apply database migrations

```bash
docker compose exec web python manage.py migrate
```

Go to link: http://localhost:8000


## Usage

Create super user
```bash
docker compose exec web python manage.py createsuperuser
```

Go to http://localhost:8000/admin login and add book data.


## Screenshots

![image](https://github.com/user-attachments/assets/f487e9df-4180-4406-8d35-ed0c00e8a5e7)

![image](https://github.com/user-attachments/assets/6717e791-6dab-4c89-9972-b24bf11ab854)

![image](https://github.com/user-attachments/assets/2dc8fe9a-6590-4141-87b3-55b77822d6bb)

![image](https://github.com/user-attachments/assets/c5ad1362-4e99-4b39-b02a-3ea897245dc7)

![image](https://github.com/user-attachments/assets/c1c3ec40-0bdd-4621-ab45-97057c31f728)

![image](https://github.com/user-attachments/assets/aad7aef8-19c1-4b97-9c29-47a317527c15)
