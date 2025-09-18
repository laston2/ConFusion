from sklearn import datasets

def swiss_roll(n_samples, noise):
    return datasets.make_swiss_roll(n_samples=n_samples, noise=noise, random_state=42)
