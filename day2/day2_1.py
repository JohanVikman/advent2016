
def run():
    input = open("input.txt", 'r')
    lines = file.read(input)
    numpad = [[1,2,3],[4,5,6],[7,8,9]]
    currentpos=[1,1] # Row 1, Column 1 == Starting at '5'
    result = ""
    for line in lines.split("\n"):
        if len(line) == 0:
            #empty line
            continue
        for instruction in line:
            if instruction[0] == "U":
                currentpos[0] = decrease(currentpos[0])
            elif instruction[0] == "D":
                currentpos[0] = increase(currentpos[0])
            elif instruction[0] == "L":
                currentpos[1] = decrease(currentpos[1])
            elif instruction[0] == "R":
                currentpos[1] = increase(currentpos[1])

        num = numpad[currentpos[0]][currentpos[1]]
        result += str(num)
    print("The code is {}".format(result))

def increase(i):
    if i < 2:
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
