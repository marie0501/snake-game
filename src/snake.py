class Snake:

    def __init__(self, body):
        self.body = body
        self.current_direction = 'right'
        self.directions = {'right':[1,0], 'left':[-1, 0], 'up':[0,1], 'down':[0,-1]}
        self.die = False

    def move(self, surface):

        new_x = self.body[0][0] + self.directions[self.current_direction][0]
        new_y = self.body[0][1] + self.directions[self.current_direction][1]

        self.body.insert(0, [new_x,new_y])

        if self.eat(surface):
            return True

        self.body.pop()

        return True

     
    def change_direction(self, direction, surface):

        if not self.is_direction_valid(direction, surface):
            self.die = True
            return False

        self.current_direction = direction

        return True
    
    def eat(self, surface):
        return surface[self.body[0]]=='fruit'

    def is_direction_valid(self, direction, surface):
        
        new_x = self.body[0][0] + self.directions[direction][0]
        new_y = self.body[0][1] + self.directions[direction][1]

        return new_x >= 0 and new_x < surface.shape[0] and new_y >= 0 and new_y < surface.shape[1] and surface[new_x,new_y] != 'block' and surface[new_x,new_y] != 'snake'

        





    