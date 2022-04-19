import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEV_CONFIG = "development"
TEST_CONFIG = "testing"
PRODUCTION_CONFIG = "production"
DEFAULT_CONFIG = "default"


class Config:
    SECRET_KEY = os.environ.get("BACKEND_SECRET_KEY") or "50m3r@nd0mh@rd2gu355t3xt"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("BACKEND_DATABASE_URI", "mysql://user:password@db/db")
    )


class TestConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("BACKEND_DATABASE_URI")
        or f"sqlite:///{os.path.join(BASE_DIR,'data-test.sqlite')}"
    )


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = (
      os.environ.get("BACKEND_DATABASE_URI", "mysql://user:password@db/db")
    )


config = {
    DEV_CONFIG: DevelopmentConfig,
    TEST_CONFIG: TestConfig,
    PRODUCTION_CONFIG: ProductionConfig,
    DEFAULT_CONFIG: DevelopmentConfig,
}
