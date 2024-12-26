import pygame,sys


def sprite_map(file,size_x,size_y):
    sprites = []
    len_sprt_x = size_x
    len_sprt_y = size_y  # размер спрайта

    sprite = pygame.image.load(file)  # Загружаем файл
    sprite_rect = sprite.get_rect() # Запрос разрешения файла
    kartinok_v_stroke=int(sprite_rect.width/size_x)
    kartinok_v_stolbce = int(sprite_rect.height / size_x)
    print(kartinok_v_stroke, kartinok_v_stolbce)

    for nomer in range(kartinok_v_stroke):

        for i in range(kartinok_v_stolbce):
            sprite.set_clip(pygame.Rect(0 + len_sprt_x * nomer, 0 +len_sprt_y*i, len_sprt_x,len_sprt_y ))  # установите текущую область обрезки Поверхности
            a = sprite.subsurface(sprite.get_clip())  # получаем текущую область обрезки Поверхности
            sprites.append(a)

    return sprites

file ='sara 16x18 source.png'

s2=sprite_map(file,16,18)

print(len(s2))

# Загрузка спрайтов для анимации
walk_right = [s2[1],s2[5],s2[9]]
walk_left = [s2[3],s2[7],s2[11]]
walk_up = [s2[0],s2[4],s2[8]]
walk_down = [s2[2],s2[6],s2[10]]

# Начальный кадр анимации
current_frame = 0
animation_speed = 1  # Чем меньше число, тем быстрее анимация

# Начальные координаты спрайта
sprite_x = 400
sprite_y = 300

pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
clock = pygame.time.Clock()
x=0
# Направление движения
# Скорость движения спрайта
speed = 5
direction = "right"
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))
    # Получаем состояние клавиш
    keys = pygame.key.get_pressed()

    # Движение вверх
    if keys[pygame.K_UP]:
        direction = "up"
        sprite_y -= speed

    # Движение вниз
    if keys[pygame.K_DOWN]:
        direction = "down"
        sprite_y += speed

    # Движение вправо
    if keys[pygame.K_RIGHT]:
        direction = "right"
        sprite_x += speed

    # Движение влево
    if keys[pygame.K_LEFT]:
        direction = "left"
        sprite_x -= speed


    # Ограничение координат внутри экрана
    if sprite_x > 770:
        sprite_x = 770
    elif sprite_x < 30:
        sprite_x = 30
    if sprite_y > 570:
        sprite_y = 570
    elif sprite_y < 30:
        sprite_y = 30
    # for x in range(9):
    #     screen.blit(s2[x],(20*x+20, 20))

    screen.blit(s2[x], (20, 20))
    x += 1
    if x>35: x=0

        # Выбор текущего кадра анимации

    current_frame = (current_frame + 1) % len(walk_right)

    # new_image = pygame.transform.scale(image, (image.get_width() // 2, image.get_height() // 2)

    if direction == "right":
        for a in  range(100):
            if a==0:
                sprite_image = walk_right[current_frame]
            else:
                sprite_image = sprite_image

    elif direction == "up":
        sprite_image = walk_up[current_frame // animation_speed]

    elif direction == "down":
        sprite_image = walk_down[current_frame // animation_speed]

    else:
        sprite_image = walk_left[current_frame // animation_speed]

        # Отображение спрайта
    sprite_image_1=pygame.transform.scale(sprite_image, (sprite_image.get_width() * 4, sprite_image.get_height() * 4))
    screen.blit(sprite_image_1, (sprite_x, sprite_y))

    pygame.display.flip()
    clock.tick(60)