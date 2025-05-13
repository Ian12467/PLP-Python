"""
Assignment 1: Design Your Own Class
This module implements a Smartphone class hierarchy with inheritance and encapsulation.
"""

class ElectronicDevice:
    """Base class for all electronic devices."""
    
    def __init__(self, brand, model, price):
        """Initialize an electronic device with basic attributes.
        
        Args:
            brand (str): The manufacturer of the device
            model (str): The model name/number
            price (float): The retail price in dollars
        """
        self.brand = brand
        self.model = model
        self.price = price
        self._power_status = False  # Private attribute for encapsulation
    
    def power_toggle(self):
        """Toggle the power status of the device."""
        self._power_status = not self._power_status
        status = "on" if self._power_status else "off"
        print(f"{self.brand} {self.model} is now powered {status}")
    
    def get_power_status(self):
        """Get the current power status.
        
        Returns:
            bool: True if powered on, False if powered off
        """
        return self._power_status
    
    def get_info(self):
        """Return basic information about the device.
        
        Returns:
            str: Device information
        """
        return f"{self.brand} {self.model} - ${self.price:.2f}"


class Smartphone(ElectronicDevice):
    """A smartphone class that inherits from ElectronicDevice."""
    
    def __init__(self, brand, model, price, screen_size, storage, os):
        """Initialize a smartphone with specific attributes.
        
        Args:
            brand (str): The manufacturer of the phone
            model (str): The model name/number
            price (float): The retail price in dollars
            screen_size (float): The screen size in inches
            storage (int): Storage capacity in GB
            os (str): Operating system name
        """
        # Call the parent class constructor
        super().__init__(brand, model, price)
        
        # Smartphone-specific attributes
        self.screen_size = screen_size
        self.storage = storage
        self.os = os
        self._battery_level = 100  # Private attribute
        self._apps = []  # Private attribute - list of installed apps
    
    def make_call(self, number):
        """Simulate making a phone call.
        
        Args:
            number (str): The phone number to call
        
        Returns:
            str: Call status message
        """
        if not self.get_power_status():
            return "Cannot make call: Phone is powered off"
        
        return f"Calling {number}..."
    
    def install_app(self, app_name):
        """Install an app on the smartphone.
        
        Args:
            app_name (str): Name of the app to install
            
        Returns:
            str: Installation status message
        """
        if app_name in self._apps:
            return f"{app_name} is already installed"
        
        self._apps.append(app_name)
        return f"{app_name} has been installed successfully"
    
    def get_installed_apps(self):
        """Get list of installed apps.
        
        Returns:
            list: List of installed app names
        """
        return self._apps
    
    def charge_battery(self, amount):
        """Charge the phone battery.
        
        Args:
            amount (int): Percentage to charge
            
        Returns:
            str: Charging status message
        """
        if self._battery_level + amount > 100:
            self._battery_level = 100
        else:
            self._battery_level += amount
        
        return f"Battery charged to {self._battery_level}%"
    
    def get_battery_level(self):
        """Get the current battery level.
        
        Returns:
            int: Battery level percentage
        """
        return self._battery_level
    
    def get_info(self):
        """Override the parent method to include smartphone-specific details.
        
        Returns:
            str: Detailed smartphone information
        """
        basic_info = super().get_info()
        return f"{basic_info}, {self.screen_size}\" screen, {self.storage}GB, {self.os}"


class GamingPhone(Smartphone):
    """A specialized smartphone designed for gaming."""
    
    def __init__(self, brand, model, price, screen_size, storage, os, 
                 gpu, refresh_rate, cooling_system):
        """Initialize a gaming phone with gaming-specific attributes.
        
        Args:
            brand (str): The manufacturer of the phone
            model (str): The model name/number
            price (float): The retail price in dollars
            screen_size (float): The screen size in inches
            storage (int): Storage capacity in GB
            os (str): Operating system name
            gpu (str): Graphics processor model
            refresh_rate (int): Screen refresh rate in Hz
            cooling_system (str): Type of cooling system
        """
        # Call the parent class constructor
        super().__init__(brand, model, price, screen_size, storage, os)
        
        # Gaming phone specific attributes
        self.gpu = gpu
        self.refresh_rate = refresh_rate
        self.cooling_system = cooling_system
        self._gaming_mode = False
        self._game_library = []
    
    def toggle_gaming_mode(self):
        """Toggle gaming mode on/off.
        
        Returns:
            str: Status message
        """
        self._gaming_mode = not self._gaming_mode
        status = "enabled" if self._gaming_mode else "disabled"
        return f"Gaming mode {status}"
    
    def add_game(self, game_name):
        """Add a game to the library.
        
        Args:
            game_name (str): Name of the game
            
        Returns:
            str: Status message
        """
        if game_name in self._game_library:
            return f"{game_name} is already in your library"
        
        self._game_library.append(game_name)
        return f"{game_name} added to your game library"
    
    def get_game_library(self):
        """Get the list of games in the library.
        
        Returns:
            list: List of game names
        """
        return self._game_library
    
    def get_info(self):
        """Override to include gaming phone specific details.
        
        Returns:
            str: Detailed gaming phone information
        """
        smartphone_info = super().get_info()
        return f"{smartphone_info}, {self.gpu} GPU, {self.refresh_rate}Hz refresh rate, {self.cooling_system} cooling"


# Demonstration
if __name__ == "__main__":
    # Create a regular smartphone
    iphone = Smartphone("Apple", "iPhone 15", 999.99, 6.1, 256, "iOS")
    iphone.power_toggle()  # Turn it on
    print(iphone.get_info())
    print(iphone.install_app("Instagram"))
    print(iphone.install_app("Twitter"))
    print(f"Installed apps: {', '.join(iphone.get_installed_apps())}")
    print(iphone.make_call("555-123-4567"))
    print(iphone.charge_battery(20))
    print(f"Battery level: {iphone.get_battery_level()}%")
    print()
    
    # Create a gaming phone
    rog_phone = GamingPhone("ASUS", "ROG Phone 7", 1299.99, 6.8, 512, "Android", 
                           "Adreno 740", 165, "Vapor Chamber")
    rog_phone.power_toggle()  # Turn it on
    print(rog_phone.get_info())
    print(rog_phone.toggle_gaming_mode())
    print(rog_phone.add_game("Call of Duty Mobile"))
    print(rog_phone.add_game("Genshin Impact"))
    print(f"Game library: {', '.join(rog_phone.get_game_library())}")
    print(f"Battery level: {rog_phone.get_battery_level()}%")
    print(rog_phone.charge_battery(10))