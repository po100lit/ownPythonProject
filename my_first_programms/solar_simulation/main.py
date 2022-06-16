import pygame
import math

pygame.init()

width, height = 900, 900
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Симуляция солнечной системы')
light_grey = (230, 230, 230)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 102, 0)
yellow = (255, 255, 0)
green = (0, 128, 0)
light_blue = (66, 170, 255)
blue = (0, 0, 255)
violet = (180, 0, 255)
dark_grey = (73, 66, 61)
scales = {1: 800, 2: 550, 3: 400, 4: 250, 5: 80, 6: 45, 7: 20, 8: 14}
num_of_planet = int(input('Сколько планет отобразить? (введите от 1 до 8): '))
font = pygame.font.SysFont('calibri', 16)


class Planet:
    au = 149.6e6 * 1000
    g = 6.67428 * 10 ** -11
    scale = scales[num_of_planet] / au
    timestep = 3600 * 24

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, game_window):
        x = self.x * self.scale + width / 2
        y = self.y * self.scale + height / 2

        # if len(self.orbit) > 1:
        #     updated_points = []
        #     for point in self.orbit:
        #         x, y = point
        #         x = x * self.scale + width / 2
        #         y = y * self.scale + height / 2
        #         updated_points.append((x, y))
        #
        #     pygame.draw.lines(game_window, self.color, False, updated_points, 1)

        pygame.draw.circle(game_window, self.color, (x, y), self.radius)

        # if not self.sun:
        #     distance_text = font.render(f'{round(self.distance_to_sun / 10 ** 9, 3)}  mln.km', 1, light_grey)
        #     game_window.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.g * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
        self.x_vel += total_fx / self.mass * self.timestep
        self.y_vel += total_fy / self.mass * self.timestep
        self.x += self.x_vel * self.timestep
        self.y += self.y_vel * self.timestep
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()

    # координата Х = +/- начальная отрисовка справа/слева от Солнца
    # earth.y_vel = +/- вращение против/по часовой стрелки

    sun = Planet(0, 0, Planet.scale * 11.5 ** 10, yellow, 1.98892 * 10 ** 30)
    sun.sun = True

    mercury = Planet(-0.387 * Planet.au, 0, sun.radius / 7, green, 0.33 * 10 ** 24)
    mercury.y_vel = 47.4 * 1000

    venus = Planet(-0.723 * Planet.au, 0, sun.radius / 4, orange, 4.8685 * 10 ** 24)
    venus.y_vel = 35.02 * 1000

    earth = Planet(-1 * Planet.au, 0, sun.radius / 4, light_blue, 5.9742 * 10 ** 24)
    earth.y_vel = 29.783 * 1000

    mars = Planet(-1.524 * Planet.au, 0, sun.radius / 4, red, 6.39 * 10 ** 23)
    mars.y_vel = 24.077 * 1000

    jupiter = Planet(-5.2 * Planet.au, 0, sun.radius / 2, light_grey, 1.8986 * 10 ** 27)
    jupiter.y_vel = 13.07 * 1000

    saturn = Planet(-9.58 * Planet.au, 0, sun.radius / 2, blue, 5.6846 * 10 ** 26)
    saturn.y_vel = 9.69 * 1000

    uran = Planet(-19.2 * Planet.au, 0, sun.radius / 5, violet, 8.6813 * 10 ** 25)
    uran.y_vel = 6.81 * 1000

    neptun = Planet(-30.1 * Planet.au, 0, sun.radius / 5, dark_grey, 1.0243 * 10 ** 26)
    neptun.y_vel = 5.4349 * 1000

    all_planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uran, neptun]
    planets = []
    for i in range(num_of_planet + 1):
        planets.append(all_planets[i])

    while run:
        clock.tick(60)
        game_window.fill(black)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for planet in planets:
            planet.update_position(planets)
            planet.draw(game_window)

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
