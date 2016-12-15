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
    passcode=""
    reg = re.compile("^00000.*")
    while True:
        test=input+str(i)
        testhex=hashlib.md5(test).hexdigest()
        if reg.match(testhex):
            print("{} works! ({}) ".format(test, testhex))
            passcode+=str(testhex[5])
            j += 1
            if j == 8:
                print("PASSCODE is {}".format(passcode))
                return
        i+=1


if __name__ == '__main__':
    run()
