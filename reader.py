__authors__ = "Vaggelis Malandrakis, Kleio Fragkedaki"

def getCentroids(filepath):
    centroids = []
    with open(filepath) as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip the first line
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                try:
                    x, y = map(float, parts[:2])
                    centroids.append((x, y))
                except ValueError as e:
                    print(f"Error processing line: {line}. {e}", file=sys.stderr)
                    continue
    return centroids

# Function to check if the centroids have converged (within a threshold)
def checkCentroidsDistance(centroids, centroids1):
    threshold = 1.0  # Convergence threshold

    for i in range(len(centroids)):
        x_diff = abs(centroids[i][0] - centroids1[i][0]) < threshold
        y_diff = abs(centroids[i][1] - centroids1[i][1]) < threshold

        # If any centroid's x or y difference is greater than the threshold, they haven't converged
        if not (x_diff and y_diff):
            print(0)
            return

    # If all centroids' differences are within the threshold, print 1 (indicating convergence)
    print(1)

if __name__ == "__main__":
    # Read the current centroids and the previous centroids
    centroids = getCentroids('centroids.txt')     # Current centroids
    centroids1 = getCentroids('centroids1.txt')   # Previous centroids

    # Check if centroids have converged
    checkCentroidsDistance(centroids, centroids1)
