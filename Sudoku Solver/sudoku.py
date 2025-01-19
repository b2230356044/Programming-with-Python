import sys


def main():
    adress= sys.argv[1]
    output=sys.argv[2]
    file = open(adress, "r")
    reading = file.readlines()

    for i in range(0, len(reading)):
        reading[i] = reading[i].replace("\n", "") #Text was read line by line

    for i in range(0, len(reading)):
        reading[i] = reading[i].split(" ")#Text file was made list with split function
    with open(sys.argv[2], "w") as f:
        f.write(18*'-'+"\n")
        sudokutraveller(reading,f)

def sudokuwriting(sudokuTable, f):
    list_write = []
    for i in range(0, 9):
        strwrt = ""
        for j in range(0, 9):
            strwrt = strwrt + sudokuTable[i][j] + " "
        list_write.append(strwrt)#Between every element of list corresponding to rows was made gap
    for line in list_write:
        f.write(line + '\n')
    f.write("-" * 18 + "\n")


def sudokutraveller(sudokuTable,f):
        count=0
        while (istherezero(sudokuTable)):
            found = False
            for i in range(0, 9):
                for j in range(0, 9):
                    if sudokuTable[i][j] == '0':#Rows and columns was checked if there is a 0.
                        set = sudokusolver(sudokuTable, i, j)#If there is sudokusolver was called
                        if len(set) == 1:
                            sudokuTable[i][j] = list(set)[0]#The solution of sudokusolvers was printed instead of 0.
                            count+=1
                            f.write("Step"+" "+str(count)+" "+"-"+" "+str(sudokuTable[i][j])+" "+"@ R"+str(i+1)+"C"+str(j+1)+"\n")
                            f.write(18*"-"+"\n")
                            found = True
                            sudokuwriting(sudokuTable,f)
                            break
                if found:
                  break


def istherezero(sudokuTable):
    for i in range(0, 9):
        for j in range(0, 9):
            if sudokuTable[i][j] == '0':#For the loop in the sudokutraveller,0 points were checked until there are no more 0 points.
                return True
    return False


def sudokusolver(sudokuTable, i, j):
    set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}#All possible values
    for k in range(0, 9):
        set.discard(sudokuTable[i][k])#For the given row,all points were checked and if there are numbers which are not zero they were removed from set.
    for r in range(0, 9):
        set.discard(sudokuTable[r][j])#For the given column,all points were checked and if there are numbers which are not zero they were removed from set.
    corneri = i // 3#The 3*3 square's row which the point belongs to was found by dividing the point's row by 3.
    cornerj = j // 3#The 3*3 square's column which the point belongs to was found by dividing the point's column by 3.
    for d in range(corneri * 3, corneri * 3 + 3):
        for b in range(cornerj * 3, cornerj * 3 + 3):
            set.discard(sudokuTable[d][b])#In this 3*3 square,all points were checked and if there are numbers which are not zero they were removed from set.
    return set


if True:
    main()
    print()