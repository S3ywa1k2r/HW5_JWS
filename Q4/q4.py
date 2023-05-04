import csv
def main():
    f=open('q4.csv','r',encoding='ANSI')
    data=csv.reader(f)
    next(data)
    line_1={}
    line_2={}
    line_3={}
    line_4={}     
    for row in data:
        if row[1]=='1호선':
            line_1[row[3]]=int(row[4])+int(row[5])

        elif row[1]=='2호선':
            line_2[row[3]]=int(row[4])+int(row[5])

        elif row[1]=='3호선':
            line_3[row[3]]=int(row[4])+int(row[5])

        elif row[1]=='4호선':
            line_4[row[3]]=int(row[4])+int(row[5])

    sorted_line_1=dict(sorted(line_1.items(),key=lambda item: item[1]))
    sorted_line_1_keys=list(sorted_line_1.keys())
    sorted_line_1_values=list(sorted_line_1.values())
    
    sorted_line_2=dict(sorted(line_2.items(),key=lambda item: item[1]))
    sorted_line_2_keys=list(sorted_line_2.keys())
    sorted_line_2_values=list(sorted_line_2.values())
    
    sorted_line_3=dict(sorted(line_3.items(),key=lambda item: item[1]))
    sorted_line_3_keys=list(sorted_line_3.keys())
    sorted_line_3_values=list(sorted_line_3.values())
    
    sorted_line_4=dict(sorted(line_4.items(),key=lambda item: item[1]))
    sorted_line_4_keys=list(sorted_line_4.keys())
    sorted_line_4_values=list(sorted_line_4.values())
        
    print('*** Subway Report for Seoul on March 2023 ***')
    print('Line {0:d}'.format(1))
    print('Busiest Station: {0:s} ({1:d})'.format(sorted_line_1_keys[-1],sorted_line_1_values[-1]))
    print('Least Station: {0:s} ({1:d})'.format(sorted_line_1_keys[0],sorted_line_1_values[0]))

    print('Line {0:d}'.format(2))
    print('Busiest Station: {0:s} ({1:d})'.format(sorted_line_2_keys[-1],sorted_line_2_values[-1]))
    print('Least Station: {0:s} ({1:d})'.format(sorted_line_2_keys[0],sorted_line_2_values[0]))

    print('Line {0:d}'.format(3))
    print('Busiest Station: {0:s} ({1:d})'.format(sorted_line_3_keys[-1],sorted_line_3_values[-1]))
    print('Least Station: {0:s} ({1:d})'.format(sorted_line_3_keys[0],sorted_line_3_values[0]))

    print('Line {0:d}'.format(4))
    print('Busiest Station: {0:s} ({1:d})'.format(sorted_line_4_keys[-1],sorted_line_4_values[-1]))
    print('Least Station: {0:s} ({1:d})'.format(sorted_line_4_keys[0],sorted_line_4_values[0]))

    f.close()

if __name__ == '__main__':
    main()


