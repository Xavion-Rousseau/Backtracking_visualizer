import pygame 
  
pygame.font.init() 
  
 
screen = pygame.display.set_mode((500, 500)) 

  
x = 0
y = 0
dif = 500 / 9
val = 0
grid =[ 
        [7, 8, 0, 4, 0, 0, 1, 2, 0], 
        [6, 0, 0, 0, 7, 5, 0, 0, 9], 
        [0, 0, 0, 6, 0, 1, 0, 7, 8], 
        [0, 0, 7, 0, 4, 0, 2, 6, 0], 
        [0, 0, 1, 0, 5, 0, 9, 3, 0], 
        [9, 0, 4, 0, 6, 0, 0, 0, 5], 
        [0, 7, 0, 3, 0, 0, 0, 1, 2], 
        [1, 2, 0, 0, 0, 7, 4, 0, 0], 
        [0, 4, 9, 2, 0, 6, 0, 0, 7] 
    ] 
  
font1 = pygame.font.SysFont("comicsans", 40) 
font2 = pygame.font.SysFont("comicsans", 20) 
def draw_box(): 
    for i in range(2): 
        pygame.draw.line(screen, (255, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7) 
        pygame.draw.line(screen, (255, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)    
  
def draw(): 
 
         
    for i in range (9): 
        for j in range (9): 
            if grid[i][j]!= 0: 
  
                pygame.draw.rect(screen, (0, 0, 250), (i * dif, j * dif, dif + 1, dif + 1)) 

                text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0)) 
                screen.blit(text1, (i * dif + 15, j * dif + 15))            
    for i in range(10): 
        if i % 3 == 0 : 
            thick = 7
        else: 
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick) 
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)       
  
def draw_val(val): 
    text1 = font1.render(str(val), 1, (0, 0, 0)) 
    screen.blit(text1, (x * dif + 15, y * dif + 15))     

def valid(m, i, j, val): 
    for it in range(9): 
        if m[i][it]== val: 
            return False
        if m[it][j]== val: 
            return False
    it = i//3
    jt = j//3
    for i in range(it * 3, it * 3 + 3): 
        for j in range (jt * 3, jt * 3 + 3): 
            if m[i][j]== val: 
                return False
    return True
def solve(grid, i, j): 
      
    while grid[i][j]!= 0: 
        if i<8: 
            i+= 1
        elif i == 8 and j<8: 
            i = 0
            j+= 1
        elif i == 8 and j == 8: 
            return True
    pygame.event.pump()     
    for it in range(1, 10): 
        if valid(grid, i, j, it)== True: 
            grid[i][j]= it 
            global x, y 
            x = i 
            y = j 
            
            screen.fill((255, 255, 255)) 
            draw() 
            draw_box() 
            pygame.display.update() 
            pygame.time.delay(20) 
            if solve(grid, i, j)== 1: 
                return True
            else: 
                grid[i][j]= 0
            screen.fill((255, 255, 255)) 
          
            draw() 
            draw_box() 
            pygame.display.update() 
            pygame.time.delay(50)     
    return False  
  
def result(): 
    return  
run = True
go = 0
go2 = 0
rs = 0
error = 0

while run: 
      
     
    screen.fill((255, 255, 255)) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            run = False  
        if event.type == pygame.MOUSEBUTTONDOWN: 
            go = 1
            pos = pygame.mouse.get_pos() 
            get_cord(pos) 
        if event.type == pygame.KEYDOWN: 
            
            if event.key == pygame.K_RETURN: 
                go2 = 1   
            
            
    if go2 == 1: 
        if solve(grid, 0, 0)== False: 
            error = 1
        else: 
            rs = 1
        go2 = 0    
         
    if rs == 1: 
        result()         
    draw()   
    if go == 1: 
        draw_box()        

    pygame.display.update()   
 
pygame.quit() 