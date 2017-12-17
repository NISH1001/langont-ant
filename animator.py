#!/usr/bin/env python3

from ant import LangtonAnt
import matplotlib.pyplot as plt
from matplotlib import animation

class Animator:
    def __init__(self, ant):
        self.ant = ant

    def _animate(self, i):
        self.ant._step()
        self.img.set_data(self.ant.grid)
        return [self.img]

    def animate(self, num_frames=1000):
        fig = plt.figure()
        self.img = plt.imshow(self.ant.grid, interpolation='none', vmin=0, vmax=1)
        anim = animation.FuncAnimation(fig, self._animate,
                               frames=num_frames, interval=0, blit=True,
                               repeat=False)
        plt.show()


def main():
    ant = LangtonAnt(100)
    animator = Animator(ant)
    animator.animate(500)

if __name__ == "__main__":
    main()
