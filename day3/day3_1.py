def run():
    input = open("input.txt", 'r')
    lines = file.read(input)
    actual_triangles = 0
    for line in lines.split("\n"):
        if len(line) == 0:
            #Empty line
            continue
        sides = [int(n) for n in line.split()]
        if is_triangle(sides):
            actual_triangles += 1
    print("Total number of triangles {}".format(actual_triangles))

def is_triangle(sides):
    if sides[0] + sides[1] > sides[2]:
        if sides[1] + sides[2] > sides[0]:
            if sides[0] + sides[2] > sides[1]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
        
if __name__ == '__main__':
    run()
