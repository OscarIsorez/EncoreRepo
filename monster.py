import pygame
import random
import  animation


#créer une classe qui va gérer la notion de monstre sur notre jeu
import game


class Monster(animation.AnimateSprite) :

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health =100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount =10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed  = speed
        self.velocity = 0.5 + random.randint(0, 1)

    def set_loot_amount (self, amount ):
        self.loot_amount =  amount
    def damage(self, amount):
        #infliger les dégats
        self.health -= amount

        #vérifier si son nv nombre de point de vie est inférieur ou égal à 0

        if self.health <= 0 :
        #réapparaitre comme un nv monstre
            self.rect.x = 1000 + + random.randint(0, 300)
            self.velocity = 0.5 + random.randint(0, self.default_speed)
            self.health = self.max_health
            #ajouter le nombre de points
            self.game.add_score(self.loot_amount)

        #verifier si la barre dévenement est chargée au max
        if self.game.comet_event.is_full_loaded():
            #retirer du jeu
            self.game.all_monsters.remove(self)
        # appel de la methode pour essayer de déclencher la pluie de comète
            self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):

        #déssiner arriere plan
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])

        # déssiner la barre de vie
        pygame.draw.rect(surface, (111,210,46), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward (self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity

            # si le monstre est en collision avec le joueur
        else:
            # infliger des dégats ( au joueur)
            self.game.player.damage(self.attack)

#definir une class pour la momie
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount(20)

        
#definir une class pour l'alien
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(50)