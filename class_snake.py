import random
class Board():
    def __init__(self,size = (600, 600), color = 'lightred'):
        self.size = size
        self.color = color

class Snake():
    def __init__(self, size, color, coords,apple_coord):
        self.size = size
        self.color = color
        self.length = len(coords)
        self.coords = coords
        self.apple_coord = apple_coord
    def draw_snake(self, p,screen):
        for i in self.coords:
            p.draw.rect(screen, 'black', p.Rect(i[0], i[1], self.size,self.size))
            p.draw.rect(screen, 'white', p.Rect(i[0], i[1], self.size-3,self.size-3))
            p.draw.rect(screen, self.color, p.Rect(i[0], i[1], self.size-6,self.size-6))

    
    def snake_move(self, direction):
        if direction != (0, 0):
            self.coords.append([self.coords[-1][0]+self.size*direction[0],self.coords[-1][1]+self.size*direction[1]])
    
    def apple_generator(self, p, screen, apple_coord, placed):
        
        while self.apple_coord in self.coords and not placed:
            
            self.apple_coord = [random.randrange(20) * 20,random.randrange(20) * 20]
        else:
            p.draw.rect(screen, 'red', p.Rect(self.apple_coord[0],self.apple_coord[1], self.size,self.size))
            placed = True
        if placed and self.apple_coord in self.coords:
                self.length += 1
 
                placed = False
        return placed


               

# random variable for x and y coords of apple and then check if (apple coord in snake.coords)
# if it is then redo it until its not.


 

