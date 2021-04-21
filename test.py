
def sumerize_all_data():
    f_all_data = open("weibo_comment.txt", "w",encoding="utf-8")
    f_comment = open("weibo_flask\\all_data.csv", 'r',encoding="utf-8")
    lines = f_comment.readlines()
    for line in lines:
        line = line.split(',')[7]
        f_all_data.write(line + '\n')
    f_all_data.close()
sumerize_all_data()