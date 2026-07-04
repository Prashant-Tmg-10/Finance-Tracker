# 💰 Finance Tracker API

A RESTful backend application built with **FastAPI** for managing personal finances, including expenses, budgets, and categories. The project follows a modular structure, uses environment-based configuration, and provides interactive API documentation for easy testing and integration.

---

## 🚀 Features

### Expense Management
- Create new expenses
- View all expenses
- Get expense details by ID
- Update existing expenses
- Delete expenses

### Category Management
- Create categories
- View available categories
- Update category information
- Delete categories

### Budget Tracking
- Set monthly budgets
- Monitor spending against budgets
- Manage budget records

### Validation & Configuration
- Request validation using Pydantic
- Environment variable management using `.env`
- Centralized application settings
- Error handling and response validation

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| FastAPI | REST API framework |
| Pydantic | Data validation |
| SQLAlchemy | Database ORM |
| SQLite / PostgreSQL | Database |
| Uvicorn | ASGI server |
| Python-dotenv | Environment variable management |

---

## 📂 Project Structure

```text
Finance-Tracker/
│
├── src/
│   ├── api/
│   │   ├── routes/
│   │   └── dependencies/
│   │
│   ├── models/
│   │   └── database models
│   │
│   ├── schemas/
│   │   └── request/response schemas
│   │
│   ├── services/
│   │   └── business logic
│   │
│   └── utils/
│       ├── db.py
│       ├── settings.py
│       └── helpers.py
│
├── .env
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Finance-Tracker
```

### 2. Create Virtual Environment

```bash
python -m venv env
```

### 3. Activate Virtual Environment

**Windows**

```bash
env\Scripts\activate
```

**Linux / macOS**

```bash
source env/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=your_database_url
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

After starting the server, visit:

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

---

## 🔄 API Capabilities

### Expenses
- Create expense
- Get all expenses
- Get expense by ID
- Update expense
- Delete expense

### Categories
- Create category
- Get all categories
- Update category
- Delete category

### Budgets
- Create budget
- View budgets
- Update budget
- Delete budget

---

## 🔒 Environment Configuration

Sensitive configuration values are stored in `.env` files and excluded from version control using `.gitignore`.

Example:

```env
DATABASE_URL=postgresql://user:password@localhost/finance_tracker
```

---

## 🎯 Future Improvements

- JWT Authentication & Authorization
- User Accounts & Profiles
- Expense Analytics Dashboard
- Monthly Financial Reports
- Docker Containerization
- Unit & Integration Testing
- PostgreSQL Production Deployment
- CI/CD Pipeline

---

## 📚 What I Learned

Through this project I gained practical experience with:

- Building REST APIs using FastAPI
- Database integration and CRUD operations
- Request validation using Pydantic
- Environment-based configuration management
- Organizing backend applications with a modular architecture
- API documentation using Swagger and ReDoc
- Git and GitHub version control workflows

---

## 👨‍💻 Author

**Prashant**

Backend Developer | Python Enthusiast

GitHub: https://github.com/Prashant-Tmg-10

---

## 📄 License

This project is created for learning and portfolio purposes.
