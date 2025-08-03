# FastAPI EXT Project

Proyek ini merupakan implementasi REST API sederhana menggunakan **FastAPI**, **SQLModel**, dan **Alembic** sebagai database migration tool. Cocok untuk keperluan belajar, pengembangan, atau sebagai boilerplate proyek backend berbasis Python modern.

## 🔧 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework modern berbasis Python
- [SQLModel](https://sqlmodel.tiangolo.com/) - ORM dan Pydantic dalam satu model
- [Alembic](https://alembic.sqlalchemy.org/) - Migration tool untuk SQL databases
- [Uvicorn](https://www.uvicorn.org/) - ASGI server
- SQLite (default, bisa diganti PostgreSQL, dll)

---

## 📁 Struktur Proyek

```
fastapi-ext/
├── alembic/                # Folder migrasi alembic
├── app/                    # Modul utama aplikasi
│   ├── routes/             # Modular routing (notes, users)
│   ├── database.py         # Koneksi DB & model
│   ├── schema.py           # Pydantic schemas
│   └── main.py             # Entry point FastAPI
├── data/                   # File SQLite database (dev.db)
├── .env                    # File environment (DB URL, dll)
├── Dockerfile              # Untuk containerization
├── requirements.txt        # Daftar dependensi
└── README.md
```

---

## 🚀 Menjalankan Aplikasi

### 1. **Clone repo dan install dependencies**

```bash
git clone https://github.com/yourusername/fastapi-ext.git
cd fastapi-ext
python -m venv venv
source venv/bin/activate  # atau venv\Scripts\activate di Windows
pip install -r requirements.txt
```

### 2. **Atur environment**

Buat file `.env`:

```env
DATABASE_URL=sqlite:///./data/dev.db
```

### 3. **Jalankan migrasi Alembic**

```bash
alembic upgrade head
```

### 4. **Run server**

```bash
uvicorn app.main:app --reload
```

---

## 📡 Endpoint API

Buka dokumentasi interaktif:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- Scalar UI: [http://localhost:8000/scalar](http://localhost:8000/scalar)

---

## ⚙️ Alembic Command

- Membuat migration baru:
  ```bash
  alembic revision --autogenerate -m "add user table"
  ```

- Menerapkan migration:
  ```bash
  alembic upgrade head
  ```

---

## 🐳 Docker (opsional)

Build dan jalankan image:

```bash
docker build -t yourname/fastapi-ext .
docker run -p 8000:8000 yourname/fastapi-ext
```

---

## 📌 Catatan

- Default DB: SQLite (`data/dev.db`)
- Pastikan folder `data/` sudah ada sebelum menjalankan app atau migrasi

---

## 📜 Lisensi

MIT License. Free for personal and commercial use.
