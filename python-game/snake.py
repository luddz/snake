import pygame
import time
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game')
game_over = False

x_pos = dis_width / 2
y_pos = dis_height / 2

snake_block = 10

x_delta = 0
y_delta = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])


while not game_over:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_delta = -10
                y_delta = 0
            elif event.key == pygame.K_RIGHT:
                x_delta = 10
                y_delta = 0
            elif event.key == pygame.K_UP:
                x_delta = 0
                y_delta = -10
            elif event.key == pygame.K_DOWN:
                x_delta = 0
                y_delta = 10

    if x_pos >= dis_width or x_pos < 0 or y_pos >= dis_height or y_pos < 0:
        game_over = True


    x_pos += x_delta
    y_pos += y_delta
    dis.fill(white)
    pygame.draw.rect(dis, black, [x_pos, y_pos, snake_block, snake_block])

    pygame.display.update()


    clock.tick(snake_speed)

message("You lost", red)
pygame.display.update()
time.sleep(2)


pygame.quit()
quit()
