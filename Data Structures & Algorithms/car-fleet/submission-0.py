class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        for i in range(len(position)):
            stack.append((position[i],speed[i]))

        group_index=0
        sorted_stack=sorted(stack)

        while sorted_stack:
            pos, speed = sorted_stack.pop()
            time = (target-pos)/speed
            while sorted_stack:
                next_pos = sorted_stack[-1][0]
                next_speed = sorted_stack[-1][1]
                next_time = (target-next_pos)/next_speed
                if next_time <= time:
                    sorted_stack.pop()
                else:
                    break
            group_index+=1

        return group_index