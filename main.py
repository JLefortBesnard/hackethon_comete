import pygame
from game import Game
from AI_players import AI_p_passive, AI_p_aggressive, AI_player
from radar import Radar
import time, random

screen_x = 1500
screen_y = 900

# function to explode outside player
def check_if_outside_screen(coord_x, coord_y, screen_x, screen_y):
    output = False
    if coord_x < 0:
        return True
    elif coord_x > screen_x:
        return True
    elif coord_y < 0:
        return True
    elif coord_y > screen_y:
        return True
    return False

def deploy_AI(AI, player, nb_player, t_j, screen):
    if t_j != None:
        t_j = float(t_j)
    if nb_player == 1:
        global txt
        global winner_surname
        txt = "{} WON the game".format(player.surname)
        winner_surname = player.surname
        txt_pause = pygame.font.SysFont('Consolas', 32).render(txt, True, pygame.color.Color('White'))
        screen.blit(txt_pause, (10, 30))
        game_over = True
    else:
        game_over = False
    if AI and player.shoot_av:
        player.launch_projectile()
        t_j = time.time()
    elif not player.shoot_av:
        if time.time() > t_j + 2:
            player.recharge_weapon()
    return game_over, t_j

# création de l explosion
def explosion(x, y, screen):
    explosion_img = pygame.image.load("assets/explosion.png")
    explosion_img = pygame.transform.scale(explosion_img, (70, 70))
    screen.blit(explosion_img, (x, y))


def Main(pool, screen, background, screen_x, screen_y):
    # charger le jeu
    game = Game(pool)
    players_list_start =  [player.surname for player in game.all_players]
    game_over = False

    start_ticks = pygame.time.get_ticks()
    running = True
    # boucle tant que la condition est vraie
    while running:
        pygame.time.wait(25) # change game speed, higher == slower

        # print(game.pressed)
        # applique l'arriere plan
        screen.blit(background, (0, 0))

        # check if some players are dead
        players_list_current = [player.surname for player in game.all_players]
        if len(players_list_current) != len(players_list_start):
            # define txt to display
            deads = "Dead : {}".format(set(players_list_start) - set(players_list_current))
            deads_display = pygame.font.SysFont('Consolas', 10).render(deads, True, pygame.color.Color('red'))
            # # draw the text
            screen.blit(deads_display, (10, screen_y-50))


        # applique l'image du joueur
        nb_player = len(game.all_players)
        for player in game.all_players: # test for not empty
            screen.blit(player.image, player.rect)
            if player.surname == 'J1':
                if "t_j1" not in locals():
                    game_over, t_j1 = deploy_AI(AI_player(player, game), player, nb_player, None, screen)
                else:
                    game_over, t_j1 = deploy_AI(AI_player(player, game), player, nb_player, t_j1, screen)

            elif player.surname == 'J2':
                if "t_j2" not in locals():
                    game_over, t_j2 = deploy_AI(AI_p_passive(player, game), player, nb_player, None, screen)
                else:
                    game_over, t_j2 = deploy_AI(AI_p_passive(player, game), player, nb_player, t_j2, screen)

            elif player.surname == 'J3':
                if "t_j3" not in locals():
                    game_over, t_j3 = deploy_AI(AI_p_passive(player, game), player, nb_player, None, screen)
                else:
                    game_over, t_j3 = deploy_AI(AI_p_passive(player, game), player, nb_player, t_j3, screen)

            elif player.surname == 'J4':
                if "t_j4" not in locals():
                    game_over, t_j4 = deploy_AI(AI_p_aggressive(player, game), player, nb_player, None, screen)
                else:
                    game_over, t_j4 = deploy_AI(AI_p_aggressive(player, game), player, nb_player, t_j4, screen)



            if check_if_outside_screen(player.rect.center[0], player.rect.center[1], screen_x, screen_y):
                player.remove()
        if not game_over:
            # recuperer les projectiles du joueur
            for player in game.all_players:
                for projectile in player.all_projectiles:
                    boom = projectile.move()
                    if len(boom) != 0:
                        for coords in boom:
                            explosion(coords[0], coords[1], screen)

            # appliquer l'ensemble des images de mon groupe projectiles
            for player in game.all_players:
                player.all_projectiles.draw(screen)
            time_to_stop = time.time()


        else:
            if time.time() > time_to_stop + 3:
                running = False
                game.all_players.empty()
                for player in game.all_players:
                    player.all_projectiles.empty()




        # si le joueur ferme la fenètre
        for event in pygame.event.get():
            # que levenement est femerture de fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("fermeture du jeu")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    for radar_per_player in game.all_players:
                        # drawing radar
                        radar = Radar(screen_x, screen_y)
                        list_of_coordinates = []
                        for player in game.all_players:
                            if player.surname != radar_per_player.surname:
                                list_of_coordinates.append([player.rect[0], player.rect[1], player.rect[2], player.rect[3], 'red'])
                                for projectile in player.all_projectiles:
                                    list_of_coordinates.append([projectile.rect[0], projectile.rect[1], projectile.rect[2], projectile.rect[3], "red"])
                            else:
                                list_of_coordinates.append([player.rect[0], player.rect[1], player.rect[2], player.rect[3], 'green'])
                                for projectile in player.all_projectiles:
                                    list_of_coordinates.append([projectile.rect[0], projectile.rect[1], projectile.rect[2], projectile.rect[3], "green"])
                        for coord in list_of_coordinates:
                            radar.create_rectangle(coord[0],coord[1], coord[2], coord[3], coord[4])
                        radar.define_title(radar_per_player.surname)
                        radar.show()

                elif event.key == pygame.K_n:
                    for player in game.all_players:
                        player.print_surname(screen)


        pygame.display.flip()
    return winner_surname



if __name__ == '__main__':
    pygame.init()
    screen_x = 1500
    screen_y = 900
    # generer la fenetre
    pygame.display.set_caption("AI_Shoot")
    screen = pygame.display.set_mode((screen_x, screen_y))
    background = pygame.image.load("assets/bg.jpg")

    P1 = [
        'J1',  # player1_name
        'assets/J1.png',  # player1_picture_path
        'assets/J1_weapon.png',  # player1_projectile_path
        'J1'  # surname
    ]
    P2 = [
        'J2',  # player1_name
        'assets/J2.png',  # player1_picture_path
        'assets/J2_weapon.png',  # player1_projectile_path
        'J2',  # surname

    ]
    P3 = [
        'J3',  # player1_name
        'assets/J3.png',  # player1_picture_path
        'assets/J3_weapon.png',  # player1_projectile_path
        'J3',  # surname
    ]
    P4 = [
        'J4',  # player1_name
        'assets/J4.png',  # player1_picture_path
        'assets/J4_weapon.png',  # player1_projectile_path
        'jeremy',  # surname
    ]
    pool1 = [P1, P2, P3, P4]
    Main(pool1, screen, background, screen_x, screen_y)

