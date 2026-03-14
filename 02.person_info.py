import pygame
import random
import sys

# Инициализация на Pygame
pygame.init()

# Настройки на екрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)  # Цял екран
pygame.display.set_caption("Ловец на духове")

# Цветове
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Герой
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 10
player_health = 1000
player_attack = 1000

# Призраци
ghost_size = 30
ghost_speed = 2  # Намалена скорост
ghosts = []
ghost_health_base = 20
ghost_health_increase = 5
max_ghosts = 5  # Максимален брой призраци

# Предмети
items = []
item_effects = {"sword": 5, "armor": 10}

# Score и Level
score = 0
level = 1

# Анимация на атаката
is_attacking = False
attack_duration = 10  # Колко кадъра ще трае анимацията на атаката
attack_frame = 0

# Текст за щетите
damage_texts = []

# Бос
boss = None
boss_health = 100

# Функция за създаване на призраци
def create_ghost():
    if len(ghosts) < max_ghosts:  # Ограничаване на броя призраци
        ghost_x = random.randint(0, WIDTH - ghost_size)
        ghost_y = random.randint(0, HEIGHT - ghost_size)
        ghost_health = ghost_health_base + (score // 10) * ghost_health_increase
        ghosts.append([ghost_x, ghost_y, ghost_health])

# Функция за създаване на предмети
def create_item():
    item_x = random.randint(0, WIDTH - player_size)
    item_y = random.randint(0, HEIGHT - player_size)
    item_type = random.choice(list(item_effects.keys()))
    items.append([item_x, item_y, item_type])

# Функция за атака на призраци
def attack_ghosts():
    global score
    for ghost in ghosts:
        if (player_x < ghost[0] + ghost_size and player_x + player_size > ghost[0] and
                player_y < ghost[1] + ghost_size and player_y + player_size > ghost[1]):
            ghost[2] -= player_attack
            damage_texts.append([f"-{player_attack}", ghost[0], ghost[1], 30])  # Текст за щетите
            if ghost[2] <= 0:
                ghosts.remove(ghost)
                score += 1
                if score % 10 == 0:
                    level_up()

# Функция за повишаване на нивото
def level_up():
    global level, player_attack, player_health
    level += 1
    player_attack += 2
    player_health += 10

# Функция за създаване на бос
def create_boss():
    global boss, boss_health
    boss_x = random.randint(0, WIDTH - ghost_size * 2)
    boss_y = random.randint(0, HEIGHT - ghost_size * 2)
    boss_health = 100 + (level * 20)
    boss = [boss_x, boss_y, boss_health]

# Основен цикъл на играта
clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)

    # Обработка на събития
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Изход с ESC
                running = False

    # Движение на героя
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Атака на призраците
    if keys[pygame.K_SPACE]:
        is_attacking = True
        attack_frame = attack_duration
        attack_ghosts()

    # Анимация на атаката
    if is_attacking:
        if attack_frame > 0:
            pygame.draw.rect(screen, YELLOW, (player_x, player_y, player_size, player_size))
            attack_frame -= 1
        else:
            is_attacking = False
    else:
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))

    # Проверка за границите на екрана
    player_x = max(0, min(player_x, WIDTH - player_size))
    player_y = max(0, min(player_y, HEIGHT - player_size))

    # Създаване на призраци
    if random.randint(1, 100) < 3:  # Намалена честота на появяване
        create_ghost()

    # Движение и рисуване на призраците
    for ghost in ghosts:
        # Призраците се движат към героя
        if ghost[0] < player_x:
            ghost[0] += ghost_speed
        elif ghost[0] > player_x:
            ghost[0] -= ghost_speed

        if ghost[1] < player_y:
            ghost[1] += ghost_speed
        elif ghost[1] > player_y:
            ghost[1] -= ghost_speed

        # Проверка за границите на екрана
        ghost[0] = max(0, min(ghost[0], WIDTH - ghost_size))
        ghost[1] = max(0, min(ghost[1], HEIGHT - ghost_size))

        # Рисуване на призрака
        pygame.draw.rect(screen, RED, (ghost[0], ghost[1], ghost_size, ghost_size))

        # Проверка за сблъсък с героя
        if (player_x < ghost[0] + ghost_size and player_x + player_size > ghost[0] and
                player_y < ghost[1] + ghost_size and player_y + player_size > ghost[1]):
            player_health -= 1
            if player_health <= 0:
                running = False

    # Създаване на предмети
    if random.randint(1, 100) < 2:
        create_item()

    # Рисуване на предметите
    for item in items:
        pygame.draw.rect(screen, BLUE, (item[0], item[1], player_size, player_size))

        # Проверка за събиране на предмети
        if (player_x < item[0] + player_size and player_x + player_size > item[0] and
                player_y < item[1] + player_size and player_y + player_size > item[1]):
            if item[2] == "sword":
                player_attack += item_effects["sword"]
            elif item[2] == "armor":
                player_health += item_effects["armor"]
            items.remove(item)

    # Показване на текст за щетите
    for text in damage_texts:
        font = pygame.font.SysFont(None, 25)
        damage_surface = font.render(text[0], True, WHITE)
        screen.blit(damage_surface, (text[1], text[2]))
        text[3] -= 1
        if text[3] <= 0:
            damage_texts.remove(text)

    # Показване на информация за героя
    font = pygame.font.SysFont(None, 35)
    health_text = font.render(f"Health: {player_health}", True, WHITE)
    attack_text = font.render(f"Attack: {player_attack}", True, WHITE)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(health_text, (10, 10))
    screen.blit(attack_text, (10, 50))
    screen.blit(score_text, (10, 90))
    screen.blit(level_text, (10, 130))

    # Бос
    if score % 20 == 0 and score > 0 and boss is None:
        create_boss()

    if boss:
        # Движение на боса
        if boss[0] < player_x:
            boss[0] += ghost_speed
        elif boss[0] > player_x:
            boss[0] -= ghost_speed

        if boss[1] < player_y:
            boss[1] += ghost_speed
        elif boss[1] > player_y:
            boss[1] -= ghost_speed

        # Рисуване на боса
        pygame.draw.rect(screen, (255, 0, 255), (boss[0], boss[1], ghost_size * 2, ghost_size * 2))

        # Проверка за атака на боса
        if (player_x < boss[0] + ghost_size * 2 and player_x + player_size > boss[0] and
                player_y < boss[1] + ghost_size * 2 and player_y + player_size > boss[1]):
            player_health -= 2  # Босът нанася повече щети

    # Обновяване на дисплея
    pygame.display.flip()
    clock.tick(30)

# Изход от играта
pygame.quit()
sys.exit()