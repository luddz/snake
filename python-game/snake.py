import pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)


dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game')
game_over = False

x_pos = 300
y_pos = 300

x_delta = 0
y_delta = 0

clock = pygame.time.Clock()

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

    x_pos += x_delta
    y_pos += y_delta
    dis.fill(white)
    pygame.draw.rect(dis, black, [x_pos, y_pos, 10, 10])

    pygame.display.update()


    clock.tick(30)

pygame.quit()
quit()
