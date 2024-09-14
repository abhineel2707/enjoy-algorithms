import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

mpl.style.use("seaborn-v0_8-darkgrid")


class ModelTrainerMAE:
    NUM_PARAMS = 3

    def __init__(
        self,
        lr=0.01,
        epochs=10000,
        seed=42,
        train_percent=80,
        patience=5,
        tolerance=1e-6,
    ):
        self.lr = lr
        self.epochs = epochs
        self.seed = seed
        self.train_percent = train_percent
        self.patience = patience
        self.tolerance = tolerance
        self.cost_per_epoch = []
        self.params = self.make_random_start(self.NUM_PARAMS)

    def make_random_start(self, total_nums):
        np.random.seed(self.seed)
        return np.random.rand(total_nums)

    def split_dataset(self, X, Y):
        idx = int((len(X) * self.train_percent) / 100)

        X_train, Y_train = X[:idx], Y[:idx]
        X_test, Y_test = X[idx:], Y[idx:]

        return X_train, Y_train, X_test, Y_test

    def prediction(self, X):
        Y_pred = self.params[0] + (self.params[1] * X) + (self.params[2] * (X**2))
        return Y_pred

    def train(self, X, Y):
        unchanged_count = 0
        prev_params = self.params.copy()

        for _ in range(self.epochs):
            cost = 0
            dJ_dtheta0, dJ_dtheta1, dJ_dtheta2 = 0, 0, 0

            for i in range(len(X)):
                Y_pred = self.prediction(X[i])
                error = Y_pred - Y[i]
                cost = cost + abs(error)

                if error > 0:  # Yp > Ya
                    dJ_dtheta0 = dJ_dtheta0 + 1
                    dJ_dtheta1 = dJ_dtheta1 + X[i]
                    dJ_dtheta2 = dJ_dtheta2 + (X[i] ** 2)
                elif error < 0:  # Yp < Ya
                    dJ_dtheta0 = dJ_dtheta0 - 1
                    dJ_dtheta1 = dJ_dtheta1 - X[i]
                    dJ_dtheta2 = dJ_dtheta2 - (X[i] ** 2)
                # if error == 0 do nothing

            # average
            cost = cost / len(X)
            self.cost_per_epoch.append(cost)

            self.params[0] = self.params[0] - ((self.lr * dJ_dtheta0) / len(X))
            self.params[1] = self.params[1] - ((self.lr * dJ_dtheta1) / len(X))
            self.params[2] = self.params[2] - ((self.lr * dJ_dtheta2) / len(X))

            if all(
                abs(self.params[i] - prev_params[i]) < self.tolerance for i in range(3)
            ):
                unchanged_count += 1
            else:
                unchanged_count = 0

            if unchanged_count >= self.patience:
                break

            prev_params = self.params.copy()

        return self.params, self.cost_per_epoch

    def plot_data(self, X_train, Y_train, X_test, Y_test):
        # plot training data
        plt.figure()
        plt.plot(X_train, Y_train, "*", color="red")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Training Data")
        plt.show()

        # plot test data
        plt.figure()
        plt.plot(X_test, Y_test, "o", color="red")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Testing Data")
        plt.show()

    def plot_cost(self):
        # plot cost per epoch
        plt.figure()
        plt.plot(self.cost_per_epoch)
        plt.ylabel("cost")
        plt.xlabel("epoch")
        plt.title("Cost per epoch")
        plt.show()

    def plot_predictions(self, X_test, Y_test):
        Y_pred_test = self.prediction(X_test)
        plt.figure()
        plt.plot(X_test, Y_test, "o", color="red", label="Actual")
        plt.plot(X_test, Y_pred_test, "*", color="blue", label="Predicted")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.legend()
        plt.title("Model Prediction")
        plt.show()


if __name__ == "__main__":
    # setup supervised dataset
    X = np.arange(-10, 10, 0.1)
    np.random.shuffle(X)
    Y_actual = (-2 * (X**2)) - X + 2 + (10 * np.random.normal(0, 1, len(X)))

    # create instance of ModelTrainer class
    model_trainer = ModelTrainerMAE(lr=0.01, epochs=100000)

    # split dataset into training and testing dataset
    X_train, Y_train, X_test, Y_test = model_trainer.split_dataset(X, Y_actual)

    # plot training and testing data
    model_trainer.plot_data(X_train, Y_train, X_test, Y_test)

    # train the model
    params, cost_per_epoch = model_trainer.train(X_train, Y_train)
    print(f"Trained params: {params}")

    # plot cost per epoch
    model_trainer.plot_cost()

    # plot model prediction
    model_trainer.plot_predictions(X_test, Y_test)
