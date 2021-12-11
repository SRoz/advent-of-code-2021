import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.signal import convolve2d


""" Logic """
def step(input):
    octs = input + 1
    all_flashers = np.zeros_like(octs, dtype=bool)

    while (flashers := octs > 9).any():
        octs += convolve2d(flashers, np.array([[1,1,1],[1,0,1], [1,1,1]]), mode='same')
        all_flashers = flashers | all_flashers
        octs[all_flashers] = 0

    return octs, all_flashers.sum()

def part2(input):
    octs = np.array(input)
    n_steps = 0
    while not (octs==0).all():
        octs, _ = step(octs)
        n_steps += 1
    return n_steps


""" Plotting """
plt.rcParams["figure.figsize"] = [7.5, 5.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()
dimension = (10, 10)

def init():
    sns.heatmap(np.zeros(dimension), vmax=.8, cbar=False)

def animate(_):
    global octs
    octs, _ = step(octs)
    sns.heatmap(octs/10, vmax=.8, cbar=False)

def animated_plotter(input, n_steps):
    global octs
    octs = np.array(input)
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=n_steps+10, repeat=False)
    #plt.show()
    anim.save("day11/animation.gif", progress_callback=lambda i, n: print(f'Saving frame {i} of {n}') if i%10==0 else None )

if __name__=='__main__':
    with open("day11/inputs/input1.txt", "r") as f:
        input1 = [[int(n) for n in l if n!='\n'] for l in f.readlines()]
    n_steps = part2(input1)
    
    animated_plotter(input1, n_steps=n_steps)

    

    