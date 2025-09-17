import matplotlib.pyplot as plt
from sklearn import datasets

def swiss_roll():
    X, t = datasets.make_swiss_roll(n_samples=1000, noise=0.1)
    
    fig, ax = plt.subplots()
    ax.scatter(X[:, 0], X[:, 2], c=t)
    plt.show()