#! /bin/python
import sys

def data(path_data,path_source,name):
    fi = open(path_data,"r",encoding="utf-8")
    txt_data = fi.readlines()
    fi.close()
    fo = open(path_source,"r",encoding="utf-8")
    txt_source = fo.readlines()
    fo.close()
    k = 0
    flag_data_1,flag_data_2,flag_num= 0,0,0
    name = name+': ['
    for i in txt_data:
        flag_num += 1
        if(i.find(name) != -1  ):
            flag_data_1 = flag_num
        elif(i.find("],") != -1):
            flag_data_2 = flag_num-1
            break
    
    while(flag_data_1 != flag_data_2 and flag_data_2 != 0):
        flag_data_1 += 1
        k += 1
        txt_data[flag_data_1-1] = txt_source[k-1]
    fi = open(path_data,"w",encoding="utf-8")
    for i in txt_data:
        fi.writelines(i)
    fi.close()
        

def main(argv):
    # data("index.vue","1.txt","category")
    if len(sys.argv) != 4:
        print("Usage: source_file.vue data_file.csv key")
        print("key is where should be replaced")
        sys.exit(-1)

    print(argv)
    data(argv[1], argv[2], argv[3])
    
if __name__ == '__main__':
    main(sys.argv)

