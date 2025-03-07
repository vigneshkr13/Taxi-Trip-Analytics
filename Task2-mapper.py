#!/usr/bin/env python

import sys
from math import sqrt

# Function to get initial medoids from initialization.txt
def getMedoids(filepath):
    medoids = []
    with open(filepath) as fp:
        lines = fp.readlines()
        for line in lines[1:]:  # skip the first line (number of iterations)
            cord = line.strip().split()
            medoids.append([float(cord[0]), float(cord[1])])
    return medoids

# Function to create clusters based on medoids
def createClusters(medoids):
    for line in sys.stdin:
        loc = line.strip().split(',')
        dropoff_x, dropoff_y =  float(loc[6]), float(loc[7])
        # print("droppoff_x",dropoff_x)

        # Initialize min distance
        min_dist = float('inf')
        closest_medoid_index = -1

        # Find the closest medoid
        for i, medoid in enumerate(medoids):
            dist = sqrt((dropoff_x - medoid[0])**2 + (dropoff_y - medoid[1])**2)
            if dist < min_dist:
                min_dist = dist
                closest_medoid_index = i

        # Emit the medoid index and the point
        print(f"{closest_medoid_index}\t{dropoff_x}\t{dropoff_y}")

if __name__ == "__main__":
    medoids = getMedoids('centroids.txt')
    createClusters(medoids)
