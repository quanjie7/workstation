#encoding:utf-8
from pyspark import SparkContext
readme="E:\\sparkIDE\\file\\spark.txt"
sc = SparkContext("local","Simple App")
logData = sc.textFile(readme).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
print(sc.textFile(readme).count())
sc.stop()