from rouge import Rouge

def evaluate_model(predicted, reference):

    rouge = Rouge()

    scores = rouge.get_scores(predicted, reference)

    return scores