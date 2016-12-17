from __future__ import print_function

def run():
    input = open("input.txt", 'r')
    lines = file.read(input)
    abbas = 0
    for line in lines.split("\n"):
        if len(line) == 0:
            continue

        sliding_window = []
        bracket_mod = False
        abba_mod = False
        try:
            for c in line:
                if c == "[":
                    bracket_mod=True
                elif c == "]":
                    bracket_mod=False

                if len(sliding_window) == 4:
                    sliding_window.pop(0)
                    sliding_window.append(c)
                else:
                    sliding_window.append(c)
                if len(sliding_window) < 4:
                    continue
                new_abba_mod = check_abba(sliding_window)
                if new_abba_mod and bracket_mod:
                    raise NameError("Bad ABBA")
                if new_abba_mod:
                    abba_mod=new_abba_mod

        except NameError:
            print("{} has ABBA between ".format(line))
            continue
        if abba_mod:        
            print("{} is ok".format(line))
            abbas+=1
        else:
            print("{} NO".format(line))     

    print("{} ABBA".format(abbas))

def check_abba(sliding_window):
    if sliding_window[0] == sliding_window[3]:
        if sliding_window[0]  != sliding_window[1]:
            if sliding_window[1] == sliding_window[2]:
                print("{} is candidate".format(sliding_window))
                return True
    return False

if __name__ == '__main__':
    run()
