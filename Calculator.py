import time

# Creating a class called Block with attributes mass and velocity.
class Block:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity


def calc_velocities(v1, v2, m1, m2) -> tuple:
    """Returns the final velocities of two blocks after a perfectly elastic
    collision when their respective mass and initial velocities are given."""

    base = (((2 * (m1 * v1)) + v2 * (m2 - m1))/(m1 + m2))
    add = v2 - v1

    return add + base, base


# Number of digits of pi you want to compute to.
n = int(input("How many digits of pi do you want to compute?: "))


# Moving block with mass (100^(n-1))
B1 = Block(mass=(100**(n-1)), velocity=-1)

# Stationary block with mass 1 (units)
B2 = Block(mass=1, velocity=0)

running = True

collision_count = 0

if __name__ == '__main__':
    start = time.time()
    while running:
        # Stops the simulation when B2 and B1 are moving away from the wall and B1 has a higher speed than B2.
        if B1.velocity > B2.velocity >= 0:
            running = False

        else:
            # Calculating the velocities of the blocks after each elastic collision.
            B1.velocity, B2.velocity = calc_velocities(B1.velocity, B2.velocity, B1.mass, B2.mass)

            # Incrementing the collision count after every block-block collision.
            collision_count += 1

            if B2.velocity < 0:

                # Simulating B2 switching direction after colliding with wall.
                B2.velocity = -B2.velocity

                # Incrementing the collision count after every block-wall collision.
                collision_count += 1

    print("π =", (collision_count / (10 ** (n-1))))
    stop = time.time()
    print("It took", round(stop - start, 3), "seconds to compute", n, "digits of pi")
