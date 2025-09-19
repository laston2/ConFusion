import matplotlib.pyplot as plt

import test_cases.manufactured.manifolds as manifolds

def close_figure_on_escape(event):
    if event.key == 'escape':
        plt.close(event.canvas.figure)

def plot_data(data, colour):
    fig = plt.figure()

    # 2D projection
    ax = fig.add_subplot(121)
    ax.scatter(data[:, 0], data[:, 2], c=colour)

    # 3D projection
    ax = fig.add_subplot(122, projection='3d')
    
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c=colour, s=50, alpha=0.8)
    ax.set_title("Swiss Roll")
    ax.view_init(azim=-66, elev=12)
    _ = ax.text2D(0.8, 0.05, s=f'n_samples={data.shape[0]}', transform=ax.transAxes)

    # Allow for 'ESC' key to close the figure
    fig.canvas.mpl_connect('key_press_event', close_figure_on_escape)
    plt.show()

def generate_test_cases(n_samples, noise):
    test_cases = []
    test_cases.append(manifolds.swiss_roll(n_samples, noise))

    return test_cases
