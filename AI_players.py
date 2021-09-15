import numpy as np

screen_x = 1500
screen_y = 900


def outside_screen(coord_x, coord_y):
    if coord_x < 0:
        return True
    elif coord_x > screen_x:
        return True
    elif coord_y < 0:
        return True
    elif coord_y > screen_y:
        return True
    return False

def compute_dist(vectA, vectB):
    X2 = (vectA[0] - vectB[0])**2
    Y2 = (vectA[1] - vectB[1]) ** 2
    dist = np.sqrt(X2 + Y2)
    return dist

def move_toward(player, x, y, target_x, target_y, velocity=1):
    if target_x < x and target_y > y:
        if not outside_screen(x+velocity, y+velocity):
            player.move_downleft()
        else:
            return True
    elif target_x < x and target_y < y:
        if not outside_screen(x+velocity, y-velocity):
            player.move_upleft()
        else:
            return True
    elif target_x > x and target_y < y:
        if not outside_screen(x-velocity, y-velocity):
            player.move_upright()
        else:
            return True
    elif target_x > x and target_y > y:
        if not outside_screen(x-velocity, y+velocity):
            player.move_downright()
        else:
            return True
    elif target_x < x:
        if not outside_screen(x-velocity, y):
            player.move_left()
        else:
            return True
    elif target_x > x:
        if not outside_screen(x+velocity, y):
            player.move_right()
        else:
            return True
    elif target_y > y:
        if not outside_screen(x, y+velocity):
            player.move_down()
        else:
            return True
    elif target_y < y:
        if not outside_screen(x, y-velocity):
            player.move_up()
        else:
            return True
    return False

def return_info_per_players(player, game):
    enemies_coordinates = []
    # get the information about enemy location + their shoots and store it in a list (dictionnary per enemy)
    for ind, enemy in enumerate(game.all_players):
        if enemy.surname != player.surname: # enemy
            enemies_coordinates.append([enemy.rect[0], enemy.rect[1], enemy.rect[2], enemy.rect[3], enemy.rect.center, ind])
        else: # myself
            my_coordinates = [enemy.rect[0], enemy.rect[1], enemy.rect[2], enemy.rect[3], enemy.rect.center]
    return [enemies_coordinates, my_coordinates]

def closest(enemies_coordinates, my_coordinates):
    closest = 10000
    enemy_to_target = 0
    for enemy in enemies_coordinates:
        dist = compute_dist(my_coordinates[4], enemy[4])
        if closest > dist:
            closest = dist
            enemy_to_target = enemy
    if enemy_to_target == 0:
        return 0
    else:
        return enemy_to_target

##########################
#### AI BUILDING AREA ####
##########################

def AI_player(player, game, memory_AI_p1=None):
    '''Système AI pour le jeu AI_shooter

    Paramètres utilisables
    ----------

    Information:
    player.rect.x : coordonnée en abscisse
    player.rect.y : coordonnée en ordonnée

    Taille de l'image du joueur : 70

    Fonctions utilisables:

    player.move_right()
    player.move_left()
    player.move_up()
    player.move_down()
    player.move_upright()
    player.move_downright()
    player.move_upleft()
    player.move_downleft()

    return_info_per_players(player, game) : [[enemies_coordinates], my_coordinates]
            my_coordinates est sous la forme : [x, y, size_x, size_y, center]
            center est sous la forme : (x, y)


    closest(enemies_coordinates, my_coordinates) : abscisse et ordonnée de l'ennemi le plus proche
    retourne 0 si plus aucun ennemi

    move_toward(player, x, y, target_x, target_y, velocity) : dirige le robot dans la direction de la cible

    outside_screen(coord_x, coord_y) : True si point à abscisse x et ordonnée y en dehors de l'écran

    player.memory : liste, possibilité d'ajouter -.append(element)- ou retirer élément -.remove(element)- ou reset -player.memory = []-

    '''

    ### GET INFORMATION ###
    infos = return_info_per_players(player, game)
    enemies_coordinates = infos[0]
    my_coordinates = infos[1]

    x = my_coordinates[-1][0]
    y = my_coordinates[-1][1]


    ## ACTUAL AI ##
    move_toward(player, x, y, 500, 500)

    # return False => not to shoot
    return True # => ask to shoot

def AI_p_aggressive(player, game):
    move_toward(player, x, y, 500, 500)
    # return False # => not to shoot
    return True # => ask to shoot

def AI_p_passive(player, game):
    return False # => not to shoot
    # return True # => ask to shoot






