class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        dirsmap = {"N": [0,1], "S":[0,-1], "E": [1,0], "W": [-1,0]}
        
        currDir = "N"
        x, y = 0, 0
        instructions = instructions * 4 # checking all 4 sides
        for i in instructions:
            if i == "G":
                x, y = x + dirsmap[currDir][0], y + dirsmap[currDir][1]
            elif i == 'L':
                if currDir == "N":
                    currDir = "W"
                elif currDir == 'S':
                    currDir = "E"
                elif currDir == "E":
                    currDir = "N"
                else:
                    currDir = "S"
            elif i == 'R':
                if currDir == "N":
                    currDir = "E"
                elif currDir == 'S':
                    currDir = "W"
                elif currDir == "E":
                    currDir = "S"
                else:
                    currDir = "N"
                    
                    
        return x == 0 and y == 0
                
                    
            


        
#         dirX, dirY = 0, 1  # initial north
        
#         x, y = 0, 0   # inital cordinates
        
#         for i in instructions:
#             if i == "G":   # easy case, move one step ahead so we add diretion coordinates
#                 x, y = x + dirX, y + dirY
                
#             elif i == "L":   # moving to left, turning by 90 deg acc to linear algebra rotating is swapping values 
#                 # multiply X by -1 as we want to go left side not right side
#                 dirX, dirY = -1 * dirY, dirX   
                
#             else:
#                 dirX, dirY = dirY, -1 * dirX
                 
#         return (x,y) == (0,0) or (dirX, dirY) != (0,1)   # we are checking that the cordinates should be original ones and directions should be not same
                
        
#         dirsmap = {"N": [0,1], "S":[0,-1], "E": [1,0], "W": [-1,0]}
        
#         currDir = "N"
#         currLoc = (0,0)
#         i = 0
#         while True:
#             if i == len(instructions) and currDir == "N":
#                 return False
#             if instructions[i] == "G": 
#                 currLoc[0] += dirsMap[currDir][0]
#                 currLoc[1] += dirsMap[currDir][1]
                
                
#             elif instructions[i] == "L":
                
                
#             elif instructions[i] == "R":
        