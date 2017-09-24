import re
import sys
import os

def getLastProcessNo(line):
    #30282 ?        S      0:00 python3 dblp.py 51 25

    process_num_last = regexMatch("python3 dblp.py (\d{0,2})",line)
    return int(process_num_last)
def regexMatch(pattern,content):
    pattern = re.compile(pattern, re.DOTALL)
    matcher = pattern.findall(content)
    return matcher[0]
def getActiveProcess(pattern,content):
    matcher = regexMatch(pattern,content)
    if len(matcher) > 3:
        return True
    else:
        return False

process_num = int(sys.argv[1])
process = os.popen("ps x | grep 'python3 dblp.py' | grep -v grep | wc -l")
active_no = process.read()
an_current = process_num
if int(active_no) == an_current :
    os._exit(0)
else:
    process = os.popen("ps x | grep 'python3 dblp.py' | grep -v grep")
    list_active = process.read()
    list_active = list_active.split("\n")
    an_last =  getLastProcessNo(list_active[0])
    pattern = "(python3 dblp.py %s %s)"
    if an_last == an_current :
        for i in range(an_current):
            for line in list_active:
                faceback = getActiveProcess(pattern%(an_current,i),line)
                print(faceback)
    else:
        pass
    for i in range(an_current):
        pass

process.close()

