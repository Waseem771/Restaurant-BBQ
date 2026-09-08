import os
import modal

# 1. Define the Modal App
app = modal.App("restaurant-bbq-backend")

# 2. Define the container image and dependencies
image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install_from_requirements("requirements.txt")
    .add_local_dir("app", remote_path="/root/app")
)

# 3. Reference the persistent volume you created
volume = modal.Volume.from_name("bbq-data")

# 4. Inject our local environment variables into the cloud container
secrets = modal.Secret.from_dict({
    "JWT_SECRET_KEY": "dev_secret_key_change_this_in_production_use_secrets_module",
    "ACCESS_TOKEN_EXPIRE_MINUTES": "60",
    "CORS_ORIGINS": "*",  # Temporarily allow all origins so Vercel can connect
    "LLM_PROVIDER": "groq",
    "GROQ_API_KEY": os.environ.get("GROQ_API_KEY", "YOUR_GROQ_API_KEY_HERE"),
    "GROQ_MODEL": "openai/gpt-oss-20b",
    
    # CRITICAL: Tell the app to look for the database in the mounted volume
    "BBQ_DATA_DIR": "/data",
    "BBQ_DB_PATH": "/data/bbq.db",
    "BBQ_DATASET_DIR": "/data"
})

# 5. Serve the FastAPI app using Modal's ASGI wrapper
@app.function(
    image=image,
    volumes={"/data": volume},
    secrets=[secrets],
)
@modal.asgi_app()
def fastapi_app():
    # We must import the app inside the function so it loads the cloud environment variables
    from app.main import app as web_app
    return web_app
