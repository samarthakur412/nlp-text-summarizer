from datasets import load_dataset

def load_data():

    dataset = load_dataset("cnn_dailymail", "3.0.0")

    train = dataset["train"]
    test = dataset["test"]

    return train, test