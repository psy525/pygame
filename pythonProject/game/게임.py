import pygame
import random

#이미지 넣기
pygame.init()

#화면크기
window_width=1920
window_height=1080
window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("피하기") # 제목

#맵, 캐릭터, 날라오는거, 장애물
background = pygame.image.load('../image/배경.png').convert_alpha()
character_files = ['../image/제트.png', '../image/레이나.png', '../image/레이즈.png', '../image/세이지.png', '../image/스카이.png', '../image/오멘.png', '../image/피닉스.png']
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

# 캐릭터 위치

# 공격위치

# 장애물 위치

# 하트 위치


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
            if event.key == pygame.K_LEFT:
                print ("<-화살표 눌림")
                to_x = to_x - character_speed
            elif event.key == pygame.K_RIGHT:
                print("->화살표 눌림")
                to_x = to_x + character_speed


#각종 캐릭터, 이벤트들 위치 계산



#충돌판정



# 게임 룰



# 렌더링


#반납
pygame.time.delay(1000) #2초 대기 후
pygame.quit() #아예 종료