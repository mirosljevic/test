import importlib
import os
from logger import log
from settings.environment import ENVIRONMENT


class ModuleWrapper:
    def __init__(self, module, module_name: str, environment: str):
        self._module = module
        self._module_name = module_name
        self._environment = environment

    def __getattr__(self, name: str):
        if hasattr(self._module, name):
            return getattr(self._module, name)
        else:
            log.warning(
                f"Property '{name}' not found in {self._module_name} for environment '{self._environment}'")
            return None

    def __dir__(self):
        return dir(self._module)


class EnvironmentLoader:
    def __init__(self):
        self._hosts = None
        self._settings = None
        self._environment = ENVIRONMENT
        log.debug(f"Environment set to: {self._environment}")

    def load_module(self, module_name: str):
        module_path = f"environment.envs.{self._environment}.{module_name}"

        try:
            module = importlib.import_module(module_path)
            log.debug(f"Successfully loaded {module_name} from {module_path}")
            return ModuleWrapper(module, module_name, self._environment)
        except ImportError as e:
            env_path = os.path.join(os.path.dirname(__file__), "envs", self._environment)
            if not os.path.exists(env_path):
                log.error(f"Environment '{self._environment}' does not exist. Available environments: "
                          f"{self._get_available_environments()}")
                raise ImportError

            module_file = os.path.join(env_path, f"{module_name}.py")
            if not os.path.exists(module_file):
                return None

            log.error(f"Failed to import {module_path}: {e}")
            raise ImportError

    @staticmethod
    def _get_available_environments():
        envs_path = os.path.join(os.path.dirname(__file__), "envs")
        if not os.path.exists(envs_path):
            return []

        environments = []
        for item in os.listdir(envs_path):
            item_path = os.path.join(envs_path, item)
            if os.path.isdir(item_path) and not item.startswith("."):
                environments.append(item)
        return environments
