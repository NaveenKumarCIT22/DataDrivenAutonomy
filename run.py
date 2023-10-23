import pickle
import pygame
from newcar import Car 
import sys
# from detectStartStop import getSpots

WIDTH = 1920
HEIGHT = 1080
MAP = 'map3.png'

# Initialize Pygame
pygame.init()

# Set the display mode
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load the game map image after initializing Pygame and setting display mode
game_map = pygame.image.load(MAP).convert()

def load_best_network(filename):
    with open(filename, 'rb') as f:
        best_net = pickle.load(f)
    print("-- ",best_net)
    return best_net

if __name__ == "__main__":
    # Load the best neural network
    best_net = load_best_network('best_network.pickle')

    # Create a car with the loaded neural network
    car = Car()
    car.nets = [best_net]  # Replace the nets list with the loaded best_net

    clock = pygame.time.Clock()
    generation_font = pygame.font.SysFont("Arial", 50, True)
    alive_font = pygame.font.SysFont("Arial", 30, True)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        output = car.nets[0].activate(car.get_data())
        choice = output.index(max(output))
        if choice == 0:
            car.angle += 10 # Left
        elif choice == 1:
            car.angle -= 10 # Right
        elif choice == 2:
            if(car.speed - 2 >= 12):
                car.speed -= 2 # Slow Down
        else:
            car.speed += 2 # Speed Up

        # Update and draw the car using the loaded neural network
        car.update(game_map)
        screen.blit(game_map, (0, 0))
        if car.is_alive():
            car.draw(screen)
        else:
            print("Sethupochu !")
            break

        # Display Info
        text = generation_font.render("Data Driven Autonomy", True, (255,25,0))
        text_rect = text.get_rect()
        text_rect.center = (900, 450)
        screen.blit(text, text_rect)

        text = alive_font.render("Naveen Kumar.M and Arivarasan.A", True, (255,25,0))
        text_rect = text.get_rect()
        text_rect.center = (900, 490)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)
