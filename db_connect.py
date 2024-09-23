import os
from dotenv import load_dotenv

# Esta función Automaticamente .env
load_dotenv()

database_url = os.getenv('DATABASE_URL')
secret_key = os.getenv('SECRET_KEY')
debug = os.getenv('DEBUG')

print(f"Database URL: {database_url}")
print(f"Secret key: {secret_key}")
print(f"Debug: {debug}")


