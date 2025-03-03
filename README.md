# Taxi Trip Analytics with MapReduce

A big data processing project implementing MapReduce algorithms for analyzing taxi trip data. This project leverages the Hadoop ecosystem to process large datasets of taxi trip information and extract meaningful statistics.

## Project Overview

This project analyzes taxi trip data using custom MapReduce implementations in Python. The analysis includes:

1. **Trip Classification and Statistics**: Categorizes trips as long, medium, or short based on distance, then computes statistics for each taxi including count, maximum fare, minimum fare, and average fare.

2. **Location-Based Clustering**: Implements a k-medoid clustering algorithm (PAM - Partitioning Around Medoids) to group trips based on dropoff locations, allowing for pattern discovery in destination hotspots.

3. **Company Performance Analysis**: Joins taxi and trip data to analyze the number of trips per taxi company, with results sorted in ascending order.

## Dataset Description

The project works with two datasets stored on HDFS:

### Taxis.txt
Contains information about taxis with the following format:
```
Taxi#, company, model, year
```

### Trips.txt
Contains information about trips with the following format:
```
Trip#, Taxi#, fare, distance, pickup_x, pickup_y, dropoff_x, dropoff_y
```

## Technical Implementation

### Key Features
- Custom MapReduce implementation in Python without external MapReduce libraries
- In-mapper combining with state preservation
- Multi-stage MapReduce operations including join, aggregation, and sorting
- K-medoid clustering algorithm implementation in a distributed environment
- Memory-efficient processing of large datasets

### Technology Stack
- Python for MapReduce implementation
- Hadoop Distributed File System (HDFS) for data storage
- Hadoop Streaming for executing Python MapReduce jobs

## Running the Project

### Prerequisites
- Hadoop cluster or single-node setup
- Python 3.x
- HDFS with the datasets loaded

### Task 1: Trip Classification and Statistics

This task categorizes trips as long (≥200), medium (≥100 and <200), or short (<100) based on distance, then computes statistics for each taxi.

```bash
./Task1-run.sh
```

### Task 2: K-Medoid Clustering

This task clusters trips based on dropoff locations using the PAM algorithm. The number of clusters (k) and iterations (v) can be configured in the initialization.txt file.

```bash
./Task2-run.sh
```

Sample initialization.txt for k=3 and v=10:
```
10
85.679
11.737
83.802
99.074
11.615
1.277
```

### Task 3: Company Performance Analysis

This task joins taxi and trip data to count trips per company and sort results.

```bash
./Task3-run.sh
```

## Results

The project generates the following outputs:

1. **Task 1**: For each taxi and trip type (long, medium, short), provides count, max fare, min fare, and average fare.

2. **Task 2**: Clusters of trips based on dropoff locations, with each trip assigned to a cluster.

3. **Task 3**: Sorted list of taxi companies based on the total number of trips in ascending order.

## Project Structure

```
├── Task1-run.sh            # Shell script to run Task 1
├── Task1-mapper.py         # Mapper for Trip Classification
├── Task1-reducer.py        # Reducer for Trip Statistics
├── Task2-run.sh            # Shell script to run Task 2
├── Task2-mapper.py         # Mapper for K-Medoid Clustering
├── Task2-reducer.py        # Reducer for K-Medoid Clustering
├── initialization.txt      # Configuration for K-Medoid Clustering
├── Task3-run.sh            # Shell script to run Task 3
├── Task3-join-mapper.py    # Mapper for Join Operation
├── Task3-join-reducer.py   # Reducer for Join Operation
├── Task3-count-mapper.py   # Mapper for Counting
├── Task3-count-reducer.py  # Reducer for Counting
├── Task3-sort-mapper.py    # Mapper for Sorting
├── Task3-sort-reducer.py   # Reducer for Sorting
└── README.md               # Project documentation
```

## Key Implementation Considerations

- The project implements in-mapper combining with state preservation across lines
- The code is optimized to work with 3 reducers
- Data is processed line by line without loading the entire dataset into memory
- The k-medoid clustering implementation supports configurable k and iteration counts
- The multi-stage MapReduce process for Task 3 demonstrates advanced Hadoop workflow concepts
