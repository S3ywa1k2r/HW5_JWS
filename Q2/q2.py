import csv
def main():
    f=open('q2.csv','r',encoding='ANSI')
    data=csv.reader(f)
    next(data)
    date_max=''
    date_min=''
    diff_max=-999
    diff_min=999
    diff=0
    for row in data:
        if(row[3]=='' or row[4] ==''):
            continue
        diff = float(row[4])-float(row[3])
        if diff>diff_max:
            diff_max=diff
            date_max=row[0]

        if diff<diff_min:
            diff_min=diff
            date_min=row[0]

    print('*** Annual Temperature Report for Seoul in 2022 ***')
    print('Day with the Largest Temperature Variation: {0:s}'.format(date_max))
    print('Maximum Temperature Difference: {0:.1f} Celsius'.format(diff_max))
    print('Day with the Smallest Temperature Variation: {0:s} Celsius'.format(date_min))
    print('Minimum Temperature Difference: {0:.1f} Celsius'.format(diff_min))
    f.close()

if __name__ == '__main__':
    main()


