global score
import sys
def writing(reading):
    global score
    list_write = []
    for i in range(0, len(reading)):
        strwrt = ""
        for j in range(0, len(reading[1])):
            strwrt = strwrt + reading[i][j] + " "
        list_write.append(strwrt)
        str_val = "\n".join(list_write) #The given input was written as a rectangle or the shape of it.
    print(str_val)
    print("\nYour score is:" + str(score) + "\n")
    return str_val
score = 0
input_file =sys.argv[1]
file = open(input_file, "r")
reading = file.readlines()
for j in range(0, len(reading)):
    reading[j] = reading[j].replace("\n", " ")
for i in range(0, len(reading)):
    reading[i] = reading[i].split()
writing(reading)
len_r = len(reading)
len_c = len(reading[1])
while True:
 try:
    R, C = map(int, input("Please enter a row and column number: ").strip().split())
    num = reading[R - 1][C - 1]#The input was taken from the user as row and column. It was checked if the input has a mistake.
    break
 except IndexError:
    print("Please enter a correct size")
 except ValueError:
    print("Please enter a correct size")


def playing(reading, R, C):
    global score
    gtd = set([(R - 1, C - 1)])
    num = reading[R - 1][C - 1]
    gtd_sz = 0
    done = set()
    all_num_idx = set((r, c) for r in range(len_r) for c in range(len_c) if reading[r][c] == num)#Numbers which same with the given inputs cells number found and made a set.

    while len(gtd) != gtd_sz:
        gtd_sz = len(gtd)
        for a in gtd:
            if a in done:
                continue
            else:
                possible = set([(a[0] + 1, a[1]), (a[0] - 1, a[1]), (a[0], a[1] + 1), (a[0], a[1] - 1)]) # it looped over the tbd and add all indexed from all_num_idx that differ only in -1/+1 in row or col to any index thats already in the set
            gtd = gtd.union(possible & all_num_idx)
            all_num_idx -= gtd # reduced all_num_idx by all those that we already addded
            done.add(a)
    if len(gtd) > 1:
        count = len(gtd)
    else:
        count = 0
    score += count * int(num)
    for r, c in gtd:
        if len(gtd) > 1:
            reading[r][c] = " " #If there are possible neighbours that has the same value with the chosen cell it was made empty.
        else:
            print("\n" + "No movement happened try again\n")#If there are no neighbour cell which has same value of the chosen cell. This statement was printed.
    sliding(reading)
    columnslide(reading)
    writing(reading)
    return reading


def sliding(reading):
    rows = len(reading)
    cols = len(reading[0])
    while isthereanyspace(reading):
     for i in range(rows - 1, -1, -1):#The columns and rows were checked by nested loops if there was a empty cell under a number.
        for j in range(cols - 1, -1, -1):
            for k in range(0, len(reading)):#k is the variable for the empty cells row.
                if k > i:
                    if reading[k][j] == " ":
                        if reading[i][j] != " ":
                            number = reading[i][j]#If a empty cell under a number was founded.The empty cell was changed with the number and the numbers cell changed with a space.
                            reading[k][j] = number
                            reading[i][j] = " "



def isthereanyspace(reading):
    for i in range(len(reading) - 1):
        for j in range(len(reading[0])):
            if reading[i][j] != " " and reading[i + 1][j] == " ":#If there are any spaces under a number it returns true and calls the function sliding one more time.
                return True
    return False

def isthereanyspacecolumn(reading):
    columnslist = []
    for i in range(0,len(reading[0])-1,1):
        con = True
        for j in range(0, len(reading), 1):
            if reading[j][i] != " ":#The columns were travelled and if there is any cell that is not empty.False was returned by this function because empty column was searched.
                con = False
                break
        if con:
            columnslist.append(i)
            break
    return columnslist

def columnslide(reading):
    columnlist = isthereanyspacecolumn(reading)
    while (len(columnlist) != 0):#isthereanyspacecolumn function was called to define the empty column.
        for i in range(0,len(reading),1):
            reading[i][columnlist[0]] = reading[i][columnlist[0]+1]
            reading[i][columnlist[0] + 1] = " "#The right side of the empty column shifted to the left and their cell was made empty.
        columnlist = isthereanyspacecolumn(reading)

def check_and_play(reading):
    rows = len(reading)
    cols = len(reading[0])
    for i in range(rows):
        for j in range(cols):
            if reading[i][j] is not " ":
                current_value = reading[i][j]#The cells which are not empty were searched to check if there are more playable neighbour cells which have the same value.

    while True:
        found_same_value = False

        # Check for adjacent cells with the same value
        for i in range(rows):
            for j in range(cols):
                if reading[i][j] is not " ":
                    current_value = reading[i][j]

                    # Check right neighbor
                    if j + 1 < cols and reading[i][j + 1] == current_value:
                        found_same_value = True

                    # Check down neighbor
                    if i + 1 < rows and reading[i + 1][j] == current_value:
                        found_same_value = True

                    # Check up neighbor
                    if i - 1 >= 0 and reading[i - 1][j] == current_value:
                        found_same_value = True

                    # Check left neighbor
                    if j - 1 >= 0 and reading[i][j - 1] == current_value:
                        found_same_value = True

        if found_same_value:
            try:
                R, C = map(int, input("Please enter a row and column number: ").strip().split())
                print("")#If there are more neighbour cells which have the same numeric value. Input is taken one more time.
                reading = playing(reading, R, C)#The deleting cells function is called.
            except ValueError:
                print("Please enter a correct size")
            except IndexError:
                print("Please enter a correct size")
        else:
            print("Game over!")#If there are no more neighbour cells which have the same value. Game over is printed out.
            break


playing(reading, R, C)
check_and_play(reading)
