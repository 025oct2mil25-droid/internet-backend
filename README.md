# Backend (FastAPI) — Internet API de ejemplo

Funciones:

- Registro de usuarios (`POST /auth/register`)
- Login con JWT (`POST /auth/login`) — usa `username` (email) y `password` (form-data)
- Perfil del usuario (`GET /me`)
- CRUD básico de items (`/items`) — requiere Bearer token

## Cómo ejecutar

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # edita SECRET_KEY
uvicorn app.main:app --reload --port 8000
```

La API quedará en `http://127.0.0.1:8000` y la documentación interactiva en `http://127.0.0.1:8000/docs`.

## Despliegue rápido

### Opción A: Docker local
```bash
docker compose up --build
# API en http://localhost:8000/docs
```

### Opción B: Render.com (gratis)
1. Sube esta carpeta a un repo en GitHub.
2. En Render, crea un **Web Service** desde ese repo. Detectará `Dockerfile` automáticamente.
3. Expón el puerto **8080** (Render lo hace solo).
4. Añade variables de entorno: `SECRET_KEY`, `ACCESS_TOKEN_EXPIRE_MINUTES`, y si usas Postgres, `DATABASE_URL`.
5. Obtendrás una URL pública (ej: `https://internet-backend.onrender.com`). Úsala en la app Android.

### Opción C: Fly.io
Puedes usar este `Dockerfile` tal cual. (Si lo quieres, te genero `fly.toml` y comandos).
