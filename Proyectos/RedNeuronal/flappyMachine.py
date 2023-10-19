import pygame
import random
import tensorflow as tf
import numpy as np

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

    def draw(self):
        pygame.draw.rect(win, WHITE, self.top_pipe)
        pygame.draw.rect(win, WHITE, self.bottom_pipe)

def main():
    bird = Bird()
    pipes = [Pipe(WIDTH)]
    clock = pygame.time.Clock()

    learning_rate = 0.001
    discount_factor = 0.95
    epsilon = 0.1

    model = tf.keras.Sequential([
        tf.keras.layers.Dense(24, input_shape=(5,), activation='relu'),
        tf.keras.layers.Dense(2, activation='linear')
    ])
    optimizer = tf.keras.optimizers.Adam(learning_rate)

    generations = 0
    best_score = 0
    score = 0

    while True:  # Bucle para las generaciones
        generations += 1
        print(f"Generation: {generations}, Actual Score: {score} Best Score: {best_score}")

        bird = Bird()
        pipes = [Pipe(WIDTH)]
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            for pipe in pipes:
                pipe.move(5)

                bird_y = bird.y
                pipe_x = pipe.x
                pipe_top_y = pipe.height
                pipe_bottom_y = pipe.height + 150

                state = [bird_y, pipe_x, pipe_top_y, pipe_bottom_y, bird.vel]

                if np.random.rand() < epsilon:
                    action = np.random.randint(2)
                else:
                    action = np.argmax(model.predict(np.array([state])))

                if action == 1:
                    bird.jump()

                bird.move()

                if bird.y > HEIGHT or bird.y < 0:
                    run = False

                if pipe.x + 50 < 0:
                    pipes.pop(0)
                    pipes.append(Pipe(WIDTH))
                    score += 1

                if bird.bird_img.colliderect(pipe.top_pipe) or bird.bird_img.colliderect(pipe.bottom_pipe):
                    run = False

            if not run:
                target = score

                if score > best_score:
                    best_score = score

                model = tf.keras.Sequential([
                    tf.keras.layers.Dense(24, input_shape=(5,), activation='relu'),
                    tf.keras.layers.Dense(2, activation='linear')
                ])
                optimizer = tf.keras.optimizers.Adam(learning_rate)

                with tf.GradientTape() as tape:
                    predictions = model(np.array([state]))
                    loss = tf.reduce_sum(tf.square(target - predictions))
                grads = tape.gradient(loss, model.trainable_variables)
                optimizer.apply_gradients(zip(grads, model.trainable_variables))

            win.fill((0, 0, 0))
            bird.draw()
            for pipe in pipes:
                pipe.draw()

            pygame.display.update()
            clock.tick(30)

if __name__ == '__main__':
    main()
