import os
import multiprocessing


# Crawler function
def crawler(topic):
    # This crawler will generate csv file in /topic
    cmd = "python WeiboTopicScrapy.py %s" % topic
    os.system(cmd)


# Get all hot topics, and let threads to crawl them.
print("Get top topics")
os.system("python WeiboTopic.py > topic/top_topics.txt")
f = open("topic/top_topics.txt", "r")
lines = f.readlines()
top_topics = []
for line in lines:
    # Filter data
    c = line.split(" ")[0]
    # We don't need "0\n"
    if c != "0\n":
        top_topics.append(line.split(" ")[0])

# Make threads/workers
for top_topic in top_topics:
    print("crawler topic %s" % top_topic)
    p = multiprocessing.Process(target=crawler, args=(top_topic,))
    p.start()

# Analyze emotion
os.system("python write_emotion2csv.py")
