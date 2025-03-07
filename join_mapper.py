import sys

# Mapper function to process both files
def mapper():
    for line in sys.stdin:
        data = line.strip().split(',')
        
        if len(data) == 8:  # It's from Trips.txt
            trip_id, taxi_id, fare, distance, pickup_x, pickup_y, dropoff_x, dropoff_y = data
            print(f"{taxi_id}\tTRIP\t{trip_id}")
        
        elif len(data) == 4:  # It's from Taxis.txt
            taxi_id, company, model, year = data
            print(f"{taxi_id}\tTAXI\t{company}")
            
if __name__ == "__main__":
    mapper()
