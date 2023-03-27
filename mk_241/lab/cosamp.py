import numpy as np


def cosamp(Phi, u, s, tol=1e-10, max_iter=1000):
    # https://github.com/avirmaux/CoSaMP/blob/master/cosamp.ipynb
    max_iter -= 1
    num_precision = 1e-12
    a = np.zeros(Phi.shape[1])
    v = u
    iter = 0
    halt = False
    while not halt:
        iter += 1
        print("Iteration {}\r".format(iter))
        y = abs(np.dot(np.transpose(Phi), v))
        Omega = [i for (i, val) in enumerate(y)
                 if val > np.sort(y)[::-1][2*s] and val > num_precision]
        T = np.union1d(Omega, a.nonzero()[0])
        b = np.dot( np.linalg.pinv(Phi[:,T]), u )
        iGood = ((abs(b) > np.sort(abs(b))[::-1][s])
                 & (abs(b) > num_precision))
        T = T[iGood]
        a[T] = b[iGood]
        v = u - np.dot(Phi[:,T], b[iGood])
        halt = ((np.linalg.norm(v)/np.linalg.norm(u) < tol)
                or (iter > max_iter))
    return a