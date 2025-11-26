from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str
    admin_email: str
    items_per_user: int = 50

settings = Settings()
print(settings.app_name)