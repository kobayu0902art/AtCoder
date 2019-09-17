import numpy as np

rd=np.random.randint(1,10000,(1,10000))
np.set_printoptions(formatter={'int': '{:04d}'.format},threshold=100000)
print(rd)