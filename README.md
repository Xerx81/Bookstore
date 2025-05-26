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

![image](https://github.com/user-attachments/assets/f487e9df-4180-4406-8d35-ed0c00e8a5e7)

![image](https://github.com/user-attachments/assets/6717e791-6dab-4c89-9972-b24bf11ab854)

![image](https://github.com/user-attachments/assets/2dc8fe9a-6590-4141-87b3-55b77822d6bb)

![image](https://github.com/user-attachments/assets/c5ad1362-4e99-4b39-b02a-3ea897245dc7)

![image](https://github.com/user-attachments/assets/c1c3ec40-0bdd-4621-ab45-97057c31f728)

![image](https://github.com/user-attachments/assets/aad7aef8-19c1-4b97-9c29-47a317527c15)

