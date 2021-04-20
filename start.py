import os, sys
import multiprocessing
import subprocess


# Crawler function
def crawler(topic):
    # This crawler will generate csv file in /topic
    cmd = "python WeiboTopicScrapy.py %s" % topic
    print(cmd)
    os.system(cmd)


print("Getting top topics")
print("Start writing top topics to topic/top_topics.txt")
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
    # Filter data
    c = line.split(" ")[0]
    # We don't need "0\n"
    if c != "0":
        print(c)
        f_top_topics.write(c + '\n')
f_top_topics.close()
print("Writing topic/top_topics.txt done")


# Make threads/workers
f_top_topics = open("topic/top_topics.txt", "r")
# Skip the first line
top_topics = f_top_topics.readline()
top_topics = f_top_topics.readlines()
f_top_topics.close()
for top_topic in top_topics:
    print("crawler topic %s" % top_topic)
    # crawler(top_topic)
    p = multiprocessing.Process(target=crawler, args=(top_topic,))
    p.start()

# Analyze emotion
# os.system("python write_emotion2csv.py")
print("Store weibo data and starting analyze emotion, this will cost a lot time!!!")
# subprocess.check_call(['python', 'get_weibo_crawler_data.py'])
os.system('python get_weibo_crawler_data.py')
