Project: Digital Librarian - Reverse Index
Mapper: mapper.py
Reducer: reducer.py
Stopwords: stopwords.txt
Input (HDFS): /user/student/library/
Output (HDFS): /user/student/output_reverseindex

Run command example:
hdfs dfs -rm -r /user/student/output_reverseindex
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
  -input /user/student/library/ \
  -output /user/student/output_reverseindex \
  -mapper "python3 mapper.py" \
  -reducer "python3 reducer.py" \
  -file mapper.py \
  -file reducer.py \
  -file stopwords.txt

Fetch & sort output:
hdfs dfs -get /user/student/output_reverseindex/part-00000 ./reverse_index.txt
sort reverse_index.txt -o reverse_index_sorted.txt
head -20 reverse_index_sorted.txt
