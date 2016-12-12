def run():
    input = open("input.txt", 'r')
    lines = file.read(input)
    actual_triangles = 0
    index = 0
    
    current_matrix = []
    matrices = []

    for line in lines.split("\n"):
        if len(line) == 0:
            #Empty line
            continue
        sides = [int(n) for n in line.split()]
        current_matrix.append(sides)
        index +=1
        if index == 3:
            matrices.append(current_matrix)
            current_matrix = []
            index = 0

    for matrix in matrices:
        for i in range(3):
            tri = [matrix[0][i],
                   matrix[1][i],
                   matrix[2][i]]
            if is_triangle(tri):
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
