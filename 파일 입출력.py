def reader(file): #파일 읽기
    import csv
    f = open(file,'r',newline="")
    rdr = csv.reader(f)
    return rdr

def subject_name(file): #과목 리스트 만들기 + 과목 선택받기
    subject_list = []
    rdr = reader(file)
    for line in rdr:
        if line[0] == '영역':
            continue
        if line[1] not in subject_list:
            subject_list.append(line[1])
    for i in subject_list:
        if i == subject_list[-1]:
            print(i,end=' ')
            break
        print(i,end=',')
    subject_choice = input('중 하나의 과목을 선택해주세요 :')

    return subject_choice

def chosen_subject(file): #선택된 과목의 리스트 만들기
    chosen_subject_list=[]
    subject_choice = subject_name(file)
    final_list =[]
    final_list.append(subject_choice)
    rdr = reader(file)
    for line in rdr:
        if line[1] == subject_choice:
            line[2] = int(line[2])
            line[3] = int(line[3])
            line[4] = int(line[4])
            chosen_subject_list.append((line[2:5]))
    final_list.append(chosen_subject_list)
    return final_list
