# ==============================================================================
#   copyright (C) 2018 De Groskovskaja Marco
#
#   Licensed under the Apache License, Version 2.0;
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
# ==============================================================================

import sys, os.path
import pygame
from pygame.locals import *

#my Main script
import whoDaresWins
import generateClassifier


#If the model has not been trained yet
if not os.path.isfile("./model.ckpt.meta"):
    generateClassifier.trainclassifier()
else:
    pygame.init()

    ## SCREEN
    # Colors list
    GRAY = (197, 197, 197)
    BLACK = (0, 0, 0)
    DARK_GRAY = (107, 104, 99)
    WHITE = (255, 255, 255)
    DARK_GREEN = (58, 158, 73)

    # Screen area
    infoDisplay = pygame.display.Info()
    screen_weight = infoDisplay.current_w
    screen_height = infoDisplay.current_h
    windowSurface = pygame.display.set_mode((screen_weight, screen_height), pygame.FULLSCREEN)

    windowSurface.fill(WHITE)
    pygame.display.update()

    # brush setup
    brush_size = 10
    brush_color = BLACK

    # action setup
    draw = False
    NNpredictions = []

    # Dynamic size
    menu_margin 	= screen_weight/3
    button_margin 	= screen_height/8
    bottom_margin 	= screen_height/25
    text_margin_w	= button_margin/10
    text_margin_h	= menu_margin/8



    # font setup
    std_font_size	= int(bottom_margin/1.8)
    num_font_size	= int(button_margin)

    menu_font 	= pygame.font.Font("font/FreeSans.ttf", std_font_size)
    number_font	= pygame.font.Font("font/FreeSans.ttf", num_font_size)

    menu_text = menu_font.render("Digit Recognizer - Conv. NN. trained using MNIST - De Groskovskaja Marco - v5 - from 19/01/18 to 25/03/18", True, WHITE)
    clear_text = menu_font.render("Clear", True, WHITE)
    submit_text = menu_font.render("Submit", True, WHITE)



    # Menu and Drawing area
    menu_rect 	= pygame.Rect(screen_weight - menu_margin, 0, screen_weight, screen_height - bottom_margin)
    screen_rect = pygame.Rect(0, 0, screen_weight - menu_margin, screen_height - bottom_margin)
    submit_rect = pygame.Rect(screen_weight - menu_margin +1, screen_height - 2*button_margin -2 - bottom_margin, menu_margin, button_margin)
    clear_rect  = pygame.Rect(screen_weight - menu_margin +1, screen_height - button_margin -1 - bottom_margin, menu_margin, button_margin)
    bottom_rect = pygame.Rect(0, screen_height - bottom_margin, screen_weight, bottom_margin +1)

    number_margin	= menu_margin/4

    numbers_rect_01	= pygame.Rect(screen_weight - number_margin*4, 0, number_margin, number_margin)
    numbers_rect_02	= pygame.Rect(screen_weight - number_margin*3, 0, number_margin, number_margin)
    numbers_rect_03	= pygame.Rect(screen_weight - number_margin*2, 0, number_margin, number_margin)
    numbers_rect_04	= pygame.Rect(screen_weight - number_margin  , 0, number_margin, number_margin)

    predict_rect_01	= pygame.Rect(screen_weight - number_margin*4, 0 + number_margin +2, number_margin, number_margin)
    predict_rect_02	= pygame.Rect(screen_weight - number_margin*3, 0 + number_margin +2, number_margin, number_margin)
    predict_rect_03	= pygame.Rect(screen_weight - number_margin*2, 0 + number_margin +2, number_margin, number_margin)
    predict_rect_04	= pygame.Rect(screen_weight - number_margin  , 0 + number_margin +2, number_margin, number_margin)

    number_img_01	= DARK_GRAY
    number_img_02	= DARK_GRAY
    number_img_03	= DARK_GRAY
    number_img_04	= DARK_GRAY



    ## Main loop
    while True:

    	# Event Handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                draw = True
            if event.type == MOUSEBUTTONUP:
                draw = False

            
        # Drawing dot when mousebuttondown
        mouse_pos = pygame.mouse.get_pos()
        if draw == True and mouse_pos[0] < screen_weight - menu_margin:
            pygame.draw.circle(windowSurface, brush_color, mouse_pos, brush_size)


        ## Collision detection for SUBMIT  
        if draw == True:
            if submit_rect.collidepoint(mouse_pos):
                sub = windowSurface.subsurface(screen_rect)
                pygame.image.save(sub, "drawing_board.jpg")
                NNpredictions = whoDaresWins.get_predictions("./drawing_board.jpg")
                
                if os.path.exists("./extracted_img/dig_0.jpg"):
                    number_img_01 = pygame.image.load("./extracted_img/dig_0.jpg")
                    number_img_01 = pygame.transform.scale(number_img_01, (int(number_margin), int(number_margin)))
                else: number_img_01 = DARK_GRAY
                
                if os.path.exists("./extracted_img/dig_1.jpg"):
                    number_img_02 = pygame.image.load("./extracted_img/dig_1.jpg")
                    number_img_02 = pygame.transform.scale(number_img_02, (int(number_margin), int(number_margin)))
                else: number_img_02 = DARK_GRAY
                
                if os.path.exists("./extracted_img/dig_2.jpg"):
                    number_img_03 = pygame.image.load("./extracted_img/dig_2.jpg")
                    number_img_03 = pygame.transform.scale(number_img_03, (int(number_margin), int(number_margin)))
                else: number_img_03 = DARK_GRAY
                
                if os.path.exists("./extracted_img/dig_3.jpg"):
                    number_img_04 = pygame.image.load("./extracted_img/dig_3.jpg")
                    number_img_04 = pygame.transform.scale(number_img_04, (int(number_margin), int(number_margin)))
                else: number_img_04 = DARK_GRAY
    			

        ## collision detection for CLEAR
        if draw == True:
            if clear_rect.collidepoint(mouse_pos):
                pygame.draw.rect(windowSurface, WHITE, screen_rect)
                
        
        ## Re-draw the menu
        # Menu rect
        pygame.draw.rect(windowSurface, GRAY, menu_rect)
        
        # Bottom rect
        pygame.draw.rect(windowSurface, BLACK, bottom_rect)
        windowSurface.blit(menu_text, (0, screen_height - bottom_margin))
        

        # Blit the submit and clear rects
        pygame.draw.rect(windowSurface, DARK_GREEN, submit_rect)
        windowSurface.blit(submit_text, submit_rect.center)
        
        pygame.draw.rect(windowSurface, DARK_GREEN, clear_rect)
        windowSurface.blit(clear_text, clear_rect.center)
        
        
        ## Numbers rects
        # Drew
        if number_img_01 == DARK_GRAY:
            pygame.draw.rect(windowSurface, DARK_GRAY, numbers_rect_01)	    
        else: windowSurface.blit(number_img_01, numbers_rect_01)
        
        if number_img_02 == DARK_GRAY:
            pygame.draw.rect(windowSurface, DARK_GRAY, numbers_rect_02)	    
        else: windowSurface.blit(number_img_02, numbers_rect_02)
        
        if number_img_03 == DARK_GRAY:
            pygame.draw.rect(windowSurface, DARK_GRAY, numbers_rect_03)	    
        else: windowSurface.blit(number_img_03, numbers_rect_03)
        
        if number_img_04 == DARK_GRAY:
            pygame.draw.rect(windowSurface, DARK_GRAY, numbers_rect_04)	    
        else: windowSurface.blit(number_img_04, numbers_rect_04)
        
        # Predicted
        pygame.draw.rect(windowSurface, DARK_GRAY, predict_rect_01)
        pygame.draw.rect(windowSurface, DARK_GRAY, predict_rect_02)
        pygame.draw.rect(windowSurface, DARK_GRAY, predict_rect_03)
        pygame.draw.rect(windowSurface, DARK_GRAY, predict_rect_04)
        
        
        if number_img_01 != DARK_GRAY:
            predict_text_01 = number_font.render(str(NNpredictions[0]), True, WHITE)
            windowSurface.blit(predict_text_01, (screen_weight - number_margin*4, number_margin -10))
        
        if number_img_02 != DARK_GRAY:
            predict_text_02 = number_font.render(str(NNpredictions[1]), True, WHITE)
            windowSurface.blit(predict_text_02, (screen_weight - number_margin*3, number_margin -10))
        
        if number_img_03 != DARK_GRAY:
            predict_text_03 = number_font.render(str(NNpredictions[2]), True, WHITE)
            windowSurface.blit(predict_text_03, (screen_weight - number_margin*2, number_margin -10))
        
        if number_img_04 != DARK_GRAY:	
            predict_text_04 = number_font.render(str(NNpredictions[3]), True, WHITE)
            windowSurface.blit(predict_text_04, (screen_weight - number_margin, number_margin -10))
        
        

    		
        pygame.display.update()