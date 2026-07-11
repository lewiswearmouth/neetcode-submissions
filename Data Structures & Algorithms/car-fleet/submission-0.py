class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        '''

        position array -> where each car is

        speed array -> how fast each car is going

        target -> position goal

 

        if position[x] < position[y]:

            x cannot pass y

            can only speed[x] = speed[y]

            position[x] = position[y]

            add to car fleet

       

        each car is its own car fleet

        retunr number of fleets at destination

        '''

 

        position_speed = sorted(zip(position,speed), reverse = True) # sort in descending order for positions

       

        fleet = []

        for pos, speed in position_speed:

            # time is equal to the (target - curr_pos) / curr_speed

            time = (target - pos) / speed

            if fleet and fleet[-1] >= time:

                continue

            else:

                fleet.append(time)

 

        return len(fleet)