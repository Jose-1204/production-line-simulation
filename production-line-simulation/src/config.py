NUM_PRODUCTS = 200          # how many parts I'm going to simulate
STATION_NAMES = ["Cutting", "Drilling", "Assembly", "Painting"]

# average processing time (in minutes) for each station
MEAN_PROCESS_TIMES = [2.0, 3.0, 5.0, 4.0]

# standard deviation for the processing times (just to add some variation)
STD_PROCESS_TIMES = [0.3, 0.4, 0.7, 0.5]

# planned shift duration (in minutes)
PLANNED_TIME_MIN = 8 * 60   # 8 hours
