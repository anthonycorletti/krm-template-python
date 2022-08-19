"""gunicorn server configuration."""
import os

threads = 1
workers = 1
timeout = 30
bind = f":{os.environ.get('PORT', '8000')}"
worker_class = "uvicorn.workers.UvicornWorker"
