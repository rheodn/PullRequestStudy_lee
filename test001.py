import numpy as np

mean = 0
std = 1
size = 100

sample1 = np.random.normal(mean, std, size)
print("단일 표본 (100개):")
print(sample1)

mean = 0
std = 1
size = (100, 100)

samples = np.random.normal(mean, std, size)
print("\n100개의 표본 (100x100):")
print(samples)

sample_mean = np.mean(sample1)
sample_std = np.std(sample1, ddof=1)

z_value = 1.96
margin_of_error = z_value * (sample_std / np.sqrt(len(sample1)))
ci_lower = sample_mean - margin_of_error
ci_upper = sample_mean + margin_of_error

print(f"95% 신뢰구간: ({ci_lower:.3f}, {ci_upper:.3f})")
