import os, sys
import multiprocessing
import subprocess
import csv
import sqlite3  
import jieba
from wordcloud import WordCloud
from imageio import imread


#csv path
CSV_FILE_PATH = "weibo_flask\\test.csv"

#save 
def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in datalist:
        for index in range(len(data)):
            data[index] = '"'+data[index]+'"'
        sql = '''
                insert into users_comments (
                URL,NAME,GENDER,ADDRESS,WB_NUM,FOLLOW,FANS,CONTENT,LIKES,RELEASE_TIME) 
                values(%s)'''%",".join(data)
        print(sql)
        finish(dbpath)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()

#create table
def init_db(dbpath):
    sql = '''
    CREATE TABLE users_comments(
    ID INTEGER  PRIMARY KEY  AUTOINCREMENT,
    URL            CHAR(50),
    NAME           TEXT   ,
    GENDER          CHAR(2)    NOT NULL,
    ADDRESS        CHAR(50),
    WB_NUM           INT     ,
    FOLLOW           INT     ,
    FANS           INT     ,
    CONTENT           TEXT    ,
    LIKES          INT     ,
    RELEASE_TIME           TEXT  
    )'''
   
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
def finish(dbpath):
    sql = '''
    DELETE FROM users_comments WHERE NAME = "评论者昵称";
    '''
   
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

#Transfer CSV file to DB
def csv_to_db(filepath):
    with open(filepath,encoding="utf8")as f:
        f_csv = csv.reader(f)
        saveData2DB(f_csv,"weibo_flask\\save.db")
        f.close()

#Generate WordCloud
def generateWordCloud(InPngFilePath,inTxtFile,outPngFilePath):
    frame_png = InPngFilePath
    data_source = inTxtFile

    f = open(data_source,'r',encoding='utf-8')
    txt=f.read()
    #mask=imread('6137484-dc4d579efc67f9ae.png')
    mask = imread(frame_png)
    #excludes=''stopwords = excludes,
    f.close()
    words = jieba.lcut(txt)
    new_txt = ' '.join(words)
    wordcloud = WordCloud(font_path = "msyh.ttc",\
                          background_color = "white",\
                          width = 800,\
                          height = 600,\
                          max_words = 200,\
                          mask = mask,\
                          max_font_size = 80,\
                          ).generate(new_txt)
    wordcloud.to_file(outPngFilePath)
    

    

# Crawler function
def crawler(topic):
    # This crawler will generate csv file in /topic
    cmd = "python WeiboTopicScrapy.py %s" % topic
    print(cmd)
    os.system(cmd)




if __name__ == '__main__':
    '''
    print("Getting top topics")
    print("Start writing top topics to topic\\top_topics.txt")
    # Get data from WeiboTopic.py crawler
    # This is thread, we don't want to use thread now, it will bring more problem
    # top_topics = subprocess.check_output(['python', 'WeiboTopic.py'])
    process = subprocess.Popen(['python', 'WeiboTopic.py'], stdout=subprocess.PIPE)
    # Wait for thread
    process.wait()
    # top_topics = os.system('python WeiboTopic.py')
    # check_output returns bytes, but we want chinese character, so decode it
    #print(process.stdout.read().decode('gbk'))
    top_topics = process.stdout.read().decode('gbk')
    
    
    f_top_topics = open("topic\\top_topics.txt", "w")
    lines = top_topics.split('\n')
    for line in lines:
        # Filter data
        c = line.split(" ")[0]
        # We don't need "0\n"
        if c != "0":
            print(c)
            f_top_topics.write(c + '\n')
    f_top_topics.close()
    print("Writing topic\\top_topics.txt done")
    '''
   

    '''
    # Make threads/workers
    f_top_topics = open("topic\\top_topics.txt", "r")
    # Skip the first line
    top_topics = f_top_topics.readlines()
    f_top_topics.close()
    for top_topic in top_topics:
        print("crawler topic %s" % top_topic)
        # crawler(top_topic)       
        #process = subprocess.Popen(target=crawler, args=(top_topic), shell=True, stdout=subprocess.PIPE)
        #process.wait()
        crawler(top_topic)
        
    '''
    # Analyze emotion
    # os.system("python write_emotion2csv.py")
    print("Starting analyze emotion, this will cost a lot time!!!")
    subprocess.check_call(['python', 'get_weibo_crawler_data.py'])
    
    # if save.db exists,it is not executed
    if not os.path.isfile("weibo_flask\\save.db"):
        csv_to_db(CSV_FILE_PATH)
    # generate WordCloud
    generateWordCloud("OIP.jpg","weibo_comment.txt","weibo_flask\\static\\assets\\img\\word.jpg")
        
    


