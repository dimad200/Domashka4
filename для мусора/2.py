import pygame

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((800, 600))

# Загрузка спрайтов для анимации
walk_right = [
    pygame.image.load("walk_right_1.png"),
    pygame.image.load("walk_right_2.png"),
    pygame.image.load("walk_right_3.png")
]
walk_left = [
    pygame.image.load("walk_left_1.png"),
    pygame.image.load("walk_left_2.png"),
    pygame.image.load("walk_left_3.png")
]

# Начальный кадр анимации
current_frame = 0
animation_speed = 10  # Чем меньше число, тем быстрее анимация

# Начальные координаты спрайта
sprite_x = 400
sprite_y = 300

# Скорость движения спрайта
speed = 5

# Направление движения
direction = "right"

# Основной цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем состояние клавиш
    keys = pygame.key.get_pressed()

    # Движение вверх
    if keys[pygame.K_UP]:
        sprite_y -= speed

    # Движение вниз
    if keys[pygame.K_DOWN]:
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

    # Очистка экрана
    screen.fill((0, 0, 0))  # Черный фон

    # Выбор текущего кадра анимации
    current_frame = (current_frame + 1) % len(walk_right)
    if direction == "right":
        sprite_image = walk_right[current_frame // animation_speed]
    else:
        sprite_image = walk_left[current_frame // animation_speed]

    # Отображение спрайта
    screen.blit(sprite_image, (sprite_x, sprite_y))

    # Обновление экрана
    pygame.display.flip()

# Завершение программы
pygame.quit()