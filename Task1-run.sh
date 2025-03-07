#!/bin/bash    
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D mapred.reduce.tasks=3 \
-D stream.num.map.output.key.fields=2 \
-D mapreduce.partition.keypartitioner.options=-k1,2 \
-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner \
-file ./Task1-mapper.py \
-mapper ./Task1-mapper.py \
-file ./Task1-reducer.py \
-reducer ./Task1-reducer.py \
-input /Input/Trips.txt \
-output /Output/Task1
