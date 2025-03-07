import sys

# Mapper function for counting trips per company
def mapper():
    for line in sys.stdin:
        company = line.strip().split("\t")[1]
        print(f"{company}\t1")
        
if __name__ == "__main__":
    mapper()
