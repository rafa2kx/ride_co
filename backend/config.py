import os
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://user:password@localhost:5432/grocery_list'
    )
    JWT_SECRET_KEY = os.getenv(
        'JWT_SECRET_KEY',
        'one_really_stupid_secret_key_for_testing_purposes_1234567890abcdef1234567890abcdef'
    )
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600 * 24 * 30))  # 30 days