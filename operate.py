import torch
import numpy as np

# abs
data = [-1, -2, 1, 2]
tensor = torch.IntTensor(data)

print(
    '\nsin',
    '\nnumpy', np.sin(data),
    '\ntorch', torch.sin(tensor)
)