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
        self.score = 0
        self.stay_time = 0
        self.lost_up = False
        self.lost_down = False

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
    num_birds = 1
    birds = [Bird() for _ in range(num_birds)]
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
    best_scores = [0] * num_birds
    current_scores = [0] * num_birds

    while True:
        generations += 1
        print(f"Generation: {generations}, Best Score: {max(best_scores)}")

        for i in range(num_birds):
            birds[i] = Bird()
            pipes = [Pipe(WIDTH)]
            run = True

            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                for pipe in pipes:
                    pipe.move(5)

                    bird_y = birds[i].y
                    pipe_x = pipe.x
                    pipe_top_y = pipe.height
                    pipe_bottom_y = pipe.height + 150

                    state = [bird_y, pipe_x, pipe_top_y, pipe_bottom_y, birds[i].vel]

                    if np.random.rand() < epsilon:
                        action = np.random.randint(2)
                    else:
                        action = np.argmax(model.predict(np.array([state])))

                    if action == 1:
                        birds[i].jump()

                    birds[i].move()

                    if birds[i].y > HEIGHT or birds[i].y < 0:
                        run = False
                        birds[i].lost_up = birds[i].y < 0
                        birds[i].lost_down = birds[i].y > HEIGHT

                    if pipe.x + 50 < 0:
                        pipes.pop(0)
                        new_pipe = Pipe(WIDTH)
                        pipes.append(new_pipe)
                        if pipe.x < birds[i].x:
                            birds[i].score += 1
                            birds[i].stay_time += 1
                        else:
                            birds[i].stay_time = 0

                    if birds[i].bird_img.colliderect(pipe.top_pipe) or birds[i].bird_img.colliderect(pipe.bottom_pipe):
                        run = False

                if not run:
                    if birds[i].lost_up or birds[i].lost_down:
                        reward = -100000
                    else:
                        reward = birds[i].score + birds[i].stay_time

                    if reward > best_scores[i]:
                        best_scores[i] = reward

                    target = reward

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
                birds[i].draw()
                for pipe in pipes:
                    pipe.draw()

                pygame.display.update()
                clock.tick(30)

if __name__ == '__main__':
    main()
