# UI Testing Framework 🖥️

Advanced UI testing framework with device-aware page objects, layout detection, cross-platform compatibility, and comprehensive component architecture.

## Overview

The UI framework provides robust browser automation testing with intelligent device detection, layout-aware components, and seamless cross-platform compatibility for desktop, tablet, and mobile testing.

## Key Features

- **Device-Aware Testing**: Automatic layout detection (mobile/tablet/desktop)
- **Page Object Model**: Enhanced component-based architecture
- **Cross-Platform**: Unified testing across all device types
- **Layout Intelligence**: Components adapt to different UI layouts
- **Multi-Tenant Support**: Kansas, Catalyst, and other tenant configurations
- **Playwright Integration**: Modern browser automation with Playwright

## Architecture

```
ui/
├── facade/                 # High-level UI facades
│   ├── player_facade.py   # Player UI facade
│   └── features/          # Feature-specific facades
├── pages/                 # Page object model
│   ├── base.py           # Base page and component classes
│   ├── elements/         # UI elements (buttons, inputs, etc.)
│   └── platforms/        # Platform-specific pages
└── samples/              # Usage examples and samples
```

## Layout Detection System

### Automatic Layout Detection
The framework automatically detects and adapts to three layout types:

```python
class BasePage:
    @property
    def layout(self) -> str:
        """Determine layout: mobile, tablet, or desktop"""
        # Check context flags
        if hasattr(self.page.context, '_is_tablet') and self.page.context._is_tablet:
            return 'tablet'
        if hasattr(self.page.context, '_is_mobile') and self.page.context._is_mobile:
            return 'mobile'
        
        # Fallback to viewport detection
        viewport = self.page.viewport_size
        if viewport['width'] <= 768:
            return 'mobile'
        elif viewport['width'] <= 1024:
            return 'tablet'
        else:
            return 'desktop'
```

### Layout-Specific Components
```python
class UserControls(BaseComponent):
    def register(self):
        """Register with layout-aware logic."""
        layout = self.layout
        
        if layout == 'mobile':
            # Use hamburger menu
            self.mobile_menu.hamburger_button.click()
            self.mobile_menu.register_button.click()
        elif layout == 'tablet':
            # Try direct button, fallback to hamburger
            try:
                self.register_button.click()
            except TimeoutError:
                self.mobile_menu.hamburger_button.click()
                self.mobile_menu.register_button.click()
        else:  # desktop
            # Direct button access
            self.register_button.click()
```

## Page Object Model

### Enhanced Base Components
```python
class BaseComponent:
    def __init__(self, page, instance=None, **kwargs):
        self.page = page
        self.parent = instance.locator if instance else page
        
        # Device detection
        self.is_mobile = self._detect_mobile()
        self.is_tablet = self._detect_tablet()
        self.layout = self._get_layout()
        
        # Tenant detection
        self.tenant = settings.tenant.lower()
        self.is_kansas = self.tenant == 'kansas'
    
    @property
    def layout(self) -> str:
        """Get current layout type."""
        return self._get_layout()
    
    def _get_layout(self) -> str:
        """Determine layout based on context and viewport."""
        if self.is_mobile:
            return 'mobile'
        elif self.is_tablet:
            return 'tablet'
        else:
            return 'desktop'
```

### Smart Selectors
Components automatically choose appropriate selectors based on context:

```python
class BaseComponent:
    def set_selectors(self, default_selector=None, mobile_selector=None, 
                      kansas_selector=None, **kwargs):
        self.selectors = {
            "default": default_selector,
            "mobile": mobile_selector or default_selector,
            "kansas": kansas_selector or default_selector,
            "kansas_mobile": kwargs.get('kansas_mobile_selector', mobile_selector)
        }
    
    @property
    def selector(self) -> str:
        """Choose appropriate selector based on context."""
        if self.is_kansas:
            if self.is_mobile:
                return self.selectors['kansas_mobile']
            else:
                return self.selectors['kansas']
        else:
            if self.is_mobile:
                return self.selectors['mobile']
            else:
                return self.selectors['default']
```

## Usage Examples

### Basic Page Test
```python
def test_home_page_loads(visitor):
    """Test home page loads correctly."""
    visitor.ui.open()
    
    assert visitor.ui.home_page.is_displayed()
    assert visitor.ui.home_page.layout in ['mobile', 'tablet', 'desktop']
```

### Cross-Device Registration
```python
@pytest.mark.parametrize("device", ["desktop", "ipad_air", "iphone_12"])
def test_player_registration(visitor, device):
    """Test registration across different devices."""
    os.environ['DEVICE'] = device
    
    visitor.ui.open()
    result = visitor.ui.registration.register()
    
    assert result.success
    assert "Welcome" in result.message
    
    # Layout-specific assertions
    layout = visitor.ui.home_page.layout
    if layout == 'mobile':
        assert visitor.ui.home_page.mobile_menu.is_displayed()
    else:
        assert visitor.ui.home_page.user_controls.is_displayed()
```

### Layout-Aware Testing
```python
def test_navigation_adapts_to_layout(visitor):
    """Test navigation adapts to different layouts."""
    visitor.ui.open()
    
    layout = visitor.ui.home_page.layout
    
    if layout == 'mobile':
        # Mobile uses hamburger menu
        assert visitor.ui.home_page.mobile_menu.hamburger_button.is_displayed()
        visitor.ui.home_page.mobile_menu.hamburger_button.click()
        assert visitor.ui.home_page.mobile_menu.menu_items.is_displayed()
    else:
        # Desktop/tablet use top navigation
        assert visitor.ui.home_page.top_menu.is_displayed()
        visitor.ui.home_page.top_menu.games_link.click()
```

## Device Configuration

### Supported Devices
```python
# settings/devices.py
DEVICES = {
    'desktop': {
        'viewport': {'width': 1280, 'height': 720},
        'user_agent': 'Desktop Browser',
        'is_mobile': False,
        'is_tablet': False
    },
    'ipad_pro': {
        'viewport': {'width': 1024, 'height': 1366},
        'user_agent': 'iPad',
        'is_mobile': False,
        'is_tablet': True
    },
    'ipad_air': {
        'viewport': {'width': 820, 'height': 1180},
        'user_agent': 'iPad',
        'is_mobile': False,
        'is_tablet': True
    },
    'iphone_12': {
        'viewport': {'width': 390, 'height': 844},
        'user_agent': 'iPhone',
        'is_mobile': True,
        'is_tablet': False
    }
}
```

### Device Context Creation
```python
class PlayerFacade:
    def create_context(self):
        """Create browser context with device configuration."""
        device_config = get_device_config(os.environ.get('DEVICE', 'desktop'))
        
        context = self.browser.new_context(
            viewport=device_config['viewport'],
            user_agent=device_config['user_agent']
        )
        
        # Set device flags for layout detection
        context._is_mobile = device_config['is_mobile']
        context._is_tablet = device_config['is_tablet']
        
        return context
```

## Component Types

### UI Elements
```python
class Button(BaseComponent):
    def click(self):
        """Click button with proper waiting."""
        self.wait_for()
        self.locator.click()
        log.debug(f"{self.display_name} successfully clicked")

class InputField(BaseComponent):
    def fill(self, value: str):
        """Fill input field with value."""
        self.wait_for()
        self.locator.fill(value)
        log.debug(f"Filled {self.display_name} with: {value}")

class Dropdown(BaseComponent):
    def select(self, value: str):
        """Select option from dropdown."""
        self.wait_for()
        self.locator.select_option(value=value)
```

### Complex Components
```python
class UserControls(BaseComponent):
    @locator(Button, data_test_id="pc-register-button")
    def register_button(self): pass
    
    @locator(Button, data_test_id="pc-login-button") 
    def login_button(self): pass
    
    def get_user_details(self) -> dict:
        """Get user account details with layout awareness."""
        layout = self.layout
        
        if layout == 'mobile':
            # Mobile: access via hamburger menu
            self.mobile_menu.hamburger_button.click()
            return self._extract_mobile_user_details()
        elif layout == 'tablet':
            # Tablet: try desktop approach, fallback to mobile
            try:
                return self._extract_desktop_user_details()
            except:
                return self._extract_mobile_user_details()
        else:
            # Desktop: direct access
            return self._extract_desktop_user_details()
```

## Advanced Features

### Wait Strategies
```python
class BaseComponent:
    def wait_for(self, timeout=10000, state='visible'):
        """Wait for component with proper error handling."""
        try:
            self.locator.wait_for(state=state, timeout=timeout)
            log.debug(f"{self.display_name} is {state}")
        except Exception as e:
            log.error(f"Failed to wait for {self.display_name}: {e}")
            raise
    
    def wait_for_text(self, text: str, timeout=10000):
        """Wait for specific text to appear."""
        self.locator.wait_for(state='visible', timeout=timeout)
        expect(self.locator).to_contain_text(text, timeout=timeout)
```

### Error Handling
```python
class ComponentNotFoundException(Exception):
    def __init__(self, component_name: str, selector: str):
        self.component_name = component_name
        self.selector = selector
        super().__init__(f"Component '{component_name}' not found with selector '{selector}'")

class BaseComponent:
    def is_displayed(self, timeout=3000) -> bool:
        """Check if component is displayed without throwing exception."""
        try:
            self.wait_for(timeout=timeout)
            return True
        except:
            return False
```

## Testing Patterns

### Page Flows
```python
class RegistrationFlow:
    def __init__(self, facade: PlayerFacade):
        self.facade = facade
    
    def complete_registration(self, player: Player) -> bool:
        """Complete full registration flow."""
        # Step 1: Open registration
        self.facade.home_page.user_controls.register_button.click()
        
        # Step 2: Fill registration form
        self.facade.registration_page.email_field.fill(player.email)
        self.facade.registration_page.submit_button.click()
        
        # Step 3: Verify email
        verification_link = self.facade.email_client.get_verification_link()
        self.facade.page.goto(verification_link)
        
        # Step 4: Complete profile
        self.facade.registration_page.complete_profile(player)
        
        return self.facade.home_page.is_logged_in()
```

### Data-Driven Testing
```python
@pytest.mark.parametrize("player_data", [
    PlayerFactory.build(state="KS"),
    PlayerFactory.build(state="CA"), 
    PlayerFactory.build(age=21),
    PlayerFactory.build(age=65)
])
def test_registration_with_various_data(visitor, player_data):
    """Test registration with different player data."""
    visitor.player = player_data
    
    visitor.ui.open()
    result = visitor.ui.registration.register()
    
    assert result.success
    assert visitor.ui.account.get_email() == player_data.email
```

## Best Practices

1. **Layout Awareness**: Always consider mobile/tablet/desktop differences
2. **Wait Strategies**: Use appropriate waits for dynamic content
3. **Error Handling**: Implement graceful error handling
4. **Selector Strategy**: Use data-test-id attributes when possible
5. **Component Isolation**: Keep components focused and reusable
6. **Device Testing**: Test across all supported devices
7. **Clean Architecture**: Maintain separation of concerns

## Integration

The UI framework integrates with:
- **Actors**: High-level test personas
- **Data Factory**: Test data generation  
- **Email Service**: Email verification workflows
- **Database**: Data validation
- **Dashboard**: Real-time monitoring
- **Settings**: Device and environment configuration
