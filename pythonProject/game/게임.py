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
background = pygame.image.load('../image/배경.png')
character_files = ['../image/제트.png', '../image/레이나.png', '../image/레이즈.png', '../image/세이지.png', '../image/스카이.png', '../image/오멘.png', '../image/피닉스.png']
characters=[pygame.image.load(file).convert_alpha() for file in character_files]


