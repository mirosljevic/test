from .loader import EnvironmentLoader

loader = EnvironmentLoader()

hosts = loader.load_module("hosts")
settings = loader.load_module("settings")
geofencing = loader.load_module("geofencing")
credentials = loader.load_module("credentials")
database = loader.load_module("database")

__all__ = [
    "hosts",
    "settings",
    "geofencing",
    "credentials",
    "database"
]
