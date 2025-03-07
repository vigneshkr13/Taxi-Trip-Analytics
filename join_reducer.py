import sys

current_taxi_id = None
taxi_info = None
trips = []

# Process each line from standard input
for line in sys.stdin:
    line = line.strip()
    
    # Split the line into taxi_id, record type, and data
    try:
        taxi_id, record_type, data = line.split("\t", 2)
    except ValueError:
        continue  # Skip lines that don't have enough fields
    
    if taxi_id != current_taxi_id:
        # If we encounter a new taxi_id, process the previous one
        if current_taxi_id is not None:
            # Join trips with taxi_info for the previous taxi_id
            if taxi_info:
                for trip in trips:
                    print(f"{current_taxi_id}\t{taxi_info}\t{trip}")
        
        # Reset for the new taxi_id
        current_taxi_id = taxi_id
        taxi_info = None
        trips = []
    
    # Update the current taxi_id
    if record_type == "TAXI":
        taxi_info = data  # Store taxi information (company, etc.)
    elif record_type == "TRIP":
        trips.append(data)  # Collect all trips for this taxi_id

# Don't forget to output the last taxi_id's data
if current_taxi_id and taxi_info:
    for trip in trips:
        print(f"{current_taxi_id}\t{taxi_info}\t{trip}")
