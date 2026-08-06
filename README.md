
# Backend Development Journey

This repository contains the projects I'm building while learning backend development with Python.

Instead of keeping one large project, I build small focused projects while learning new concepts. Older projects are intentionally left as they were built so I can look back and see how my code, architecture, and understanding have improved over time.

The goal is not to create perfect projects, but to document the learning process from backend fundamentals to production-ready backend development.

---

# Learning Goals

This repository focuses on learning how to:

- Build REST APIs with FastAPI
- Design clean API architecture
- Validate requests using Pydantic
- Work with PostgreSQL
- Use SQLModel ORM
- Design relational databases
- Build CRUD APIs
- Understand transactions
- Write maintainable backend code
- Learn production backend practices

---

# Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Framework | FastAPI |
| Validation | Pydantic |
| ORM | SQLModel |
| Database | PostgreSQL |
| Driver | Psycopg |
| Server | Uvicorn |
| Configuration | python-dotenv |

---

# Repository Structure

```text
backend-dev/
│
├── day_01_http_fastapi_fundamentals/
├── day_02_restful_api_design/
├── day_03_library_management_api/
├── ...
├── shop-management-api/
│
├── requirements.txt
└── README.md
```

Each directory represents a learning milestone. Older projects are not rewritten after learning better practices because they represent the knowledge I had when they were built.

---

# Projects

## Day 01 — FastAPI Fundamentals

Topics:

- FastAPI setup
- Routing
- Path Parameters
- Query Parameters
- Request Handling

---

## Day 02 — REST API Design

Project:

Book Inventory API

Topics:

- CRUD APIs
- REST conventions
- Request validation
- Error handling
- HTTP status codes

---

## Day 03 — Library Management API

Project implementing:

- Book management
- Member management
- Borrow / Return workflow
- JSON storage
- Modular project structure

---

## PostgreSQL & SQLModel

Topics covered:

- PostgreSQL
- Psycopg
- Environment variables
- SQLModel
- ORM basics
- Database sessions

---

## Shop Management API (Current Project)

This project is where every new backend concept is applied.

### Completed

- PostgreSQL Integration
- SQLModel ORM
- Database Sessions
- Item Model
- Create Item
- Get All Items
- Get Item by ID

### In Progress

- Update Item
- Transaction Module
- Batch Management
- Reports

### Planned

- Inventory Tracking
- Sales Tracking
- Profit Reports
- Stock Analytics
- Expiry Reports

---

# Current Progress

| Topic | Status |
|--------|:------:|
| FastAPI | Completed |
| REST API Design | Completed |
| Pydantic | Completed |
| PostgreSQL | Completed |
| SQLModel | Completed |
| CRUD Operations | In Progress |
| Transactions | In Progress |
| Authentication | Planned |
| Alembic | Planned |
| Testing | Planned |
| Docker | Planned |
| Redis | Planned |
| Deployment | Planned |

---

# Learning Roadmap

## Phase 1

- FastAPI
- REST APIs
- Pydantic
- PostgreSQL
- SQLModel
- CRUD

## Phase 2

- Relationships
- Transactions
- Alembic
- Authentication
- Testing
- Docker

## Phase 3

- Redis
- Background Jobs
- CI/CD
- Deployment
- Monitoring
- System Design

---

# Running a Project

Clone the repository

```bash
git clone https://github.com/bharat690/backend-dev.git
cd backend-dev
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
DATABASE_URL=your_postgresql_connection_string
```

Run a project

```bash
cd shop-management-api
uvicorn main:app --reload
```

or

```bash
cd day_03_library_management_api
uvicorn main:app --reload
```

---

# Repository Philosophy

This repository is a learning archive.

Projects are not rewritten after learning newer techniques because I want the repository to show real progress instead of pretending every project was built with my current knowledge.

If someone scrolls through the folders or Git history, they should be able to see how the code improves over time.

---

# Current Focus

Currently learning:

- SQLModel ORM
- PostgreSQL
- CRUD with ORM
- Transactions
- Backend Architecture
- Clean Project Structure

---

# Future Topics

After completing the current project, the plan is to learn:

- Alembic
- Dependency Injection
- JWT Authentication
- Async SQLAlchemy
- pytest
- Docker
- Redis
- Celery
- Background Tasks
- CI/CD
- Production Deployment
- Logging
- Monitoring
- System Design

---

# Feedback

If you notice better architecture, cleaner code, or design improvements, feel free to open an issue or submit a pull request.

I'm always interested in learning better backend engineering practices.

---

# Connect

If you're learning backend development as well, feel free to connect or discuss ideas. I'm documenting this repository as I learn, one project at a time.

