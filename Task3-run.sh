#!/bin/bash

# Subtask 1 - Join operation
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapreduce.job.reduces=3 \
-file ./join_mapper.py \
-mapper "python3 ./join_mapper.py" \
-file ./join_reducer.py \
-reducer "python3 ./join_reducer.py" \
-input /Input/Trips.txt \
-input /Input/Taxis.txt \
-output /joiner

# Subtask 2 - Counting operation
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapreduce.job.reduces=3 \
-file ./count_mapper.py \
-mapper "python3 ./count_mapper.py" \
-file ./count_reducer.py \
-reducer "python3 ./count_reducer.py" \
-input /joiner \
-output /count

# Subtask 3 - Global sorting operation using custom partitioner
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapreduce.job.reduces=3 \
-D stream.num.map.output.key.fields=1 \
-file ./sort_mapper.py \
-mapper "python3 ./sort_mapper.py" \
-file ./sort_reducer.py \
-reducer "python3 ./sort_reducer.py" \
-input /count \
-output /Output/Task3 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

# Remove previous outputs to avoid conflicts
hadoop fs -rm -r /join_output
hadoop fs -rm -r /count_output
