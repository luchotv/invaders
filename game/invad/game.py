import sys
import pygame
import os

from invad.fps_stats import FPSStats

class Game:

    __screen_size = (640,480)
    __game_title = 'Invaders!!!'

    __hero_image_filename = ['invad','assets', 'images', 'hero.png']
    __font_filename = ["invad", "assets", "fonts", "Sansation.ttf"]
    __font_size = 16
    __background_color = (15,15,30)
    __hero_Speed = 0.5
    __fps = 60

    def __init__(self):
        pygame.init()

        self.__window = pygame.display.set_mode(Game.__screen_size,0,32)
        pygame.display.set_caption(Game.__game_title)

        self.__hero_image = pygame.image.load(os.path.join(*Game.__hero_image_filename)).convert_alpha()

        self.__running = False
        my_font = pygame.font.Font(os.path.join(*Game.__font_filename), Game.__font_size)
        self.__fps_stats = FPSStats(my_font)

        self.__is_moving_up = False
        self.__is_moving_down = False
        self.__is_moving_right = False
        self.__is_moving_left = False

        self.__hero_position = pygame.math.Vector2(self.__window.get_width()/2, self.__window.get_height()/2)

        

    def run(self):
        self.__running = True

        fps_clock = pygame.time.Clock()
        while self.__running:
            delta_time = fps_clock.tick(Game.__fps)
            self.__process_events()
            self.__update(delta_time)
            self.__render()
        self.__quit()

    def __process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
            if event.type == pygame.KEYDOWN:
                self.__handle_player_input(event.key, True)
            elif event.type == pygame.KEYUP:
                self.__handle_player_input(event.key, False)

    def __update(self, delta_time):
        movement = pygame.math.Vector2(0.0, 0.0)

        if self.__is_moving_up:
            movement.y -= Game.__hero_Speed
        if self.__is_moving_down:
            movement.y += Game.__hero_Speed
        if self.__is_moving_right:
            movement.x += Game.__hero_Speed
        if self.__is_moving_left:
            movement.x -= Game.__hero_Speed
        
        self.__hero_position += movement * delta_time

        self.__fps_stats.update(delta_time)
        
    def __render(self):
        self.__window.fill(Game.__background_color)
        self.__window.blit(self.__hero_image,(self.__hero_position.xy))
        self.__fps_stats.render(self.__window)

        pygame.display.update()

    def __quit(self):
        pygame.quit()

    def __handle_player_input(self, key, is_pressed):
        if key == pygame.K_UP:
            self.__is_moving_up = is_pressed
        elif key == pygame.K_DOWN:
            self.__is_moving_down = is_pressed
        elif key == pygame.K_RIGHT:
            self.__is_moving_right = is_pressed
        elif key == pygame.K_LEFT:
            self.__is_moving_left = is_pressed
   