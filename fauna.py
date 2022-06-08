from faunadb.client import FaunaClient
from dynaconf import LazySettings

config = LazySettings(
    environments=True,
    settings_files=["config.toml"],
)


def get_fauna_client():
    return FaunaClient(
        secret=config["FAUNA_SECRET"],
        domain="db.us.fauna.com",
        port=443,
        scheme="https"
    )
