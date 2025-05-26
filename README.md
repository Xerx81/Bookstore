
# Bookstore

This project is a simple online bookstore built with Django which is result of the book *Django for Professionals*.

The goal was to get comfortable with building a real-world Django app—handling things like user authentication, models, views, templates, along with Docker and Postresql.

It’s not meant to be a polished product, but more of a learning project that helped me understand how everything fits together.


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

## Screenshots

