import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import  Alien


class AlienInvasion:
    def __init__(self):
        """Initializing the class AlienInvasion"""
        pygame.init()
        self.settings_game = Settings()
        self.screen = pygame.display.set_mode((self.settings_game.screen_width, self.settings_game.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """" Start the main loop for the game """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self.bullets.update()
            self._update_alien()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type ==pygame.KEYDOWN:
                if event.key ==pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key ==pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_q:
                    sys.exit()
    def _update_screen(self):
        self.screen.fill(self.settings_game.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _update_bullets(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings_game.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        current_x,current_y = alien_width , alien_height
        counterval = 1
        while current_y < (self.settings_game.screen_height-2 * alien_height):
            while current_x < (self.settings_game.screen_width-2 * alien_width):
                self._create_alien(current_x,current_y)
                current_x = current_x + 2 * alien_width
            current_x = alien_width
            current_y = current_y + 2 * alien_height
            counterval += 1
            if counterval == 4:
                break

    def _create_alien(self,x_pos,y_pos):
        new_alien = Alien(self)
        new_alien.x = x_pos
        new_alien.rect.x = x_pos
        new_alien.rect.y = y_pos
        self.aliens.add(new_alien)

    def _update_alien(self):
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings_game.fleet_drop_speed

        self.settings_game.fleet_direction = self.settings_game.fleet_direction * -1



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
