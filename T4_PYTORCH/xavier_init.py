import math
import torch

def xavier_uniform(tensor, gain=1):
    fan_in, fan_out = _calculate_fan_in_and_fan_out(tensor)

    std = gain * math.sqrt(2.0 / fan_in + fan_out)
    a = math.sqrt(3.0) * std

    with torch.no_grad():
        return tensor.uniform_(-a, a)