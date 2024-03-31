lines = ["10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
"10.0.0.1 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
"10.0.0.2 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
"10.0.0.2 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20",
"10.0.0.3 - GET 2020-08-24", "10.0.0.1 - GET 2020-08-24", "10.0.0.2 - GET 2020-08-20"]
import heapq

def getfreqIp(lines, cnt):
    hashMap = {}

    for i in lines:
        ip = i.split('-')[0]
        #print(ip)
        hashMap[ip] = hashMap.get(ip, 0) + 1 

    maxVal = max(hashMap.values())
    ans = []
    for ip, val in hashMap.items():
        if val == maxVal:
            ans.append(ip)

    ans.sort()

    if len(ans) == 1:
        return str(ans[0])
    else:
        return ','.join(ans)

print(getfreqIp(lines,6))