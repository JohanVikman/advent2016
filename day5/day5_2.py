import hashlib
import re

def run():
    #Door ID: ffykfhsq
    #Test ID: abc
    input = "ffykfhsq"
    m = hashlib.md5()
    m.update(input)
    i=0
    j=0
    passcode=["","","","","","","",""]
    passcodeindex=['0','1','2','3','4','5','6','7']
    reg = re.compile("^00000.*")
    while True:
        test=input+str(i)
        testhex=hashlib.md5(test).hexdigest()
        if reg.match(testhex):
            n=testhex[5]
            char=testhex[6]
            if n in passcodeindex:
                # if not, already written
                l = passcodeindex.index(n)
                passcodeindex.pop(l)
                passcode[int(n)]=char
                print("{}".format(passcode))
                j += 1
                if j == 8:
                    return
        i+=1

if __name__ == '__main__':
    run()
