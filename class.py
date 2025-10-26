class Smartphone:
    # --- 1. Constructor (__init__) ---
    def __init__(self, brand, model, storage_gb, battery_percent=100):
        # Public attributes
        self.brand = brand
        self.model = model
        
        # Protected attributes (Convention: use _ for attributes meant for internal use)
        self._storage = storage_gb
        self._battery = battery_percent
        self._is_locked = True
        
        print(f"[{brand}] New {model} initialized.")
    # --- 2. Methods (Behavior) ---
    
    def check_battery(self):
        """Returns the current battery level."""
        return f"{self.brand} {self.model} has {self._battery}% battery left."

    def lock_phone(self):
        """Locks the phone."""
        self._is_locked = True
        return f"Phone locked."

    def unlock_phone(self, passcode="1234"):
        """Attempts to unlock the phone (simple demonstration)."""
        if passcode == "1234":
            self._is_locked = False
            return "Phone unlocked successfully."
        else:
            return "Incorrect passcode. Phone remains locked."

    # A method that will be overridden (demonstrates Polymorphism later)
    def open_app(self, app_name):
        """Simulates opening a generic app."""
        if not self._is_locked:
            return f"Opening '{app_name}' on {self._default_os}."
        else:
            return "Cannot open app. Phone is locked."