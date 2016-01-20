
# Activity 1

```
$ cd
$ wget http://www.fhict.nl/docent/downloads/BGDT/GCD-Week-6-access_log.txt
$ hadoop fs -put GCD-Week-6-access_log.txt
$ spark-shell
scala> val textFile = sc.textFile("GCD-Week-6-access_log.txt")
```

## 1.1

```
scala> textFile.filter(line => line.contains("/assets/js/the-associates.js")).count()
res0: Long = 2456
```

This can also be done 10000x easier and with less "big data" tool-bullshit using just the old-school shell:

```
$ cat GCD-Week-6-access_log.txt | grep /assets/js/the-associates.js | wc -l
2456
```

## 1.2

```scala
scala> textFile.filter(line => line.contains("10.99.99.186")).count()
res1: Long = 6
```

## 1.3

Find the most popular file on the website, that is, whose path occurs most often in access_log. The output should be: the file’s path and the number of times it occurs in the log.

```scala
scala> val result = textFile.map(line => line.split(" ")(6)).map(word => (word, 1)).reduceByKey((a, b) => a + b).sortBy(_._2, false)
scala> result.take(5)
res2: Array[(String, Int)] = Array((/assets/css/combined.css,117348), (/assets/js/javascript_combined.js,106818), (/,99303), (/assets/img/home-logo.png,98744), (/assets/css/printstyles.css,93158))
```

# Activity 2

```
$ hadoop fs -put gutenberg-small/
$ spark-shell

scala> val textFile = sc.textFile("gutenberg-small/*.txt")
scala> val counts = textFile.flatMap(line => line.split(" ")).map(word => (word.toLowerCase(), 1)).reduceByKey(_ + _).sortBy(_._2, false)
scala> counts.take(10)
res10: Array[(String, Int)] = Array((the,48639), ("",38786), (of,24098), (and,21571), (to,18427), (a,17025), (i,12981), (in,10590), (was,9919), (that,9068))
```

# Activity 3
RDD:

```
scala> val textFile = sc.textFile("gutenberg-small/*.txt")
scala> textFile.persist()
res2: textFile.type = gutenberg-small/*.txt MapPartitionsRDD[1] at textFile at <console>:21
```

Transformations:

```
scala> counts.sample(true, .2).take(10)
res11: Array[(String, Int)] = Array((at,4782), (on,3835), (they,3718), (be,3330), (her,2102), (been,1676), (some,1396), (some,1396), (than,1107), (before,1038))
```

```
scala> val parallel = sc.parallelize(1 to 9)
parallel: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[21] at parallelize at <console>:21
scala> val par2 = sc.parallelize(5 to 15)
par2: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[22] at parallelize at <console>:21
scala>  parallel.union(par2).collect
res12: Array[Int] = Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
```

Actions:

```
scala> val ijsjes = sc.parallelize(List("cornetto", "magnum", "oreo", "Ben & Jerry's", "Carvel", "Bubbies", "magnum"))
ijsjes: org.apache.spark.rdd.RDD[String] = ParallelCollectionRDD[28] at parallelize at <console>:21.1

scala> ijsjes.map(k => (k, 1)).countByKey
res14: scala.collection.Map[String,Long] = Map(magnum -> 2, Ben & Jerry's -> 1, oreo -> 1, cornetto -> 1, Carvel -> 1, Bubbies -> 1)
```
