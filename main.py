import picounicorn
import time
import random

picounicorn.init()
w = picounicorn.get_width()
h = picounicorn.get_height()

# Display a random colors across the Pi Unicorn
while True:
    for x in range(w):
        for y in range(h):
            x = random.choice(range(w))
            y = random.choice(range(h))
            r, g, b = color = list(random.choices(range(256), k=3))
            time.sleep(0.1)
            picounicorn.set_pixel(x, y, r, g, b)

    # Clear the display
    for x in range(w):
        for y in range(h):
            time.sleep(0.1)
            x = random.choice(range(w))
            y = random.choice(range(h))
            picounicorn.set_pixel(x, y, 0, 0, 0)