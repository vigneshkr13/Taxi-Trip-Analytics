import sys

# Reducer function to count trips per company
def reducer():
    current_company = None
    trip_count = 0
    
    for line in sys.stdin:
        company, count = line.strip().split("\t")
        
        if company != current_company:
            if current_company:
                print(f"{current_company}\t{trip_count}")
            current_company = company
            trip_count = 0
        
        trip_count += int(count)
    
    if current_company:
        print(f"{current_company}\t{trip_count}")

if __name__ == "__main__":
    reducer()
