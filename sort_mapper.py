import sys

# Mapper for sorting: swap key and value
def mapper():
    for line in sys.stdin:
        company, count = line.strip().split("\t")
        print(f"{count}\t{company}")
        
if __name__ == "__main__":
    mapper()
