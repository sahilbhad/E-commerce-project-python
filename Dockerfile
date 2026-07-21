# ---- Base image ----
FROM python:3.12-slim

# Prevent Python from writing .pyc files & buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps needed by Pillow / sqlite
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libjpeg-dev \
        zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install python deps first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Collect static files (won't fail build even if none configured yet)
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# Use gunicorn in production; ecom is the project package (ecom/wsgi.py)
CMD ["gunicorn", "ecom.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
