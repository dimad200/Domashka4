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
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()
x=0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((255, 255, 255))

    # for x in range(9):
    #     screen.blit(s2[x],(20*x+20, 20))

    screen.blit(s2[x], (20, 20))
    x += 1
    if x>35: x=0


    pygame.display.flip()
    clock.tick(5)