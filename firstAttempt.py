import sys, pygame

WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

y = HEIGHT/2
gravity = 1
deltaY = 0
black = [0, 0, 0]

class dirt:
    def __init__(self, x, y, yspeed):
        self.x = x
        self.y = y
        self.yspeed = gravity

    def draw(self):
        draw = pygame.draw.rect(WIN, (150,80,100), (self.x, self.y, 20, 20))



def main():
    pygame.init()
    
    run = True
    while run:
        global deltaY
        global mouseX
        global mouseY
        if(pygame.mouse.get_pressed()[0]):
            mouseX = pygame.mouse.get_pos()[0]
            mouseY = pygame.mouse.get_pos()[1]


        clock.tick(65)
        WIN.fill(black)
        
        

        Dirt = dirt((mouseX), (mouseY), 0)
        Dirt.draw()
        deltaY = Dirt.y
        deltaY += Dirt.yspeed
        Dirt.y = deltaY
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

                
        pygame.display.update()


if __name__ == "__main__":
    main()
