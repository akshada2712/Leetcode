class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        # sort the boxTypes according to the units in decreasing order 
        
        boxTypes.sort(key= lambda x: x[1], reverse = True)
        max_units = 0
        for bType, bUnit in boxTypes:
            num_boxes = min(bType, truckSize)
            truckSize -= num_boxes
            max_units += (num_boxes * bUnit)
            
        return max_units
        