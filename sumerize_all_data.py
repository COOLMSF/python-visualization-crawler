import os

BASE_PATH = "weibo_data"

f_all_data = open("flask" + "/" + "all_data.csv", "w")


topics = os.listdir(BASE_PATH)
for topic in topics:
    wids = os.listdir(BASE_PATH + "/" + topic)
    for wid in wids:
        comments = os.listdir(BASE_PATH + "/" + topic + "/" + wid)
        for comment in comments:
            print("Sumerizing %s %s %s" % (topic, wid, comment))
            f_comment = open(BASE_PATH + "/" + topic + "/" \
                    + wid + "/" + comment, 'r')
            lines = f_comment.readlines()
            for line in lines:
                if len(line) < 3:
                    continue
                # Strip
                line = line.strip('\n')
                print(line)
                f_all_data.write(line + "," + topic + '\n')

f_all_data.close()
