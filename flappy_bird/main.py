from obstacles import *
from bird import *
import neat
import os

FPS = 30
width = 700
height = 500
pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
background = pygame.image.load('background.png')


def main(genomes, config):
    pygame.font.init()
    nets = []
    ge = []
    birds = []
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird(win, 50, math.floor(height / 2)))
        g.fitness = 0
        ge.append(g)
    obs = [Obstacle(win, 400), Obstacle(win, 800), Obstacle(win, 1200)]
    running = True
    score = 0
    STAT = pygame.font.SysFont("comicsans", 50)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        win.fill((0, 0, 0))
        win.blit(background, (0, 0))
        if len(birds) <= 0:
            break
        for x, bird in enumerate(birds):
            bird.show()
            bird.update()
            ge[x].fitness += 1
            if bird.die(obs[0]):
                ge[x].fitness -= 5
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)
                continue
            outputs = nets[x].activate((bird.y, obs[0].height, obs[0].height + obs[0].gap))
            if outputs[0] > 0.5:
                bird.jump()

        text = STAT.render("Score : " + str(score), 1, (0, 0, 255))
        text2 = STAT.render("Birds : " + str(len(birds)), 1, (0, 0, 255))
        for obstacles in obs:
            obstacles.show()
            obstacles.update()

        win.blit(text, (width - 10 - text.get_width(), 10))
        win.blit(text2, (10, 10))
        pygame.display.update()
        if obs[0].x <= 0:
            del obs[0]
            obs.append(Obstacle(win, 1200))
            score += 1
            for g in ge:
                g.fitness += 5


def run(c):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                c)
    p = neat.Population(config)
    p.run(main, 500)
    # print(winner)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "coonfiguration.txt")
    run(config_path)
