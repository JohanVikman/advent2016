def run():
    input = open("input.txt", 'r')
    lines = file.read(input)
    liness = lines.replace("\n", " ").split(", ")
    ws = ["n","e","s","w"]
    facing = 0
    x = x0 = 0
    y = y0 = 0
    visited = {}
    for instruction in liness:
        if instruction[0] == "L":
            facing -= 1
        elif instruction[0] == "R":
            facing += 1
        wsi = ws[facing % 4]
        y0 = y
        x0 = x
        if wsi == "n":
            y += int(instruction[1:])
        elif wsi == "s":
            y -= int(instruction[1:])
        elif wsi == "w":
            x -= int(instruction[1:])
        elif wsi == "e":
            x += int(instruction[1:])
        locs = make_passed_locs(y0, y, x0, x)
        for loc in locs:
            lockey="{},{}".format(loc[0],loc[1])
            if visited.has_key(lockey):
                print("Found it at {} shortest here {}".format(loc,
                                                               abs(loc[0]) + abs(loc[1])
                                                               )
                      )
                return
            # Otherwise keep adding them until we found it
            visited[lockey] = True

    print("Final location without any crossings y : {} x : {}".format(y, x))
    shortestway = abs(y) + abs(x)
    print("Shortest way: {}".format(shortestway))

def make_passed_locs(y0, y, x0, x):
    yrange = make_range(y0, y)
    xrange = make_range(x0, x)
    locs = []
    if len(yrange) > 1:
        for yi in yrange:
            locs.append([x,yi])
    else:
        for xi in xrange:
            locs.append([xi,y])
    return locs


def make_range(pos0, pos):
    posrange = []
    if pos0 != pos:
        if pos0 < pos:
            posrange = range(pos,pos0, -1)
        else:
            posrange = range(pos,pos0)
    else:
        posrange = [pos]
    return posrange


if __name__ == '__main__':
    run()
