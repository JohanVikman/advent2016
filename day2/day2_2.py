
def run():
    input = open("input.txt", 'r')
    lines = file.read(input)
    numpad = [["X","X",1,"X","X"],
              ["X",2,3,4,"X"],
              [5,6,7,8,9],
              ["X","A","B","C","X"],
              ["X","X","D","X","X"]]
    currentpos=[3,1] # Row 3, Column 1 == Starting at '5'
    result = ""
    for line in lines.split("\n"):
        if len(line) == 0:
            #empty line
            continue
        for instruction in line:
            if instruction[0] == "U":
                proposed = decrease(currentpos[0])
                if numpad[proposed][currentpos[1]] == "X":
                    continue
                else:
                    currentpos[0] = proposed
            elif instruction[0] == "D":
                proposed = increase(currentpos[0])
                if numpad[proposed][currentpos[1]] == "X":
                    continue
                else:
                    currentpos[0] = proposed
            elif instruction[0] == "L":
                proposed = decrease(currentpos[1])
                if numpad[currentpos[0]][proposed] == "X":
                    continue
                else:
                    currentpos[1] = proposed
            elif instruction[0] == "R":
                proposed = increase(currentpos[1])
                if numpad[currentpos[0]][proposed] == "X":
                    continue
                else:
                    currentpos[1] = proposed
                
        num = numpad[currentpos[0]][currentpos[1]]
        result += str(num)
    print("The code is {}".format(result))

def increase(i):
    if i < 4:
        return i + 1
    else:
        return i

def decrease(i):
    if i > 0:
        return i - 1
    else:
        return i
    
if __name__ == '__main__':
    run()
