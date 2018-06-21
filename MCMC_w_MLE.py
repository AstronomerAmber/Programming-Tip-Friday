import numpy as np
import matplotlib.pyplot as plt

def GFIT(data,x):
    import emcee
    # Generate fake data
    #data = np.concatenate([np.random.uniform(low=-10, high=10, size=100), np.random.normal(size=400)])

    # Define likelihoods
    def lnprob(param, x):  # ln prob for an individual data point
        fracbkg, mean, sigma = param[0], param[1], param[2]
        low, high = -900., 900. # limits of the uniformly distributed background
        P = fracbkg / (high - low) + (1 - fracbkg) / (np.sqrt(2*np.pi)*sigma) * np.exp(-0.5*(x - mean)**2/sigma**2)
        # Above integrates to 1, assumption is that the [low, high] region is wide enough to contain the whole gaussian
        return np.log(P)

    def lnprobtot(param):  # ln prob for the whole data set (separating this just to help plotting the best model later)
        fracbkg, mean, sigma = param[0], param[1], param[2]
        if fracbkg < 0 or fracbkg > 1 or sigma < 0:
            return -np.inf  # parameters out of bounds
        return np.sum(lnprob(param, data))

    # run mcmc
    ndim, nwalkers, nsteps = 3, 10, 1000 #Number of dimensions in the parameter space, The number of walkers in the ensemble.
    pos = [[np.random.uniform(), np.random.uniform(low=-5, high=5),
            np.random.uniform(low=0, high=5)] for i in range(nwalkers)]  # starting points of walkers, note limits
                                                                         # for each parameter (0 to 1, -5 to 5, 0 to 5)
    sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprobtot)
    sampler.run_mcmc(pos, nsteps)
    samples = sampler.chain[:, nsteps/2:, :].reshape((-1, ndim)) # take second half of each chain, discard "burn-in"

    # print results
    meanpar = np.mean(samples, axis=0)
    stdpar = np.std(samples, axis=0)

    print "fraction of data in uniform background (true=0.2): %0.3f +- %0.3f" % (meanpar[0], stdpar[0])
    print "mean of gaussian (true=0):  %0.3f +- %0.3f" % (meanpar[1], stdpar[1])
    print "sigma of gaussian (true=1): %0.3f +- %0.3f" % (meanpar[2], stdpar[2])

    # plot results
    #h,  bins, _ = plt.hist(data, bins=20)
    #g2, bins, patches = plt.hist(data, bins=x,color = 'navy',alpha = 1.0, label='D$_{\mathrm{tran}}$ < 300 pkpc', linewidth=1)
    #x = np.linspace(-10, 10, 100)
    model = np.exp(lnprob(meanpar, x))
    model *= (x[1]-x[0]) * data.size # match units to histogram
    floor = (meanpar[0]/(900*2))*(x[1]-x[0]) * np.size(data)
    floore = (stdpar[0]/(900*2))*(x[1]-x[0]) * np.size(data)

    return model, floor, floore, meanpar[1], stdpar[1],meanpar[2], stdpar[2]
'''
x = np.linspace(-10, 10, 100)
#data = np.concatenate([np.random.uniform(low=-10, high=10, size=100), np.random.normal(size=400)])
model = GFIT(data,x)
plt.plot(x, model, color='black')
plt.show()
'''
