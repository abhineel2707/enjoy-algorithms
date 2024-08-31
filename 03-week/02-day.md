### How does Reinforcement Learning differ from supervised, unsupervised, and semi-supervised learning?

# Day 2 (Week 3)

## Assignment

### Why do we name different machine learning algorithms as supervised or unsupervised Learning?

- `Supervised learning` algorithms learn from dataset that contains both input and output.
- The goal is to learn a mapping function from inputs to outputs based on labelled dataset that is provided.
- The term supervised comes from the fact that the learning process is supervised by a "supervisor" (set of labelled data).
- `Unsupervised learning` algorithms learn from data that contains only input data without any labelled output.
- There is no supervisor for providing correct answers during training.
- The algorithm makes sense of data on its own and groups similar data together (clustering) or reduces dimensionality of data (principal component analysis - pca).

### Why is semi-supervised Learning the most common case in Machine Learning?

- In real world scenario obtaining large amount of labeled data is expensive and time consuming whereas unlabeled data is easy to acquire.
- `High cost and effort of labelling`: If my camera is configured to capture video at 20 fps, then 10 min video will have (20*60*10 = 12000) images. Effort of labelling will be huge both in terms of cost and time (on avg. a single annotation engineer can label approx. 1000 images in a day)
- `Semi-supervised` learning leverages small amount of labeled data to guide the learning process while using abundant amount of unlabeled data better understand the underlying data. This combination leads to better performance than using labeled data alone as acquiring labeled data is expensive (in terms of both time and cost).

### How can we utilize semi-supervised Learning in case of object detection problems?

- In object detection we want our model to look at an image and identify objects in it like finding a cat, a person or a car and drawing a box around them.
- To do this, we typically will need lot of images where each object has already been identified and marked by annotation engineer - this is our `labeled data`.
- However, getting labeled data is very expensive.
- Using `semi-supervised` learning we can train machine learning model by using small amount of labeled data (where we know correct answer) and a large amount of unlabeled data.
- We use small amount of unlabeled data to teach model what to look for, and then use model's own guesses on unlabeled data.
- These guesses are called `pseudo-labels` as they are not human verified.
- We combine original labeled data and high confidence pseudo labeled data to train the model again.

### Can we think of why supervised Learning can never bring the future we expect from Machine Learning?

- High cost and time for labelling.
- As the complexity increases the demand for labeled data also grows.
- Supervised learning can only learn from what it has been taught explicitly - it cannot go beyond labeled data. This limits its ability to generalize to new, unseen scenarios.
- If incorrect labeled data is provided then model will not perform well.

### Why is the annotation process required?

- It is required to create labeled datasets that are used to train models.
- Annotations provide necessary info that tells model what correct output should be for given input.
- Annotations serve as `ground truth` or `correct answers` that machine learning model uses to learn (supervised and semi-supervised learning).

### How can the same model be classified as both a supervised model and a classification model?

- Both supervised model and classification model use labeled data for training.

- A classification model is a supervised model designed to solve classification problems.

- Therefore, all classification models (discrete output) are supervised model but not all supervised models are classification model(discrete or continuous output).

| Supervised Model                                                             | Classification Model                                                 |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| A model that learns from labeled data (input/output) to map input to output. | A model that predicts discrete categories for input data.            |
| Uses labeled data to learn the relationship between input and output.        | Learns to assign input data to categories.                           |
| Minimizes difference between predicted output and actual.                    | Accurately categorizes input data to correct categories.             |
| Can produce continuous or discrete outputs.                                  | Always produces discrete outputs.                                    |
| Can be used for regression or classification.                                | Specifically designed for classification where output is a category. |
| Requires labeled data.                                                       | Requires labeled data.                                               |

### What distinguishes supervised Learning from unsupervised Learning?

| Supervised Learning                                                               | Unsupervised Learning                                            |
| --------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Labeled data (data with correct answers is provided).                             | Unlabeled data (no answer is provided).                          |
| Learns from data where correct answer is known.                                   | Learns by finding patterns or structures in data without labels. |
| Makes accurate predictions on new data like classifying or predicting.            | Discovers hidden patterns, groupings or structures in the data.  |
| Classification - eg: "cat" or "dog"<br/>Regression - eg: "predicting house price" | Clustering - customer segmentation                               |

### Can you explain the difference between classification and clustering?

| Classification                                                                        | Clustering                                                                                           |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Supervised learning(learns from labeled data with known outputs).                     | Unsupervised learning (learns from unlabeled data without any predefined outputs).                   |
| Uses labeled data for training.                                                       | Uses unlabeled data for training.                                                                    |
| It predicts class or category of new data points based on learning from labeled data. | It finds grouping or clusters in data by identifying patterns, similarities or differences.          |
| Produces discrete labels or categories (eg: "cat", "dog", "spam", "not spam")         | Produces clusters or groups of similar data without any predefined labels (eg: "Group A", "Group B") |

### How does Reinforcement Learning differ from supervised, unsupervised, and semi-supervised learning?

- Reinforcement learning is a type of machine learning where an agent learns by interacting with an environment, taking actions and receiving feedback in the form of rewards or penalties.
- The agent's objective is to learn a strategy that maximizes the cumulative reward over time.
- There are no predefined data sets.
- Model learns from interaction with environment by receiving feedback (reward or penalty).
- Examples: robotics, autonomous driving.

### How are Deep Learning and Neural Networks different?

- Neural networks: Good at recognizing complex relationship between input and output but struggle with temporal and spatial relationship.
- Deep Learning solves the temporal and spatial relationship problem.
- Temporal relationship involves data that is sequential and has dependencies over time such as stock prices that vary over time.
- Spatial relationship involves data where relationship between x and y varies according to distance between x and y. For example consider the sentence `I was born in Germany but currently residing in India, hence I can speak ___ fluently`.
