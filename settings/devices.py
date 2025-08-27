from utils.config import get_config_var

# Get current device from environment variable or default to desktop
CURRENT_DEVICE = get_config_var("DEVICE", default="chrome")

# Device configurations with Playwright context options
DEVICES = {
    # Desktop browsers
    "chrome": {
        "viewport": {"width": 1920, "height": 1080},
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "device_scale_factor": 1,
        "is_mobile": False,
        "has_touch": False,
        "record_video_size": {"width": 1280, "height": 720}
    },
    
    "firefox": {
        "viewport": {"width": 1920, "height": 1080},
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/120.0",
        "device_scale_factor": 1,
        "is_mobile": False,
        "has_touch": False,
        "record_video_size": {"width": 1280, "height": 720}
    },
    
    "safari": {
        "viewport": {"width": 1920, "height": 1080},
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15",
        "device_scale_factor": 1,
        "is_mobile": False,
        "has_touch": False,
        "record_video_size": {"width": 1280, "height": 720}
    },
    
    # Mobile devices
    "iphone_13": {
        "viewport": {"width": 390, "height": 844},
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "record_video_size": {"width": 390, "height": 844}
    },
    
    "iphone_13_pro": {
        "viewport": {"width": 393, "height": 852},
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "record_video_size": {"width": 393, "height": 852}
    },
    
    "samsung_galaxy_s21": {
        "viewport": {"width": 360, "height": 800},
        "user_agent": "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
        "device_scale_factor": 3,
        "is_mobile": True,
        "has_touch": True,
        "record_video_size": {"width": 360, "height": 800}
    },
    
    # Tablets
    "ipad_air": {
        "viewport": {"width": 820, "height": 1180},
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "device_scale_factor": 2,
        "is_mobile": False,  # iPad Air should be treated as desktop due to larger viewport  
        "has_touch": True,
        "record_video_size": {"width": 820, "height": 1180}
    },
    
    "ipad_pro": {
        "viewport": {"width": 1024, "height": 1366},
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "device_scale_factor": 2,
        "is_mobile": False,  # iPad Pro should be treated as desktop due to larger viewport
        "has_touch": True,
        "record_video_size": {"width": 1024, "height": 1366}
    },
    
    "samsung_galaxy_tab": {
        "viewport": {"width": 768, "height": 1024},
        "user_agent": "Mozilla/5.0 (Linux; Android 11; SM-T870) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "device_scale_factor": 2,
        "is_mobile": True,
        "has_touch": True,
        "record_video_size": {"width": 768, "height": 1024}
    }
}


def get_device_config(device_name: str = None) -> dict:
    """
    Get device configuration by name.
    
    Args:
        device_name: Name of the device configuration to retrieve
        
    Returns:
        Device configuration dictionary
        
    Raises:
        ValueError: If device_name is not found in DEVICES
    """
    if device_name is None:
        # Use the device specified in DEVICE environment variable
        device_name = CURRENT_DEVICE
    
    if device_name not in DEVICES:
        available_devices = ", ".join(DEVICES.keys())
        raise ValueError(f"Device '{device_name}' not found. Available devices: {available_devices}")
    
    return DEVICES[device_name].copy()


def get_current_device_config() -> dict:
    """Get the current device configuration based on environment variables."""
    return get_device_config()


def is_mobile_device(device_name: str = None) -> bool:
    """Check if the specified device (or current device) is mobile."""
    config = get_device_config(device_name)
    return config.get("is_mobile", False)


def list_available_devices() -> list:
    """Get list of all available device names."""
    return list(DEVICES.keys())


def get_devices_by_type(device_type: str) -> list:
    """
    Get devices filtered by type.
    
    Args:
        device_type: 'desktop', 'mobile', or 'tablet'
        
    Returns:
        List of device names matching the type
    """
    if device_type == "desktop":
        return [name for name, config in DEVICES.items() if not config.get("is_mobile", False)]
    elif device_type == "mobile":
        return [name for name, config in DEVICES.items() 
                if config.get("is_mobile", False) and config.get("viewport", {}).get("width", 0) < 500]
    elif device_type == "tablet":
        return [name for name, config in DEVICES.items() 
                if config.get("is_mobile", False) and config.get("viewport", {}).get("width", 0) >= 500]
    else:
        raise ValueError(f"Invalid device_type: {device_type}. Use 'desktop', 'mobile', or 'tablet'")
