#!/usr/bin/env python3
import sys

current_taxi_id = None
current_trip_type = None
total_trips = 0
total_fare_sum = 0
max_fare = float('-inf')
min_fare = float('inf')

for line in sys.stdin:
    line = line.strip()
    taxi_id,trip_type, count, max_f, min_f, avg_f = line.split(',')
    
    count = int(count)
    max_f = float(max_f)
    min_f = float(min_f)
    avg_f = float(avg_f)
    
    if current_taxi_id == taxi_id and current_trip_type == trip_type:
        # Same taxi_id and trip_type, aggregate results
        total_trips += count
        total_fare_sum += avg_f * count
        max_fare = max(max_fare, max_f)
        min_fare = min(min_fare, min_f)
    else:
        # Output the results for the previous taxi_id and trip_type
        if current_taxi_id:
            final_avg_fare = total_fare_sum / total_trips
            print(f"{current_taxi_id}, {current_trip_type}, {total_trips}, {max_fare:.2f}, {min_fare:.2f}, {final_avg_fare:.2f}")

        
        # Reset for the new taxi_id and trip_type
        current_taxi_id = taxi_id
        current_trip_type = trip_type
        total_trips = count
        total_fare_sum = avg_f * count
        max_fare = max_f
        min_fare = min_f

# Print the last taxi's result
if current_taxi_id:
    final_avg_fare = total_fare_sum / total_trips
    # Format the fare values to 2 decimal places
    print(f"{current_taxi_id}, {current_trip_type}, {total_trips}, {max_fare:.2f}, {min_fare:.2f}, {final_avg_fare:.2f}")
