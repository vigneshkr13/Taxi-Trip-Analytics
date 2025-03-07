#!/usr/bin/env python

import sys
import math

# Function to compute the sum of Euclidean distances from all points to the given medoid
def compute_total_distance(points_list, medoid_point):
    total_distance = 0
    for point in points_list:
        total_distance += compute_euclidean(point, medoid_point)
    return total_distance

# Function to compute Euclidean distance between two points
def compute_euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Reducer function to find the best medoid
def find_best_medoid():
    active_medoid = None
    cluster_points = []

    # Process each line from the mapper
    for record in sys.stdin:
        medoid_id, x_coord, y_coord = record.strip().split('\t')
        x_coord, y_coord = float(x_coord), float(y_coord)

        if active_medoid == medoid_id:
            # Collect points belonging to the current medoid
            cluster_points.append((x_coord, y_coord))
        else:
            if active_medoid is not None:
                # If a new medoid is encountered, find the best medoid for the previous set of points
                optimal_medoid = min(cluster_points, key=lambda point: compute_total_distance(cluster_points, point))
                print(f"{optimal_medoid[0]}\t{optimal_medoid[1]}")
            
            # Reset for the new medoid
            active_medoid = medoid_id
            cluster_points = [(x_coord, y_coord)]

    # Handle the last set of points after the loop ends
    if active_medoid is not None:
        optimal_medoid = min(cluster_points, key=lambda point: compute_total_distance(cluster_points, point))
        print(f"{optimal_medoid[0]}\t{optimal_medoid[1]}")

if __name__ == "__main__":
    find_best_medoid()
