# Application Settings
APP_TITLE = "Dynex | MVRP Demo"
MAIN_HEADER = "Multi Vehicle Routing Problem"

# Shows/hides Quantum Hybrid vs Classical cost comparison in the
# results tab when both are run with the same settings.
SHOW_COST_COMPARISON = False

# Units will be in miles if true, meters if false
# If updated, make sure units match COST_LABEL below
UNITS_IMPERIAL = False
COST_LABEL = "Distance (m)"  # Either "Distance (m)" or specific distance cost description
THEME_COLOR = "#1d232f"
THEME_COLOR_SECONDARY = "#1d232f"
ADDRESS = "Wenlock Road, London, N1 7GU, United Kingdom"        # roughly the center of London
DISTANCE = 1700  # bounding box distance (in meters) around address
THUMBNAIL = "assets/logo.svg"
DESCRIPTION = """\
Run the Multi Vehicle Routing Problem (MVRP) problem for several different scenarios. Select
between delivery drones (flight path) and trucks (roads), the number of vehicles and client
locations.
"""

DEPOT_LABEL = "Depot"  # Either "Depot" or specific start location
LOCATIONS_LABEL = "Locations"  # Either "Locations" or business specific location type
RESOURCES = ["Water", "Food", "Other"]  # Supports any number of resources

#######################################
# Sliders, buttons and option entries #
#######################################

# number of vehicles slider (value means default)
NUM_VEHICLES = {
    "min": 1,
    "max": 10,
    "step": 1,
    "value": 4,
}

# number of client locations slider (value means default)
NUM_CLIENT_LOCATIONS = {
    "min": 10,
    "max": 100,
    "step": 1,
    "value": 60,
}

# solver time limits in seconds (value means default)
SOLVER_TIME = {
    "min": 10,
    "max": 300,
    "step": 5,
    "value": 10,
}
