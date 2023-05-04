import csv
def main():
    f=open('q3.csv','r',encoding='ANSI')
    data=csv.reader(f)
    next(data)
    line_dict={'1호선':0, '2호선':0,'3호선':0,'4호선':0,'5호선':0,'6호선':0,'7호선':0,'8호선':0,'9호선':0,}        
    for row in data:
        for i in line_dict.keys():
            if i==row[1]:
                line_dict[i]=line_dict[i]+int(row[4])+int(row[5])
                
    sorted_line=dict(sorted(line_dict.items(),key=lambda item: item[1]))
    lines=list(sorted_line.keys())
    passengers=list(sorted_line.values())
    print('*** Subway Report for Seoul on March 2023 ***')
    print('1st Busiest Line: Line {0:s} ({1:d})'.format(lines[8],passengers[8]))
    print('2nd Busiest Line: Line {0:s} ({1:d})'.format(lines[7],passengers[7]))
    print('1st Least used Line: Line {0:s} ({1:d})'.format(lines[0],passengers[0]))
    print('2nd Least used Line: Line {0:s} ({1:d})'.format(lines[1],passengers[1]))
    f.close()

if __name__ == '__main__':
    main()


