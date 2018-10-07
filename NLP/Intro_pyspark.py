#############################################################
#                                                           #
#                   MOVIE RATING PROGRAM                    #
#                                                           #
#############################################################

from pyspark import SparkContext, SparkConf
import collections
conf = SparkConf().setMaster("local").setAppName("RatingHistogram")
sc = SparkContext(conf=conf)

lines = sc.textFile("/Users/siddheshschavan/Documents/Work/Python/Training_MNMCK/NLP/ml-100k/u.data")
# lines1 = lines.collect()
movies = lines.map(lambda y: (int(y.split()[1]), 1))
movies1 = movies.collect()
moviesCount = movies.reduceByKey(lambda x, y: x+y)
moviesCount1 = moviesCount.collect()

flipped = moviesCount.map(lambda x, y: (y, x))
# flipped1 = flipped.collect()
# sortedMovies = flipped.sortByKey()
# sortedMovies1 = sortedMovies.collect()

for one in flipped.collect():
    print(one[0], one[1])

rating = lines.map(lambda x: x.split()[2])
rating1 = rating.collect()
result = rating.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))

for key, value in sortedResults.items():
    print("%s %s" % (key, value))


#############################################################
#                                                           #
#       Illustrate the reduceByKey and mapValues            #
#                                                           #
#############################################################
# from pyspark import SparkContext, SparkConf
# import math
# import os
# pwd = os.getcwd()
#
#
# conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
# sc = SparkContext(conf=conf)
#
#
# def readline(line):
#     fields = line.split(',')
#     age = int(fields[2])
#     friends = int(fields[3])
#     return age, friends
#
#
# lines = sc.textFile(os.path.join(pwd, "fakefriends.csv"))
# lines1 = lines.collect()
# rdd = lines.map(readline)
# rdd1 = rdd.collect()
# totalsByAge = rdd.mapValues(lambda x:(x,1)).reduceByKey(lambda x,y:(x[0]+y[0], x[1]+y[1]))
# totalsByAge1 = totalsByAge.collect()
# averagesByAge = totalsByAge.mapValues(lambda x: x[0]/x[1])
# averagesByAge1 = averagesByAge.sortByKey()
#
# results = averagesByAge1.collect()
#
# for result in results:
#     print("%d, %d" %(result[0], math.floor(result[1])))


#############################################################
#                                                           #
#       Weather data sample filtering RDD's                 #
#                                                           #
#############################################################
# from pyspark import SparkContext, SparkConf
# import os
# pwd = os.getcwd()
#
# conf = SparkConf().setMaster("local").setAppName("TemperatureMin")
# sc = SparkContext(conf=conf)
#
#
# def parseline(line):
#     fields = line.split(',')
#     stationID = fields[0]
#     entryType = fields[2]
#     temperature = float(fields[3]) * 0.1 * (9/5) + 32.0
#     return stationID, entryType, temperature
#
#
# lines = sc.textFile(os.path.join(pwd,'1800.csv'))
# parsedLines = lines.map(parseline)
# parsedLines1 = parsedLines.collect()
# filterLine = parsedLines.filter(lambda x: "TMAX" in x)
# filterLine1 = filterLine.collect()
# minTemp = filterLine.map(lambda x: (x[0], x[2]))
# minTemp1 = minTemp.collect()
# minTemp_final = minTemp.reduceByKey(lambda x,y: max(x,y))
# minTemp_final1 = minTemp_final.collect()
#
# print(parsedLines1)

#############################################################
#                                                           #
#       Count the occurance of a word                       #
#                                                           #
#############################################################
# from pyspark import SparkContext, SparkConf
# import os
# import re
# pwd = os.getcwd()
#
# conf = SparkConf().setMaster("local").setAppName("WordCount")
# sc = SparkContext(conf=conf)
#
#
# def normalizeword(text):
#     return re.compile(r'\W+', re.UNICODE).split(text.lower())
#
#
# input = sc.textFile(os.path.join(pwd, "Book.txt"))
# words = input.flatMap(normalizeword)
# words1 = words.collect()
# # wordsCount = words.countByValue()
#
# wordsCount1 = words.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x+y)
#
# # wordsCount2 = wordsCount1.collect()
# wordsCountSorted = wordsCount1.sortBy(lambda a: a[1])
#
# # wordsCountSorted1 = wordsCountSorted.collect()
#
# for i in wordsCountSorted.collect():
#     print(i[0], ":\t\t\t\t", i[1])

#############################################################
#                                                           #
#       Amount spend by the customer                        #
#                                                           #
#############################################################
# from pyspark import SparkContext, SparkConf
# import os
# pwd = os.getcwd()
#
# conf = SparkConf().setMaster("local").setAppName("TimeSpent")
# sc = SparkContext(conf=conf)
# file = sc.textFile(os.path.join(pwd, "customer-orders.csv"))
#
#
# def time_count(file_input):
#     sep = file_input.split(",")
#     ip1 = sep[0]
#     ip2 = sep[2]
#     return ip2, ip1
#
#
# file1 = file.map(time_count)
# reduceFile = file1.reduceByKey(lambda x,y: x+y)
# ascend = reduceFile.sortByKey()
# ascend1 = ascend.collect()
# for i in ascend1:
#     print("%d $%0.02f" %(int(i[1]), float(i[0])))