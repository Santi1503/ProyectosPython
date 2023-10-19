import pygame
import random

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

WHITE = (255, 255, 255)

class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.vel = 0
        self.gravity = 1
        self.jump_strength = -10
        self.bird_img = pygame.Rect(self.x, self.y, 50, 50)

    def jump(self):
        self.vel += self.jump_strength

    def move(self):
        self.vel += self.gravity
        self.y += self.vel
        self.bird_img = pygame.Rect(self.x, self.y, 50, 50)

    def draw(self):
        pygame.draw.rect(win, WHITE, self.bird_img)

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)
        self.top_pipe = pygame.Rect(self.x, 0, 50, self.height)
        self.bottom_pipe = pygame.Rect(self.x, self.height + 150, 50, HEIGHT - self.height - 150)

    def move(self, vel):
        self.x -= vel
        self.top_pipe = pygame.Rect(self.x, 0, 50, self.height)
        self.bottom_pipe = pygame.Rect(self.x, self.height + 150, 50, HEIGHT - self.height - 150)

def main():
    bird = Bird()
    pipes = [Pipe(WIDTH)]
    clock = pygame.time.Clock()

    generation = 1
    best_score = 0
    current_score = 0
    max_score = 0
    pipe_count = 0
    max_pipe_count = 0

    
    while True:
        bird = Bird()
        pipes = [Pipe(WIDTH)]
        pipe_count = 0
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            for pipe in pipes:
                pipe.move(5)

                bird_y = bird.y
                pipe_x = pipe.x
                pipe_top_y = pipe.height
                pipe_bottom_y = pipe.height + 150

                if bird.y > pipe.height and bird.y < pipe.height + 150:
                    bird.jump()

                if bird.bird_img.colliderect(pipe.top_pipe) or bird.bird_img.colliderect(pipe.bottom_pipe):
                    run = False

                bird.move()

                if pipe.x + 50 < 0:
                    pipes.pop(0)
                    pipes.append(Pipe(WIDTH))
                    pipe_count += 1
                    max_pipe_count = max(pipe_count, max_pipe_count)

                if bird.y < 0 or bird.y > HEIGHT:
                    run = False

                current_score = pipe_count
                best_score = max(current_score, best_score)
                max_score = max(max_score, current_score)

                print(f"Generation: {generation}, Current Score: {current_score}, Best Score: {best_score}, Max Score: {max_score}, Pipes Passed: {pipe_count}, Max Pipes Passed: {max_pipe_count}", end="\r")

                if not run:
                    generation += 1
                    print()

            clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
