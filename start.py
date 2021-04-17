import os
import multiprocessing

def crawler(topic):
    cmd = "python WeiboTopicScrapy.py %s" % topic
    os.system(cmd)

print("Get top topics")
os.system("python WeiboTopic.py > topic/top_topics.txt")
f = open("topic/top_topics.txt", "r")
lines = f.readlines()
top_topics = []
for line in lines:
    c = line.split(" ")[0]
    if c != "0\n":
        top_topics.append(line.split(" ")[0])

for top_topic in top_topics:
    print("crawler topic %s" % top_topic)
    p = multiprocessing.Process(target=crawler, args=(top_topic, ))
    p.start()
