# Day 1 (Week 2)

## First problem statement

- Learn a function that can map the following input and output:

```
input = [0, 1, 2, 3, 4,...,50]
output = [0, 2, 4, 6, 8, ... , 100]
```

## Steps to solve the above problem

### Step 1: Define the problem statement

- Defining the problem statement clearly is a crucial step because it lays the foundation for everything that follows.
- **Identify the objective:** What do we want to predict or classify? Clearly state the outcome you're interested in.
- Define the input variables (features).

### Step 2: Collect the data (input and output [Supervisor])

### Step 3: For equation $y = θ_{1}*x$ pick any random value of $θ_{1}$ and calculate predicted output $\hat{y}$

- At the beginning of the process we don't know the optimal value of $θ_{1}$. Therefore we start by picking a random initial value of $θ_{1}$.
- It is chosen randomly because the model hasn't learnt anything yet.
- Picking random value for $θ_{1}$ is first step in the learning process, giving the model a starting point from which it can begin adjusting and learning from data.
- Using the $θ_{1}$ and $x$, we can calculate the $\hat{y}$ for all input samples.

### Step 4: Calculate the error

- After we initialize our model by picking random value of $θ_{1}$, next step is to calculate the error.
- Error measures the difference between predicted value of $\hat{y}$ and actual value of $y$.
- The goal is to minimize error overtime by adjusting model's parameter $θ_{1}$.
- Following is formula used to calculate
  - Absolute error: $|y_i - \hat{y}_i|$
  - Square error: $(y_i - \hat{y}_i)^2$

#### How to calculate cost?

- Following formula is used to calculate cost (absolute):

  - $\text{Cost} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$ where $n$ is total number of samples

- There is another formula that can be used to calculate cost (square):
  - $\text{Cost} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$

#### Why is calculating error important?

- The error gives feedback to the model about how well is it performing.
- The learning process involves minimizing the error.

#### Error and Cost

- Error typically refers to the difference between the predicted value $\hat{y}$ and the actual value $y$ for a single data point.
- The cost (or loss) is a more general term that refers to a function that aggregates the errors across all data points in our dataset.
- Error is typically about individual data points, whereas cost is about the aggregate performance across all data points.
- In general, error is more of a local concept (individual data points), and cost is a global concept (overall model performance).

### Final Step - Let's say we ran the same for 1000 different values of $θ_{1}$ and Cost was minimum when $θ_{1} = 2$

#### What is parameter?

- Parameter refers to a value that machine learns from training data.
- In this case $θ_{1}$ is our parameter.
- Parameter also determines the relationship between output predictions $\hat{y}$ and input features $x$.
  > _Note_: The goal is to find the optimal value of parameter so that the cost is minimum and thus machine can predict results more accurately.

#### What is epoch?

- Number of times experiments need to be performed.
- In our context, $epoch = 1000$

> _Note_: Let's say that we ran the experiment 1000 times and we didn't find the optimal value of $θ_{1} = 2$ then we can say that whatever value of $θ_{1}$ for which our cost was minimum will be our learning.

## How does machine store the learning?

### Equation

$\hat{Y} = \text{Weight}^{t} * X + \text{Bias}$

- In a simple linear regression model $y = θ_{0} + θ_{1}*x$, $θ_{0}$ and $θ_{1}$ are the parameters that are stored after training.
- In a other learning model, there might be millions of weights and biases that the model learns and stores.
- After training the model can be saved in various formats like matrix, `.pb`, `.h5`, `.pt` etc.
