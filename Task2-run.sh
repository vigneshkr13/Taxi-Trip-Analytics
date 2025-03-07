#!/bin/bash

# Extract the number of iterations (v) from initialization.txt
v=$(head -n 1 initialization.txt)
iteration=0

# Copy initialization.txt to centroids.txt, skipping the first line
# tail -n +2 initialization.txt > centroids.txt
cp initialization.txt centroids.txt


while [ $iteration -lt $v ]
do
    hadoop jar ./hadoop-streaming-3.1.4.jar \
        -D mapred.reduce.tasks=3 \
	-D mapred.text.key.partitioner.options=-k1 \
        -file centroids.txt \
        -file ./Task2-mapper.py \
        -mapper ./"python3 Task2-mapper.py" \
        -file ./Task2-reducer.py \
        -reducer ./"python3 Task2-reducer.py" \
        -input /Input/Trips.txt \
        -output /output$iteration \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner
        


    # Copy the new medoids generated in this iteration
    hadoop fs -cat /output$iteration/part-* > temp_file.txt
    (echo ""; cat temp_file.txt) > centroids1.txt


    # Compare the new medoids (centroids1.txt) with the old ones (centroids.txt) using reader.py
    val=$(python3 reader.py)

    # Check the result of reader.py (if 1, convergence is achieved)
    if [ $val -eq 1 ]; then
        echo "Converged after $iteration iterations."
	hadoop fs -mkdir -p /Output/Task2
	hadoop fs -cp /output$iteration/part-* /Output/Task2/
        break
    fi

    # Prepare for the next iteration
    cp centroids1.txt centroids.txt
    iteration=$((iteration + 1))
done

# Cleanup
rm  centroids1.txt temp_file.txt
