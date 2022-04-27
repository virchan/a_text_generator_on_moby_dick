import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

class Moby_Input_Sequences():  
  def __init__(self, sentences):
    max_vocab_size = 5000

    input_text_processor = tf.keras.layers.TextVectorization(
    standardize = "lower_and_strip_punctuation",
    max_tokens = max_vocab_size)

    input_text_processor.adapt(sentences)

    input_sequences = []
    for sentence in sentences:
      token_sequence = input_text_processor(sentence)
      length = token_sequence.shape[0]

      for i in range(1, length):
        n_gram_sequence = token_sequence[:i+1]
        input_sequences.append(n_gram_sequence)

    # pad sequences 
    max_sequence_len = max([len(x) for x in input_sequences])
    input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))

    # create predictors and label
    predictors, label = input_sequences[:,:-1], input_sequences[:,-1]

    label = tf.keras.utils.to_categorical(label, num_classes=max_vocab_size)

    self.predictors = predictors
    self.label = label
    self.max_sequence_len = max_sequence_len
    self.input_text_processor = input_text_processor

  if __name__ == "__main__":
    import doctest
    doctest.testmod()