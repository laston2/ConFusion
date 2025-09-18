import test_cases.generation as generation

def generate_tests(n_samples, noise):
    plot_data = True

    manifolds = generation.generate_manifolds(n_samples, noise, plot_data)

def main():
    n_samples = 1000
    noise = 0.1

    tests = generate_tests(n_samples, noise)

if __name__ == '__main__':
    main()