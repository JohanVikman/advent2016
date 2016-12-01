
def run():
    input = open("input.txt", 'r')
    lines = file.read(input)
    liness = lines.replace("\n", " ").split(", ")
    ws = ["n","e","s","w"]
    facing = 0
    x = 0
    y = 0
    visited = {}
    for instruction in liness:
        if instruction[0] == "L":
            facing -= 1
        elif instruction[0] == "R":
            facing += 1
        wsi = ws[facing % 4]
        if wsi == "n":
            y += int(instruction[1:])
        elif wsi == "s":
            y -= int(instruction[1:])
        elif wsi == "w":
            x -= int(instruction[1:])
        elif wsi == "e":
            x += int(instruction[1:])
        print("Intr : {} wsi : {} y : {} x : {}".format(instruction, wsi, y, x))
        loc = "{},{}".format(x,y)
        if visited.has_key(loc):
            print("Found it at {} {} shortest here {}".format(y,x, abs(y) + abs(x)))
            return
        visited[loc] = True

    print("Final location y : {} x : {}".format(y, x))
    shortestway = abs(y) + abs(x)
    print("Shortest way (no blocks) : {}".format(shortestway))

if __name__ == '__main__':
    run()
