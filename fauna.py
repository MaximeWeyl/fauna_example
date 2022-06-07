from faunadb.client import FaunaClient


from dynaconf import Dynaconf
from dynaconf.constants import EXTS

DEFAULT_SETTINGS_FILES = [f"config.{ext}" for ext in EXTS] + [
    f".secrets.{ext}" for ext in EXTS
]

config =  Dynaconf(
    # This global `settings` is deprecated from v3.0.0+
    # kept here for backwards compatibility
    # To Be Removed in 4.0.x
    warn_dynaconf_global_settings=True,
    environments=True,
    lowercase_read=False,
    load_dotenv=True,
    settings_files=DEFAULT_SETTINGS_FILES,
    envvar_prefix='NOUNOUTOP',
)


def get_fauna_client():
    return FaunaClient(
        secret=config["FAUNA_SECRET"],
        domain="db.us.fauna.com",
        port=443,
        scheme="https"
    )
