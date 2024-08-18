import pygame
import random
import 위치설정
from test import current_character

print(위치설정.a)
위치설정.a = 6
print(위치설정.a)
#이미지 넣기
pygame.init()

#화면크기
window_width=1920
window_height=1080
window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("피하기") # 제목

#맵, 캐릭터, 날라오는거, 장애물
background = pygame.image.load('../image/배경.png').convert_alpha()
character_files = ['../image/J.png', '../image/J.png', '../image/R.png', '../image/L.png', '../image/S.png', '../image/sky.png', '../image/O.png','../image/P.png']
characters=[pygame.image.load(file).convert_alpha() for file in character_files]
item= pygame.image.load("../image/구슬.png").convert_alpha()
wall=pygame.image.load("../image/벽.png").convert_alpha()
attack=pygame.image.load("../image/칼.png").convert_alpha()
life=pygame.image.load("../image/하트.png").convert_alpha()
game_font=pygame.font.SysFont('오뮤 다예쁨체', 48)

#맵만들기
background_size=background.get_rect().size
background_width=window.get_rect().size[0]
background_height=window.get_rect().size[1]
background_x_pos=0
background_y_pos=0
map_speed=0.5 #맵이 왼쪽으로 움직이는 속도

# 캐릭터 위치
character_sizes=[character.get_rect().size for character in characters]
character_width=character_sizes[0][0]
character_height=character_sizes[0][1]
character_x_pos=60
character_y_pos= (window_height-character_height) + 10
jump=0

# 캐릭터별 색깔
character_color={
    (102, 153, 204): characters[1], # 제트
    (196,53,210): characters[2], # #레이나
    (255,100,68): characters[3], # #레이즈
    (199,244,194): characters[4], # #세이지
    (250,224,153): characters[5], # 스카이
    (60,74,201): characters[6], # #오멘
    (218,58,9): characters[7], # #피닉스
    (0, 0, 0): characters[0]
}

# 처음 시작시 캐릭터 고정
current_character=characters[0]



# 공격위치
attack_size=attack.get_rect().size
attack_width=attack_size[0]
attack_height=attack_size[1]
attack_x_pos= window_width-attack_width
attack_y_pos= character_y_pos+45
attack_speed=1 # 칼 속도


# 구슬위치
item_size=item.get_rect().size
item_width=item_size[0]
item_height=item_size[1]
item_x_pos= window_width-item_width
item_y_pos= character_y_pos -200
item_speed=1 # 칼 속도

#구슬 색깔
item_colors={
    (102, 153, 204), # 제트
    (196,53,210), # 레이나
    (255,100,68), # 레이즈
    (199,244,194), #세이지
    (250,224,153), # 스카이
    (60,74,201), # 오멘
    (218,58,9), # 피닉스
}


# 장애물 위치
wall_size=wall.get_rect().size
wall_width=wall_size[0]
wall_height=wall_size[1]
wall_x_pos=window_width-wall_width
wall_y_pos=window_height-wall_height
wall_speed=1

# 하트 위치
life_size=life.get_rect().size
life_width=life_size[0]
life_height=life_size[1]
life_x_pos=40
life_y_pos=60
life_speed=5

#최대목숨 설정
max_life=5
lifes=[life]*max_life

#총플레이
score=0
hit_count=0

###########
#메인루프
running = True

while running:

#키보드 이벤트
    event_list = pygame.event.get()
    for event in event_list:
        #끄는 버튼(우측상단x) 눌림
        if event.type == pygame.QUIT:
            print("끄는 버튼 눌림")
            running = False

        #스페이스 누르면 점프
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump=character_y_pos

                print ("점프")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jump=0


#각종 캐릭터, 이벤트들 위치 계산
    #캐릭터 위치
    character_y_pos=character_y_pos+jump

    #배경위치
    background_x_pos=background_x_pos-map_speed
    if background_x_pos <= - background_width:
        background_x_pos=0

    #칼 위치
    attack_x_pos=attack_x_pos-attack_speed

    #구슬위치
    item_x_pos=item_x_pos-item_speed

    #벽 위치
    wall_x_pos=wall_x_pos-wall_speed

    #하트위치



#충돌판정
    # character_rect=characters.rect().size


# 게임 룰
    # 구슬 색상 변경  #구슬 색상 변경 //구슬 색깔은 잘 변하나, 현재 실행시 바로 작동하는 문제 발생
    def colorized_image(image, color):
        colored_image=pygame.Surface((item_width, item_height), pygame.SRCALPHA)

        for x in range(item_width):
            for y in range(item_height):
                pixel_color=image.get_at((x,y))
                if pixel_color !=(0,0,0,0):
                    colored_image.set_at((x,y), color)
        return colored_image


    # 색상에 맞는 이미지로 변경

    # 구슬에 충돌할때 점수 증가

    # 하트가 다 사라지면 게임오버 및 점수 보여주기


# 렌더링
    window.blit(background,(background_x_pos,background_y_pos))
    # 충돌시 일치하는 이미지 들어가게 설정
    window.blit(current_character, (character_x_pos,character_y_pos))
    window.blit(attack, (attack_x_pos, attack_y_pos))
    window.blit(item, (item_x_pos,item_y_pos))
    window.blit(wall, (wall_x_pos,wall_y_pos))

    for i in range(max_life-hit_count):
        window.blit(lifes[i], (life_x_pos,100+ i*(life_y_pos+30)))

    pygame.display.update()

#반납
pygame.time.delay(1000) #2초 대기 후
pygame.quit() #아예 종료