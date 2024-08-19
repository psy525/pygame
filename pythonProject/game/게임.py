import time
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
character_files = ['../image/J.png', '../image/J.png', '../image/R.png', '../image/L.png', '../image/S.png', '../image/sky.png', '../image/O.png','../image/P.png']
characters=[pygame.image.load(file).convert_alpha() for file in character_files]
item= pygame.image.load("../image/구슬.png").convert_alpha()
life_item=pygame.image.load("../image/하트.png").convert_alpha()
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
character_y_default=character_y_pos

# 점프관련
max_jump=background_height
jump_start=0
jump_speed=8
gravity=2
fall_speed=5
is_jumping=False
is_falling=False

#방향키 관련
down_speed=5
max_down_distance=character_height/2
is_down=False
space_pressed_time = None
down_pressed_time = None

#todo 원래는 첫번째 캐릭터 고정해두려고 마지막에 000 넣은건데 필요없을 시 삭제
# 캐릭터별 색깔
character_color={
    (102, 153, 204): characters[1], # 제트
    (196,53,210): characters[2], # #레이나
    (255,100,68): characters[3], # #레이즈
    (199,244,194): characters[4], # #세이지
    (250,224,153): characters[5], # 스카이
    (60,74,201): characters[6], # #오멘
    (218,58,9): characters[7], # #피닉스
    (102, 153, 204): characters[0]
}

# 처음 시작시 캐릭터 고정
current_character=characters[0]

#todo 벽, 아이템, 공격 전부 x 위치 window_width로 바꾸기
# 공격위치
attack_size=attack.get_rect().size
attack_width=attack_size[0]
attack_height=attack_size[1]
attack_x_pos= window_width
attack_y_pos= random.randint(500, character_y_pos +200)
last_attack=time.time()
attack_interval=random.uniform(3,7)
attack_speed=1 # 칼 속도
attack_ready=False #바로생성x 일정 시간 준비 후  생성

#todo y_pos 체크하기
# 구슬위치
item_size=item.get_rect().size
item_width=item_size[0]
item_height=item_size[1]
item_x_pos= window_width
item_y_pos= random.randint(500, character_y_pos +200)
item_speed=1 # 칼 속도
last_item=time.time()
item_interval=random.uniform(5,10)
item_ready=False

#구슬 색깔 매핑
item_colors=list(character_color.keys())

#아이템 색상 변경함수
def colorized_image(image, color):
    colored_image = pygame.Surface((item_width, item_height), pygame.SRCALPHA)
    for x in range(item_width):
        for y in range(item_height):
            pixel_color = image.get_at((x, y))
            if pixel_color[3] != 0:
                new_color=(color[0], color[1], color[2], pixel_color[3])
                colored_image.set_at((x, y), new_color)
    return colored_image

#구슬 색깔 무작위로 선정
selected_color=random.choice(item_colors)

# 아이템 이미지 색상변경
item=colorized_image(item, selected_color)

#하트 아이템 6~12s
life_item_size=life_item.get_rect().size
life_item_width=life_item_size[0]
life_item_height=life_item_size[1]
life_item_x_pos=window_width
life_item_y_pos=random.randint(500, character_y_pos +200)
life_item_speed=1
last_life=time.time()
life_interval=random.uniform(6,12)
life_ready=False

# 장애물 위치
wall_size=wall.get_rect().size
wall_width=wall_size[0]
wall_height=wall_size[1]
wall_x_pos=window_width
wall_y_pos=window_height-wall_height
wall_speed=1
last_wall=time.time()
wall_interval=random.uniform(3,7)
wall_ready=False

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
    current_time=time.time()

#키보드 이벤트
    event_list = pygame.event.get()
    for event in event_list:
        #끄는 버튼(우측상단x) 눌림
        if event.type == pygame.QUIT:
            print("끄는 버튼 눌림")
            running = False

        #스페이스 누르면 점프
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping=True
                jump_start=character_y_pos
                space_pressed_time=time.time() #스페이스를 처음 누른 시간(3초이상 누르기 금지)
            if event.key == pygame.K_DOWN and not is_down:
                is_down=True
                down_pressed_time=time.time() #아래키  누른시간

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                is_jumping=False
                is_falling=True
                space_pressed_time=None #  스페이스바 누른시간 초기화
            if event.key == pygame.K_DOWN:
                is_down=False
                down_pressed_time=None  #아래키 시간 초기화

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        if space_pressed_time and time.time()-space_pressed_time>3: #3초 이상 눌렀다면
            is_jumping=False
            is_falling=True
            space_pressed_time=None
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        if down_pressed_time and time.time()-down_pressed_time>3:
            is_down=False
            down_pressed_time=None

#각종 캐릭터, 이벤트들 위치 계산
    #캐릭터  스페이스 눌렀을때 위치
    if is_jumping:
        if character_y_pos>jump_start-max_jump:
            character_y_pos=character_y_pos-jump_speed
        else:
            is_jumping=False
            is_falling=True
    if is_falling:
        if character_y_pos<character_y_default:
            character_y_pos=character_y_pos+fall_speed
        else:
            character_y_pos=character_y_default
            is_falling=False

    #캐릭터 다운키 눌렀을때 위치
    if is_down:
        if character_height<character_y_default+max_down_distance:
            character_y_pos=character_y_pos+down_speed
            if character_y_pos > character_y_default+character_height/2:
                character_y_pos = character_y_default+character_height/2
        else:
            character_y_pos=character_y_default+max_down_distance

    if not is_down and not character_y_pos<character_y_default:
        character_y_pos=character_y_pos+gravity
        if character_y_pos > character_y_default:
            character_y_pos = character_y_default

    #캐릭터 화면 벗어나지 못하게 조정
    if character_y_pos < 0:
        character_y_pos = 0
    if character_y_pos < max_down_distance:
        character_y_pos = max_down_distance

    #배경위치
    background_x_pos=background_x_pos-map_speed
    if background_x_pos <= - background_width:
        background_x_pos=0

    #칼 위치
    if attack_ready:
        attack_x_pos=attack_x_pos-attack_speed # 공격이 레디상태일 때에만 화면에 보이게 할 것

        #이미지가 화면 밖으로 나갔을때
        if attack_x_pos < -attack_width:
            attack_ready=False #공격 준비상태로 변경
            attack_x_pos=window_width
            last_attack=current_time
    if not attack_ready and current_time-last_attack>=attack_interval:
        attack_y_pos = random.randint(500, character_y_default + 200)
        attack_interval = random.uniform(3, 7)
        attack_ready=True

    #구슬위치
    if item_ready:
        item_x_pos=item_x_pos-item_speed
        if item_x_pos < -item_width:
            # 다시 오른쪽에서 생성
            item_ready=False
            item_x_pos=window_width
            last_item=current_time
            selected_color = random.choice(item_colors)
            item = colorized_image(item, selected_color)
    if not item_ready and current_time-last_item>=item_interval:
        item_y_pos=random.randint(500, character_y_default +200)
        #색상 변경
        selected_color=random.choice(item_colors)
        item=colorized_image(item,selected_color)
        #생성 시간
        item_interval=random.uniform(5,10)
        item_ready=True

    # 생명 아이템
    if life_ready:
        life_item_x_pos=life_item_x_pos-life_speed
        if life_item_x_pos < -life_item_width:
            life_ready=False
            life_item_x_pos=window_width
            last_life=current_time
    if not life_ready and current_time-last_life>=life_interval:
        life_y_pos=random.randint(500, character_y_default +200)
        life_interval = random.uniform(6,12)
        life_ready=True

    #벽 위치
    if wall_ready:
        wall_x_pos=wall_x_pos-wall_speed
        if wall_x_pos < -wall_width:
            wall_x_pos=window_width
            last_wall=current_time
    if not wall_ready and current_time-last_wall>=wall_interval:
        wall_interval=random.uniform(3,7)
        wall_ready=True

#충돌판정
    # character_rect=characters.rect().size
    character_rect = pygame.Rect(character_x_pos, character_y_pos, character_width, character_height)
    item_rect = pygame.Rect(item_x_pos, item_y_pos, item_width, item_height)

    if character_rect.colliderect(item_rect):
        current_character = character_color[selected_color]  # 충돌 시 캐릭터 변경
        #새로운 색상과 아이템 이미지 설정
        selected_color=random.choice(item_colors)
        item=colorized_image(item,selected_color)
        #아이템 위치와 타이머  속성 초기화
        item_x_pos = window_width  # 아이템 위치 초기화 (충돌 후 다시 시작)
        item_y_pos = random.randint(500, character_y_default + 200)


# 게임 룰
    # 구슬 색상 변경  #구슬 색상 변경 //구슬 색깔은 잘 변하나, 현재 실행시 바로 작동하는 문제 발생


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