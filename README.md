# Article API

REST API for managing articles and users, built with FastAPI.

## Tech stack

- Python 3.10
- FastAPI
- SQLAlchemy + SQLite
- JWT authentication (python-jose)
- Docker + nginx (HTTPS)

## Running the project

### With Docker (recommended)

```bash
git clone <repo-url>
cd article-api
docker-compose up --build
```

API will be available at `https://localhost`  
Swagger docs at `https://localhost/docs`

> Note: The app uses a self-signed certificate, so your browser will show a security warning. Click "Advanced" and proceed.

### Without Docker

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`

## Endpoints

### Auth
- `POST /auth/register` — register a new user
- `POST /auth/login` — login and receive JWT token

### Articles
- `POST /articles/` — create article (requires auth)
- `GET /articles/` — list articles (public, supports pagination)
- `GET /articles/{id}` — get single article (public)
- `PATCH /articles/{id}` — update article (requires auth, author only)
- `DELETE /articles/{id}` — delete article (requires auth, author only)
- `POST /articles/bulk` — bulk import articles (requires auth)

### Users
- `GET /users/me` — get current user (requires auth)
- `POST /users/me/subscribe` — subscribe to notifications (requires auth)
- `DELETE /users/me/subscribe` — unsubscribe (requires auth)
- `GET /users/me/notifications` — get notifications (requires auth)

## Design decisions

**SQLite** — chosen for simplicity. In production this would be replaced with PostgreSQL.

**In-memory notifications** — notifications are stored in memory. In production this would be replaced with a message queue (e.g. Celery + Redis) and an email service. Notifications reset on server restart.

**Self-signed certificate** — used for development/demo purposes. In production a valid certificate from a CA (e.g. Let's Encrypt) would be used.

**JWT authentication** — stateless authentication using JSON Web Tokens. Tokens expire after 30 minutes.

**Authorization** — only the author of an article can update or delete it (403 Forbidden for unauthorized attempts).