#!/usr/bin/env python3
import sys

# Dictionary to store intermediate results with Taxi# as the key
trip_data = {}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    # Split the line into fields
    fields = line.split(',')
    
    # Check if this is a Trips.txt line
    if len(fields) == 8:
        trip_id, taxi_id, fare, distance = fields[0], fields[1], float(fields[2]), float(fields[3])
        
        # Categorize the trip based on distance
        if distance >= 200:
            trip_type = "long"
        elif distance >= 100:
            trip_type = "medium"
        else:
            trip_type = "short"
        
        # Initialize the taxi_id entry if not present
        if taxi_id not in trip_data:
            trip_data[taxi_id] = {"long": [], "medium": [], "short": []}
        
        # Append the fare to the appropriate trip type
        trip_data[taxi_id][trip_type].append(fare)

# Emit the results for each taxi
for taxi_id, trip_types in trip_data.items():
    for trip_type, fares in trip_types.items():
        if fares:
            total_trips = len(fares)
            max_fare = max(fares)
            min_fare = min(fares)
            avg_fare = sum(fares) / total_trips
            print(f"{taxi_id},{trip_type},{total_trips},{max_fare},{min_fare},{avg_fare}")
