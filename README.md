# Full Finance Management system -------still on working phase

A scalable backend application built with **FastAPI** that helps users manage expenses, budgets, and financial records through a clean and modular REST API architecture.

This project follows a layered architecture pattern with separate modules for routing, business logic, validation, and database operations, making it maintainable, scalable, and production-ready.

---

## 🚀 Features

## ✅ Current Features

Implemented so far:

- User Registration
- User Login
- JWT Authentication
- Password Hashing
- PostgreSQL Database Integration
- SQLAlchemy ORM
- Alembic Database Migrations
- Expense CRUD Operations
- Budget CRUD Operations
- Budget Summary API
- Expense Filtering with Query Parameters
- Input Validation using Pydantic
- Protected Routes with Dependency Injection
- Clean Layered Architecture (Router → Controller → Database)

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
- ## 🎯 Future Enhancements

Planned improvements include:

- Expense Pagination
- Expense Analytics
- Monthly Financial Reports
- Budget Alerts & Notifications
- Recurring Expense Tracking
- CSV/PDF & Excel Report Generation
- Docker Support
- Automated Testing with Pytest
- CI/CD Pipeline with GitHub Actions
- Role-Based Access Control (RBAC)
- Admin Dashboard & User Management
- Automated Testing with Pytest
- Financial Analytics Dashboard
- Budget Alerts & Notifications

  
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
