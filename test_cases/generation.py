import matplotlib.pyplot as plt

import test_cases.manufactured.manifolds as manifolds

def generate_manifolds(n_samples, noise, plot_data=False):
    data, colour = manifolds.swiss_roll(n_samples, noise)

    fig = plt.figure()

    # 2D projection
    ax = fig.add_subplot(121)
    ax.scatter(data[:, 0], data[:, 2], c=colour)

    # 3D projection
    ax = fig.add_subplot(122, projection='3d')
    
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=colour, s=50, alpha=0.8)
    ax.set_title("Swiss Roll in Ambient Space")
    ax.view_init(azim=-66, elev=12)
    _ = ax.text2D(0.8, 0.05, s="n_samples=1500", transform=ax.transAxes)
    plt.show()
