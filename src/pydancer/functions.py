import pygame

# image functions
def load_image(image_path):
    return pygame.image.load(image_path)

def display_image(screen, image, x, y):
    screen.blit(image, (x, y))

def scale_image(image, x, y):
    return pygame.transform.scale(image, (x, y))