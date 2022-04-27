def tf_text_generator(seed_text, num_of_words):
  assert num_of_words >= 0, "Number of words-to-be-generated must be non-negative."

  if (not seed_text) or (not num_of_words):
    return seed_text

  input_text_processor = input_sequences.input_text_processor

  input_vocab = np.array(input_text_processor.get_vocabulary(include_special_tokens=False))

  for _ in range(num_of_words):
    token = input_text_processor(seed_text)
    token = pad_sequences([token], 
                          maxlen = input_sequences.max_sequence_len - 1, 
                          padding='pre')
    predicted_logits = lstm.predict(token, verbose=0)
    predicted_logits = predicted_logits[0]

    # Sampling
    token = np.random.choice(label.shape[1], 1, replace=False, p = predicted_logits)[0]
    predicted_word = input_vocab[token]
    # print(f"predicted word = {predicted_word}")
    seed_text = seed_text + " " + predicted_word

  return  seed_text