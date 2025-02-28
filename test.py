import numpy as np

height = 1.84

swell_beginners = [float(round(sb, 10)) for sb in np.arange(1.2,2.6,0.01)]
if height in swell_beginners:
    print(True)