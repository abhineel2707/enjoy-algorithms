# Day 2 (Week 2)

## Assignment

### What is the role of gradient descent in making machines learn?

- Gradient descent allows us to find the best value of parameters like $θ_{0}$ and $θ_{1}$ that minimizes the cost value thus improving the predicted value.
- If we keep on randomly assigning $θ_{0}$ and $θ_{1}$ then we might never find the minimum.
- In gradient descent:
  - Our goal is to find the best minimum (reach lowest point of slope).
  - We start at current position (random value for $θ_{0}$ and $θ_{1}$).
  - We can find the slope.
  - Based on the slope we'll take small steps downwards.
  - We repeat the process until we reach the lowest point.

### How do we decide the value of learning parameter $α$?

- The learning rate $α$ is hyperparameter.
- It determines the size of step the algorithm takes towards reaching min value of cost function.
- If the learning rate $α$ is too high, steps taken will be too large causing algorithm to overshoot the minimum.
- If the learning rate $α$ is too small, steps will be very small. It will ensure that algorithm `converges` but it might take a very long time to do so.
- An appropriate learning rate $α$ allows the algorithm to converge quickly to minimum without overshooting.
- Typical values of $α$ are [0.1, 0.01, 0.001] or in some cases $10^{-3}$ or even $10^{-4}$
- We need to execute some experiments to find the learning rate $α$. Common approach can be to start small and then increase gradually.

### Will gradient descent always help in finding the global minimum? If not, then how do you handle the possibility of getting stuck in a local minimum rather than a global minimum?

- Gradient descent does not always find the global minimum.
- We can adjust the learning rate $α$ and conduct multiple experiments.
- After running multiple experiments with different learning rates, we can compare the results (final cost value achieved in each run).
- We can then select "minimum of minimums" (global minimum).

### Do we need to change the value of the learning parameter in gradient descent? Are there any limitations or restrictions on the parameters, such as non-negativity constraints?

- If the provided learning rate $α$ doesn't provides optimal minimum, then we'll change the learning rate to get the global minimum.
- Yes, there are limitation or restrictions on learning parameter:
  - Non-negative. The learning rate $α$ should always be positive.

### How do you initialize the parameters? What impact does the choice of initialization have on the optimization process?

- Typical values of learning rate $α$ are [0.1, 0.01, 0.001] or in some cases $10^{-3}$ or even $10^{-4}$
- The choice of initialization can impact the optimization process:
  - Speed of convergence. If it is set too large then we'll overshoot the minimum (we might not be able to find the actual minimum) and if it is too small it will take a lot of iterations to reach the minimum (thus will need more compute resources as well).

### What are the stopping criteria for the optimization process? How do you determine when the optimization has converged? How can you ensure the optimization process is efficient and computationally feasible for large datasets?

- Stopping criteria are conditions that determine when the optimization process should terminate. It can be when we have reached maximum iterations (epochs) or when the parameter values stop changing.
- The goal is to stop the process when the model has sufficiently converged meaning that in further iterations the value of parameters ($θ_{0}$ and $θ_{1}$) do not change or we have exhausted max number of iterations.
- For large dataset optimizers like Adam can adjust the learning rate dynamically during training, which can lead to faster convergence. NAS can also be used to predict the learning rate and number of iterations.
