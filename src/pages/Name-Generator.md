---
title: Name Generator
layout: contact.njk
subtitle: ""
metaDescription: name generation AI
date: 2017-01-01T00:00:00.000Z
permalink: /Name-Generator/index.html
eleventyNavigation:
  key: Name Generator
  order: 1
---

<html>
  <head>
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css"/>
  </head>
  <body>
  <py-script>
      import numpy as np
      import sys
      import random
      from keras.callbacks import LambdaCallback

      from tensorflow.keras.models import Sequential
      from tensorflow.keras.layers import Dense, Activation
      from tensorflow.keras.layers import LSTM
      from tensorflow.keras.optimizers import RMSprop

      with open('data/masc_brit_names.txt', 'r') as file:
          text = file.read().lower()
      print('text length', len(text))

      chars = sorted(list(set(text))) # getting all unique chars
      print('total chars: ', len(chars))

      char_indices = dict((c, i) for i, c in enumerate(chars))
      indices_char = dict((i, c) for i, c in enumerate(chars))

      maxlen = 40
      step = 3
      sentences = []
      next_chars = []
      for i in range(0, len(text) - maxlen, step):
          sentences.append(text[i: i + maxlen])
          next_chars.append(text[i + maxlen])

      x = np.zeros((len(sentences), maxlen, len(chars)), dtype=bool)
      y = np.zeros((len(sentences), len(chars)), dtype=bool)
      for i, sentence in enumerate(sentences):
          for t, char in enumerate(sentence):
              x[i, t, char_indices[char]] = 1
          y[i, char_indices[next_chars[i]]] = 1

      model = Sequential()
      model.add(LSTM(128, input_shape=(maxlen, len(chars))))
      model.add(Dense(len(chars)))
      model.add(Activation('softmax'))

      optimizer = RMSprop(learning_rate=0.01)
      model.compile(loss='categorical_crossentropy', optimizer=optimizer)


      def sample(preds, temperature=1.0):
          # helper function to sample an index from a probability array
          preds = np.asarray(preds).astype('float64')
          preds = np.log(preds) / temperature
          exp_preds = np.exp(preds)
          preds = exp_preds / np.sum(exp_preds)
          probas = np.random.multinomial(1, preds, 1)
          return np.argmax(probas)

      def on_epoch_end(epoch, logs):
          # Function invoked at end of each epoch. Prints generated text.
          print()
          print('----- Generating text after Epoch: %d' % epoch)

          start_index = random.randint(0, len(text) - maxlen - 1)
          for diversity in [0.2, 0.5, 1.0, 1.2]:
              print('----- diversity:', diversity)

              generated = ''
              sentence = text[start_index: start_index + maxlen]
              generated += sentence
              print('----- Generating with seed: "' + sentence + '"')
              sys.stdout.write(generated)

              for i in range(400):
                  x_pred = np.zeros((1, maxlen, len(chars)))
                  for t, char in enumerate(sentence):
                      x_pred[0, t, char_indices[char]] = 1.

                  preds = model.predict(x_pred, verbose=0)[0]
                  next_index = sample(preds, diversity)
                  next_char = indices_char[next_index]

                  generated += next_char
                  sentence = sentence[1:] + next_char

                  sys.stdout.write(next_char)
                  sys.stdout.flush()
              print()

      print_callback = LambdaCallback(on_epoch_end=on_epoch_end)

      from tensorflow.keras.callbacks import ModelCheckpoint

      filepath = "weights.hdf5"
      checkpoint = ModelCheckpoint(filepath, monitor='loss',
                                  verbose=1, save_best_only=True,
                                  mode='min')

                                  from tensorflow.keras.callbacks import ReduceLROnPlateau
      reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.2,
                                    patience=1, min_lr=0.001)

      callbacks = [print_callback, checkpoint, reduce_lr]

      model.fit(x, y, batch_size=128, epochs=3, callbacks=callbacks)

      def generate_text(length, diversity):
          # Get random starting text
          start_index = random.randint(0, len(text) - maxlen - 1)
          generated = ''
          sentence = text[start_index: start_index + maxlen]
          generated += sentence
          for i in range(length):
                  x_pred = np.zeros((1, maxlen, len(chars)))
                  for t, char in enumerate(sentence):
                      x_pred[0, t, char_indices[char]] = 1.

                  preds = model.predict(x_pred, verbose=0)[0]
                  next_index = sample(preds, diversity)
                  next_char = indices_char[next_index]

                  generated += next_char
                  sentence = sentence[1:] + next_char
          return generated

      print(generate_text(500, .9))
  </py-script>
  </body>
</html>