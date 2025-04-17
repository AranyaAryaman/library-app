# Library App 📚

A simple web application built with **Flask** and **PostgreSQL** to manage a library system.

Users can:
- Enter their **Member ID** and view all loans they have ever made.
- Click on any **Book ID** to view **available copies** across library branches.

---

## 🚀 Technologies Used

- Python 3.x
- Flask
- PostgreSQL (psycopg2)
- HTML/CSS (Jinja2 templates)

---

## 🛠️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/AranyaAryaman/library-app.git
cd library-app
```

2. **Install Dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up the Database**

Make sure you have PostgreSQL running locally.

Connect to your database:

```bash
psql -U aranya -d library
```

Ensure the following tables exist:

- `Member`
- `Book`
- `LibraryBranch`
- `BookCopy`
- `Loan`

(Plus optional views: `available_books`, `book_view`.)

4. **Run the Flask App**

```bash
python app.py
```

Then visit: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 📂 Project Structure

```
library-app/
│
├── app.py             # Main Flask app
├── requirements.txt   # Python dependencies
├── templates/         # HTML templates
│   ├── home.html
│   ├── loans.html
│   └── available.html
├── .gitignore         # Ignored files and folders
└── README.md          # Project documentation
```

---

## ✨ Features

- View all loans made by a member.
- Click on any Book ID to see available copies.
- Clean separation of backend (Flask) and frontend (HTML templates).
- Secure SQL queries with parameterized inputs.

---
