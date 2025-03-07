"""
 * List of objects
 * based on ArrayListClass Daniel Shiffman.
 *
 * This example demonstrates how to use a Python list to store
 * a variable number of objects.    Items can be added and removed
 * from the list.
 *
 * Click the mouse to add bouncing balls.
"""

balls = []
ball_width = 48

# Simple bouncing ball class


class Ball:
    def __init__(self, temp_x, temp_y, temp_w):
        self.x = temp_x
        self.y = temp_y
        self.w = temp_w
        self.speed = 0
        self.gravity = 0.1
        self.life = 255

    def move(self):
        # Add gravity to speed
        self.speed = self.speed + self.gravity
        # Add speed to y location
        self.y = self.y + self.speed
        # If square reaches the bottom
        # Reverse speed
        if self.y > height:
            # Dampening
            self.speed = self.speed * -0.8
            self.y = height

        self.life -= 1

    def finished(self):
        # Balls fade out
        return self.life < 0

    def display(self):
        # Display the circle
        fill(0, self.life)
        # stroke(0,life)
        ellipse(self.x, self.y, self.w, self.w)


def setup():
    size(200, 200)
    smooth()
    no_stroke()

    # Start by adding one element
    balls.append(Ball(width / 2, 0, ball_width))


def draw():
    background(255)

    # Count down backwards from the end of the list
    for ball in reversed(balls):
        ball.move()
        ball.display()
        if ball.finished():
            balls.remove(ball)


def mouse_pressed():
    # A new ball object is added to the list (by default to the end)
    balls.append(Ball(mouse_x, mouse_y, ball_width))
