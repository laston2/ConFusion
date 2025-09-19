import configparser
import test_cases.generation as generation
import utils.calculations as calculations

from pathlib import Path
from scipy.spatial.distance import pdist, squareform

_config = configparser.ConfigParser()
_config.read(Path(__file__).with_name("config.ini"))
config = _config


def generate_tests(n_samples, noise):
    plot_data = True

    test_cases = generation.generate_test_cases(n_samples, noise)

    # Plots all data one after the other
    if plot_data:
        for test_data, colour in test_cases:
            generation.plot_data(test_data, colour)

    return test_cases

def setup_calculations(data):
    fully_connected = True

def main():
    data = config["data"]

    test_cases = generate_tests(int(data["n_samples"]), float(data["noise"]))

if __name__ == '__main__':
    try:
        main()
    except Excetpion as ex:
        print(ex)