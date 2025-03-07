import sys

# Reducer function to output sorted trip counts
def reducer():
    # List to hold (count, company) tuples
    data = []
    
    # Read input from stdin and collect data
    for line in sys.stdin:
        count, company = line.strip().split("\t")
        data.append((int(count), company))  # Convert count to integer for sorting
    
    # Sort data by company name or trip count (optional)
    data.sort(key=lambda x: x[0])  # Sort by company name (x[1])
    
    # Output sorted data
    for count, company in data:
        print(f"{company}\t{count}")
        
if __name__ == "__main__":
    reducer()
