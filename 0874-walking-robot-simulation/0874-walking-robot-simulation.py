class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # need to track changes in X and Y directions, to get final location
        # if command is -1, turn right 90 deg, meaning we go backwards in direction list
        # if command is -2 turn left 90 deg, meaning we go forwards in direction list
        # if command >0 then we move forward that number
        # can be blocked by obstacles so if hit an obstacle, stop moving
        # directions can be NSEW, N: +y, E: +x, S: -y, W: -x
        
        x,y=0,0 # init origin position
        points = []
        max_dist = 0
        
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        # -2 so we go forrwards in dicrections
        direction_index = 0
        obstacle_set = set(map(tuple,obstacles)) # map the tuple function on all obstacles and create a set
        for command in commands:
            if command == -1:  # Turn right 90 degrees
                direction_index = (direction_index + 1) % 4
            elif command == -2:  # Turn left 90 degrees
                direction_index = (direction_index - 1) % 4
            else:
                dx, dy = direction[direction_index]
                for i in range(command):
                    if(x + dx, y + dy) in obstacle_set:
                        break
                    x += dx
                    y += dy
                max_dist = max(max_dist, x**2 + y**2)
        return max_dist