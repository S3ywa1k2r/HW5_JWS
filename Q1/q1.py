import csv
def main():
    f=open('q1.csv','r',encoding='ANSI')
    data=csv.reader(f)
    next(data)
    avg_temp=0
    min_temp=0
    max_temp=0
    cnt=0

    for row in data:
        if row[2]=='' or row[3]=='' or row[4]=='':
            continue
        
        if row[2]!='':
            avg_temp+=float(row[2])
        if row[3]!='':
            min_temp+=float(row[3])
        if row[4]!='':
            max_temp+=float(row[4])
        cnt+=1
            
    avg_temp/=cnt
    min_temp/=cnt
    max_temp/=cnt
    print('*** Annual Temperature Report for Seoul in 2022 ***')
    print('Average Temperature: {0:.2f} Celsius'.format(avg_temp))
    print('Average Minimum Temperature: {0:.2f} Celsius'.format(min_temp))
    print('Average Maximum Temperature: {0:.2f} Celsius'.format(max_temp))
    f.close()

if __name__ == '__main__':
    main()


