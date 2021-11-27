# central_limit_theorem

Tools to work with random variables and visualize the Central Limit Theorem. 

<img src="https://i.ibb.co/gyqFB9n/clt-unscaled.gif" width=400>

## Central Limit Theorem
The Central Limit essentially states that the sum of N independent, identically-distributed random variables converges to a Gaussian distribution as N goes to infinity. 

More precisely, 

![equation](https://latex.codecogs.com/gif.latex?%5Clim_%7Bn%5Crightarrow%20%5Cinfty%7D%20%5Cfrac%7BX_1%20&plus;%20X_2%20&plus;%20...%20&plus;%20X_n%20-%20n%5Cmu%7D%7B%5Csqrt%7Bn%7D%7D%20%3D%20%5Cmathcal%7BN%7D%280%2C%20%5Csigma%5E2%29)

## Adding Random Variables
Clearly, we need a way to add random variables. To keep things simple, we stick to discrete random variables. 

Adding two random variables involves two steps: adding up their possible values and convolving their probability distributions. For discrete random variables, we can just pass their probability mass functions to numpy.convolve().

Adding up their possible values is actually a bit trickier than it sounds. We need to list all combinations (cartesian product) of values between one random variable and the other. Then we add up the values. Finally, we remove duplicates to keep just the unique sums. 

The problem is that after we remove duplicates, we sometimes get a list of sums that looks like [-2, -1, -1.1942847e-16, 0, 1, 2]. And if we inspect the original combinations, we see things like [(-1, -1), (-1, 0.333333337), (-1, 0.3333333326)...]. We could round every number down to a few decimals, but even this breaks after several iterations. 

A more robust solution is to limit ourselves to integer random variables. This may sound restrictive, but it is easy to scale these values if we want to make plots with non-integer random variables. The important thing is that the internals for adding random variables only uses integers. Thus, our central class is IntegerRandomVariable. 
