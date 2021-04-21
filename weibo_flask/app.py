from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    #return render_template("index.html")
    return index()


@app.route('/movie')
def movie():
    datalist  = []
    con = sqlite3.connect("save.db")
    cur = con.cursor()
    sql = "select * from users_comments"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    print(datalist)
    return render_template("movie.html",movies = datalist)



@app.route('/score')
def score():
    score = []  
    num = []
    score1 = []  
    num1 = []
    score2 = []  
    num2 = []
    k=0
    con = sqlite3.connect("save.db")
    cur = con.cursor()
    sql = "select topics as t,sum(WB_NUM) from users_comments  group by topics order by WB_NUM desc limit 5"
    sql1 = "select release_time  as time ,count(release_time) from users_comments group by time"
    sql2 = "select address,count(address) as t  from users_comments  group by address order by t desc"
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        num.append(item[1])
    data1 = cur.execute(sql1)
    for item in data1:
        score1.append(str(item[0]))
        num1.append(item[1])
    data2 = cur.execute(sql2)
    for item in data2:
         if(k<5):
            k+=1
            score2.append(str(item[0]))
            num2.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html",score= score,num=num,score1= score1,num1=num1,score2= score2,num2=num2)


@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    addr = {}
    con = sqlite3.connect("save.db")
    cur = con.cursor()
    sql = "select address,wb_num from users_comments"
    data = cur.execute(sql)
    for item in data:
        flag = addr.get(item[0],0)
        if(flag):
            addr[item[0]]=item[1]+addr.get(item[0])
        else:
            addr[item[0]]=item[1]
        #print(item)
       

    cur.close()
    con.close()
    print(addr)
    #print(addr['北京'])
    #print(type(addr.get('北京')))
    return render_template("team.html",addr=addr)


if __name__ == '__main__':
    app.run()
