import mysql.connector

mydb = mysql.connector.connect(
        host = "localhost",
        user = "root", 
        password = "hushanglai", 
        database = "crawler_data"
        )

mycursor = mydb.cursor()

f = open("IaYZIu0Ko.csv", "r")
lines = f.readlines()
i = 1

for line in lines:
    elements = line.split(",")
    commenter_homepage = elements[0]
    commenter_name = elements[1]
    commenter_gender = elements[2]
    commenter_location = elements[3]
    comenter_weibo_num = elements[4]
    commenter_guanzhu_num = elements[5]
    commenter_fan_num = elements[6]
    comment_content = elements[7]
    comment_like_num = elements[8]
    comment_release_date = elements[9]

    # sql1 = "insert into weibo_crawler_data (commenter_homepage, commenter_name, \
    # commenter_gender, commenter_location) values (%s, %s, %s, %s)"
    # values1 = (commenter_homepage, commenter_name, commenter_gender, commenter_location)
    # mycursor.execute(sql1, values1)
    # sql2 = "insert into weibo_crawler_data (comenter_weibo_num, commenter_guanzhu_num, \
    # commenter_fan_num, comment_content, comment_like_num, comment_release_date) \
    # values (%s, %s, %s, %s, %s, %s)"
    # print(comment_content)
    # values2 = (int(comenter_weibo_num), int(commenter_guanzhu_num), int(commenter_fan_num), \
    #         comment_content, int(comment_like_num), UNIX_TIMESTAMP(
    #         comment_release_date))
    # mycursor.execute(sql2, values2)
    # mydb.commit()
    sql = "insert into test (id, name, id_key, date_time_date) values (%s, %s, %s, %s)"
    values = (str(i), commenter_name, comment_content, comment_release_date)
    mycursor.execute(sql, values)
    mydb.commit()
    i = i + 1
