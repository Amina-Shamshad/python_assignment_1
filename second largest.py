if __name__ == '__main__':

    outterlst=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        outterlst.append([name,score])
    # print(outterlst)
    sort_val= sorted(set(grade for name, grade in outterlst))
    # print(sort_val)
    second_value=sort_val[1]
    grades = sorted([name for name, grade in outterlst if grade==second_value])
    for i in grades:
        print(i)