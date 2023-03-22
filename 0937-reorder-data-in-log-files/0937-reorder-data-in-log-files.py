import re
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        ll = []
        dl = []
        
        for i in logs:
            parts = i.split()
            identifier = parts[0]
            first_entry = parts[1]
            #print(first_entry)
            
            if first_entry.isalpha():
                ll.append(i)
            else:
                dl.append(i)
                
        #print(ll,dl)
                
        return sorted(ll, key = lambda x:(x.split()[1:], x.split()[0])) + dl