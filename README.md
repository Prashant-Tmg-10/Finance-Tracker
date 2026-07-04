# Full Finance Management system -------still on working phase

A scalable backend application built with **FastAPI** that helps users manage expenses, budgets, and financial records through a clean and modular REST API architecture.

This project follows a layered architecture pattern with separate modules for routing, business logic, validation, and database operations, making it maintainable, scalable, and production-ready.

---

## 🚀 Features

### 👤 User Management
- Create and manage users
- Maintain user-specific financial records
- Structured user module architecture

### 💸 Expense Management
- Create expenses
- Retrieve expense history
- Update expense records
- Delete expenses
- Categorize expenses

### 📊 Budget Management
- Create monthly budgets
- Update budget allocations
- Monitor spending limits
- Delete budgets

### ✅ Data Validation
- Request validation using Pydantic DTOs
- Consistent API response structures
- Type-safe data handling

### ⚙️ Configuration Management
- Environment-based configuration
- Centralized settings management
- Secure handling of sensitive data

### 📚 API Documentation
- Interactive Swagger UI
- ReDoc documentation
- Automatic OpenAPI schema generation

---

## 🏗️ Architecture

The application follows a layered architecture:

```text
Client Request
      │
      ▼
 Router Layer
      │
      ▼
Controller Layer
      │
      ▼
 Database Layer
      │
      ▼
   Database
```

### Router Layer
Handles API endpoints and request routing.

### Controller Layer
Contains business logic and application workflows.

### DTO Layer
Validates incoming requests and outgoing responses.

### Model Layer
Defines database entities and relationships.

### Utility Layer
Provides reusable helpers, settings, and database configuration.

---

## 📂 Project Structure

```text
Finance-Tracker/
│
├── src/
│
├── budget/
│   ├── controller.py
│   ├── router.py
│   ├── models.py
│   ├── dtos.py
│   └── enum.py
│
├── expense/
│   ├── controller.py
│   ├── router.py
│   ├── models.py
│   ├── dtos.py
│   └── enum.py
│
├── user/
│   ├── controller.py
│   ├── router.py
│   ├── models.py
│   └── dtos.py
│
├── utils/
│   ├── db.py
│   ├── settings.py
│   └── helpers.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| FastAPI | Backend Framework |
| SQLAlchemy | ORM |
| Pydantic | Data Validation |
| PostgreSql | Database |
| Uvicorn | ASGI Server |
| Python-dotenv | Environment Management |

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Prashant-Tmg-10/finance-tracker.git
cd finance-tracker
```

### Create Virtual Environment

```bash
python -m venv env
```

### Activate Virtual Environment

#### Windows

```bash
env\Scripts\activate
```

#### Linux / macOS

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=sqlite:///finance.db
```

### Run Application

```bash
uvicorn main:app --reload
```

---

## 📖 API Documentation

After starting the server, access:

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

---

## 🔍 Core Modules

### Expense Module
Responsible for managing expense-related operations.

- Create Expense
- View Expenses
- Update Expense
- Delete Expense

### Budget Module
Responsible for budget management.

- Create Budget
- View Budget
- Update Budget
- Delete Budget

### User Module
Responsible for user-related operations.

- Create User
- Manage User Data
- Associate Financial Records

---

## 🔒 Security & Best Practices

- Environment variables managed through `.env`
- Sensitive files ignored using `.gitignore`
- Request validation using DTOs
- Modular and maintainable architecture
- Separation of concerns across layers

---

## 🎯 Future Enhancements

Planned improvements include:

- JWT Authentication
- Password Hashing
- PostgreSQL Integration
- Alembic Database Migrations
- Docker Support
- Automated Testing with Pytest
- Financial Analytics Dashboard
- Budget Alerts & Notifications
- Recurring Expense Tracking
- PDF & Excel Report Generation
- CI/CD Pipeline with GitHub Actions
- Role-Based Access Control (RBAC)

---

## 💡 Key Backend Concepts Demonstrated

- RESTful API Development
- CRUD Operations
- Layered Architecture
- Data Validation
- Environment-Based Configuration
- Database Integration
- API Documentation
- Modular Project Structure
- Separation of Concerns

---

## 👨‍💻 Author

**Prashant**

Backend Developer | Python Developer

GitHub: https://github.com/Prashant-Tmg-10

---

## 📄 License

This project is developed for learning, portfolio, and educational purposes.
