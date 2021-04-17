import jieba
import os
import sys
from wordcloud import WordCloud
from imageio import imread

def main(argv):
    if len(argv) != 3:
        print("Usage:%s %s %s" % (argv[0], "frame.png", "data_stource.txt"))
        print("For example: python wordCloud.py ./OIP.jpg ./weibo_comment.txt")
        sys.exit(-1)

    frame_png = argv[1]
    data_source = argv[2]

    f = open(argv[2],'r',encoding='utf-8')
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
    wordcloud.to_file('词云图.png')

if __name__ == "__main__":
    main(sys.argv)
