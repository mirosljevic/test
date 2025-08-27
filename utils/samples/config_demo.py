from utils.config import get_config_var

print("Config Utilities Demo")
print("=" * 30)

print("Boolean config with default False:")
enable_debug = get_config_var("DEBUG_MODE", False)
print(f"DEBUG_MODE: {enable_debug}")

print("\nInteger config with default 30:")
timeout = get_config_var("API_TIMEOUT", 30)
print(f"API_TIMEOUT: {timeout}")

print("\nFloat config with default 1.5:")
retry_delay = get_config_var("RETRY_DELAY", 1.5)
print(f"RETRY_DELAY: {retry_delay}")

print("\nString config with default 'localhost':")
host = get_config_var("DATABASE_HOST", "localhost")
print(f"DATABASE_HOST: {host}")

print("\nTo test with environment variables, run:")
print("export DEBUG_MODE=true")
print("export API_TIMEOUT=60")
print("export RETRY_DELAY=2.0")
print("export DATABASE_HOST=prod-server")
print("python -m utils.samples.config_demo")
