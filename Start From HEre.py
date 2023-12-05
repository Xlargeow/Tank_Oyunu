import pygame
import random


def main():
    pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Tank Oyunu')

    while True:
        tank_health = 100
        tank2_health = 100
        tank1_x = 200
        tank1_y = 200
        tank2_x = 600
        tank2_y = 200
        tank_speed = 5

        bullet_speed = 10
        bullet_width = 5
        bullet_height = 15
        bullet_color = (255, 255, 255)
        bullets = []

        font = pygame.font.Font(None, 36)
        font_large = pygame.font.Font(None, 72)
        win_message = None

        running = True
        game_over = False

        clock = pygame.time.Clock()
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()

            if game_over:
                if keys[pygame.K_r]:
                    game_over = False
                    tank_health = 100
                    tank2_health = 100
                    bullets = []  # Mermileri sıfırla
                    win_message = None  # Kazanan mesajını sıfırla
                elif keys[pygame.K_q]:
                    pygame.quit()
                    return

            if not game_over:
                if keys[pygame.K_w]:
                    tank1_y -= tank_speed
                if keys[pygame.K_s]:
                    tank1_y += tank_speed
                if keys[pygame.K_UP]:
                    tank2_y -= tank_speed
                if keys[pygame.K_DOWN]:
                    tank2_y += tank_speed
                if keys[pygame.K_SPACE]:
                    bullet = [tank1_x + 50, tank1_y + 25, 1, 0]
                    bullets.append(bullet)
                if keys[pygame.K_RETURN]:
                    bullet = [tank2_x - 5, tank2_y + 25, -1, 0]
                    bullets.append(bullet)

                screen.fill((0, 0, 0))
                pygame.draw.rect(screen, (255, 255, 255), (tank1_x, tank1_y, 50, 50))
                pygame.draw.rect(screen, (255, 255, 255), (tank2_x, tank2_y, 50, 50))

                bullets_to_remove = []
                for bullet in bullets:
                    pygame.draw.rect(screen, bullet_color, (bullet[0], bullet[1], bullet_width, bullet_height))
                    bullet[0] += bullet[2] * bullet_speed
                    if bullet[0] < 0 or bullet[0] > screen_width:
                        bullets_to_remove.append(bullet)
                for bullet in bullets_to_remove:
                    bullets.remove(bullet)

                tank1_health_text = font.render(f"Can: {tank_health}", True, (255, 255, 255))
                tank2_health_text = font.render(f"Can: {tank2_health}", True, (255, 255, 255))
                screen.blit(tank1_health_text, (10, 10))
                screen.blit(tank2_health_text, (screen_width - 150, 10))

                if tank_health <= 0:
                    win_message = font_large.render("Oyuncu 2 Kazandı!", True, (255, 0, 0))
                    game_over = True
                elif tank2_health <= 0:
                    win_message = font_large.render("Oyuncu 1 Kazandı!", True, (0, 255, 0))
                    game_over = True

                if win_message:
                    screen.blit(win_message, (screen_width // 2 - 200, screen_height // 2 - 50))

            pygame.display.flip()

            for bullet in bullets:
                if pygame.Rect(tank1_x, tank1_y, 50, 50).colliderect(
                        pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)):
                    tank_health -= 1
                    bullets.remove(bullet)
                if pygame.Rect(tank2_x, tank2_y, 50, 50).colliderect(
                        pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)):
                    tank2_health -= 1
                    bullets.remove(bullet)


if __name__ == "__main__":
    main()