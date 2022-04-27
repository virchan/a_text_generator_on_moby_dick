import tensorflow as tf

class Moby_LSTM(tf.keras.Model):
  
  def __init__(self, max_sequence_len):
    super().__init__(self)

    # Embedding Layer
    self.embedding = tf.keras.layers.Embedding(5000, 
                                    100, 
                                    input_length = max_sequence_len-1)
    
    # Bidirectional LSTM Layer
    self.bi_lstm = tf.keras.layers.Bidirectional(
                tf.keras.layers.LSTM(256, 
                                      return_sequences = True))
    
    # A Dropout Layer
    self.dropout = tf.keras.layers.Dropout(0.2)

    # An LSTM Layer
    self.lstm = tf.keras.layers.LSTM(256)

    # A Dense Layer including regularizers
    self.dense = tf.keras.layers.Dense(5000, 
                                       activation = "relu", 
                                       kernel_regularizer = tf.keras.regularizers.l2(0.01))
    
    # The Output Layer
    self.classifier = tf.keras.layers.Dense(5000, 
                                activation = "softmax")
    
  def call(self, inputs):
    x = self.embedding(inputs)
    x = self.bi_lstm(x)
    x = self.dropout(x)
    x = self.lstm(x)
    x = self.dense(x)

    return self.classifier(x)

  if __name__ == "__main__":
    import doctest
    doctest.testmod()