"""
Activity 2: Polymorphism Challenge
This module demonstrates polymorphism with different vehicle classes
implementing the same method differently.
"""

class Vehicle:
    """Base class for all vehicles."""
    
    def __init__(self, make, model, year, color):
        """Initialize a vehicle with basic attributes.
        
        Args:
            make (str): The manufacturer of the vehicle
            model (str): The model name
            year (int): The manufacturing year
            color (str): The color of the vehicle
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def move(self):
        """Base move method - to be overridden by child classes."""
        return "The vehicle is moving"
    
    def get_info(self):
        """Get basic vehicle information.
        
        Returns:
            str: Vehicle information
        """
        return f"{self.year} {self.color} {self.make} {self.model}"


class Car(Vehicle):
    """A car that inherits from Vehicle."""
    
    def __init__(self, make, model, year, color, num_doors, fuel_type):
        """Initialize a car with specific attributes.
        
        Args:
            make (str): The manufacturer of the car
            model (str): The model name
            year (int): The manufacturing year
            color (str): The color of the car
            num_doors (int): Number of doors
            fuel_type (str): Type of fuel used
        """
        super().__init__(make, model, year, color)
        self.num_doors = num_doors
        self.fuel_type = fuel_type
    
    def move(self):
        """Override the move method for cars.
        
        Returns:
            str: Car movement description
        """
        return f"🚗 Driving on the road with {self.num_doors} doors"
    
    def honk(self):
        """Car-specific method.
        
        Returns:
            str: Honking sound
        """
        return "Beep beep!"


class Plane(Vehicle):
    """A plane that inherits from Vehicle."""
    
    def __init__(self, make, model, year, color, wingspan, max_altitude):
        """Initialize a plane with specific attributes.
        
        Args:
            make (str): The manufacturer of the plane
            model (str): The model name
            year (int): The manufacturing year
            color (str): The color of the plane
            wingspan (float): The wingspan in meters
            max_altitude (int): Maximum flying altitude in feet
        """
        super().__init__(make, model, year, color)
        self.wingspan = wingspan
        self.max_altitude = max_altitude
    
    def move(self):
        """Override the move method for planes.
        
        Returns:
            str: Plane movement description
        """
        return f"✈️ Flying through the air at {self.max_altitude} feet"
    
    def take_off(self):
        """Plane-specific method.
        
        Returns:
            str: Take-off description
        """
        return "Taking off from the runway!"


class Boat(Vehicle):
    """A boat that inherits from Vehicle."""
    
    def __init__(self, make, model, year, color, boat_type, length):
        """Initialize a boat with specific attributes.
        
        Args:
            make (str): The manufacturer of the boat
            model (str): The model name
            year (int): The manufacturing year
            color (str): The color of the boat
            boat_type (str): Type of boat (e.g., sailboat, yacht)
            length (float): Length of the boat in feet
        """
        super().__init__(make, model, year, color)
        self.boat_type = boat_type
        self.length = length
    
    def move(self):
        """Override the move method for boats.
        
        Returns:
            str: Boat movement description
        """
        return f"🚢 Sailing across the water with {self.length} feet length"
    
    def anchor(self):
        """Boat-specific method.
        
        Returns:
            str: Anchoring description
        """
        return "Dropping anchor!"


class Submarine(Vehicle):
    """A submarine that inherits from Vehicle."""
    
    def __init__(self, make, model, year, color, max_depth, crew_capacity):
        """Initialize a submarine with specific attributes.
        
        Args:
            make (str): The manufacturer of the submarine
            model (str): The model name
            year (int): The manufacturing year
            color (str): The color of the submarine
            max_depth (int): Maximum diving depth in meters
            crew_capacity (int): Maximum number of crew members
        """
        super().__init__(make, model, year, color)
        self.max_depth = max_depth
        self.crew_capacity = crew_capacity
    
    def move(self):
        """Override the move method for submarines.
        
        Returns:
            str: Submarine movement description
        """
        return f"🌊 Diving underwater to a depth of {self.max_depth} meters"
    
    def surface(self):
        """Submarine-specific method.
        
        Returns:
            str: Surfacing description
        """
        return "Surfacing to periscope depth!"


# Demonstration of polymorphism
if __name__ == "__main__":
    # Create different vehicle objects
    sedan = Car("Toyota", "Camry", 2023, "Blue", 4, "Hybrid")
    jet = Plane("Boeing", "747", 2020, "White", 68.4, 35000)
    yacht = Boat("Sea Ray", "Sundancer", 2022, "White", "Yacht", 40)
    sub = Submarine("General Dynamics", "Virginia Class", 2019, "Black", 800, 135)
    
    # Create a list of vehicles
    vehicles = [sedan, jet, yacht, sub]
    
    # Demonstrate polymorphism by calling the same method on different objects
    print("Demonstrating Polymorphism with Vehicle.move():")
    print("-" * 50)
    
    for vehicle in vehicles:
        print(f"{vehicle.get_info()}:")
        print(f"  {vehicle.move()}")
    
    print("\nDemonstrating vehicle-specific methods:")
    print("-" * 50)
    print(f"Car: {sedan.honk()}")
    print(f"Plane: {jet.take_off()}")
    print(f"Boat: {yacht.anchor()}")
    print(f"Submarine: {sub.surface()}")