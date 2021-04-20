import os, sys
import subprocess
import shutil
import time

BASE_PATH = "weibo_data"
# Run this script after all crawlers have done their jobs!!!

def cp_append_file(dst, src):
    f_src = open(src, "r")
    f_dst = open(dst, "w")
    # Skip the first line
    lines = f_src.readline()
    lines = f_src.readlines()
    for line in lines:
        # f_dst.write(line)
        comment = line.split(',')[-3]
        # Get comment emotion
        print("Starting to analyze emotion")
        emotion = subprocess.check_output(['python', 'keras-bert-emotional-classifier/eval.py', comment]).decode('utf-8')
        # Write file
        print(line + ',' + emotion + '\n')
        f_dst.write(line + ',' + emotion + '\n')
    f_src.close()
    f_dst.close()


try:
    # Always delete old weibo_data
    shutil.rmtree(BASE_PATH)
except:
    pass


# Create weibo_data directory to store all crawler data
os.mkdir(BASE_PATH)


# Get all topics, topics data is in topic directory
all_topics = os.listdir("topic")
# Filter other files, we only need csv files, every .csv file is a topic
temp = []
for topic in all_topics:
    # Filename contains csv string
    if topic.find("csv") > 1:
        # Don't need its suffix
        topic = topic.split('.')[0]
        temp.append(topic)
all_topics = temp


print("All topics")
print(all_topics)
# Get all posts
for topic in all_topics:
    os.mkdir(BASE_PATH + "/" + topic)
    f_topic_csv = open("topic/" + topic + ".csv")
    # Skip the first line
    lines = f_topic_csv.readline()
    lines = f_topic_csv.readlines()
    for line in lines:
        elements = line.split(',')
        wid = elements[0]
        comment_num = elements[-2]


        # We create the weibo post directory using wid(weibo post id)
        # We only need the post that its comment is greater that 1,
        # because we want analyze its emotion using(emotional-classifier)
        # os.mkdir("weibo_data/" + topic + "/" + wid)
        if int(comment_num) > 1:
            os.mkdir(BASE_PATH + "/" + topic + "/" + wid)
            # f_comments = open(BASE_PATH + "/" + topic + "/" + wid + "all_comments.txt", "w")
            # check_output returns []byte
            print("Starting to crawl post: %s" % wid)
            # subprocess.check_output(['python', 'WeiboTopicScrapy.py', wid])
            # cmd = "python WeiboTopicScrapy.py" + " " + wid
            cmd = [ "python", "WeiboCommentScrapy.py", wid ]
            # process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
            print("python WeiboCommentScrapy.py %s" + wid)
            process = subprocess.Popen("python WeiboCommentScrapy.py" + " " + wid, shell=True, stdout=subprocess.PIPE)
            process.wait()
            # try:
            #     cp_append_file(BASE_PATH + "/" + topic + "/" + wid + "/" + "comment" + ".csv", "comment" + "/" + wid + ".csv")
            # except:
            #     print("cp file error")
            cp_append_file(BASE_PATH + "/" + topic + "/" + wid + "/" + "comment" + ".csv", "comment" + "/" + wid + ".csv")
                # No comment found, do nothing
                # pass
            # print(BASE_PATH + "/" + topic + "/" + wid + "/" + "comment" + ".csv" + "<-" + "comment" + "/" + wid + ".csv")
