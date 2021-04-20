import os, sys
import multiprocessing
import subprocess


# Crawler function
def crawler(topic):
    # This crawler will generate csv file in /topic
    cmd = "python WeiboTopicScrapy.py %s" % topic
    print("--------------------------")
    print(cmd)
    print("--------------------------")
    os.system(cmd)


print("--------------------------")
print("Getting top topics")
print("Start writing top topics to topic/top_topics.txt")
print("--------------------------")
# Get data from WeiboTopic.py crawler
# This is thread, we don't want to use thread now, it will bring more problem
# top_topics = subprocess.check_output(['python', 'WeiboTopic.py'])
process = subprocess.Popen(['python', 'WeiboTopic.py'], stdout=subprocess.PIPE)
# Wait for thread
process.wait()
# top_topics = os.system('python WeiboTopic.py')
# check_output returns bytes, but we want chinese character, so decode it
top_topics = process.stdout.read().decode('utf-8')


f_top_topics = open("topic/top_topics.txt", "w")
lines = top_topics.split('\n')
for line in lines:
    f_top_topics.write(line + '\n')
f_top_topics.close()
print("--------------------------")
print("Writing topic/top_topics.txt done")
print("--------------------------")


# Make threads/workers
f_top_topics = open("topic/top_topics.txt", "r")
top_topics = f_top_topics.readlines()
f_top_topics.close()
for top_topic in top_topics:
    print("--------------------------")
    print("crawler topic %s" % top_topic)
    print("--------------------------")
    # Check invalid topic
    if len(top_topic) > 3:
        crawler(top_topic)

# Analyze emotion
print("Store weibo data and starting analyze emotion, this will cost a lot time!!!")
os.system('python get_weibo_crawler_data.py')
