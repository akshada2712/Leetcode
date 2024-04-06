class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda num: (num.bit_count(), num))
        
        return arr
        
#         binaries = {}
        
#         for i in range(len(arr)):
#             binaries[i] = Counter(bin(arr[i]))
#             del binaries[i]['b']
#         print(binaries)
#         cnts = defaultdict(list)
        
#         for i, bins in binaries.items():
            
            
        