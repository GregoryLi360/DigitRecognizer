import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

models = [keras.models.load_model("mnistCNNmodel2.h5")]

# model1=keras.models.load_model("mnistCNNmodel2.h5")
model1=models[0]

def predict_image(x, model): #takes in 3D Numpy array that represents an image
  x = x.astype('float32') 
  x/=255.0 #converts to 0-1 float scale

  x = np.expand_dims(x, axis=0) 

  image_predict = model.predict(x, verbose=0)

  # plt.imshow(np.squeeze(x))
  # plt.xticks([])
  # plt.yticks([])
  # plt.show()
  print("Predicted Label: ", np.argmax(image_predict))
  return image_predict

def plot_value_array(predictions_array, true_label):
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array[0], color="#777777")
  plt.ylim([-1, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')
  plt.show()

def eval(path):
  # img=image.load_img(path,target_size=(28,28),color_mode="grayscale")
  # img_arr=image.img_to_array(img)
  # img=tf.keras.utils.load_img(path,target_size=(28,28),color_mode="grayscale")
  img=tf.keras.utils.load_img(path,target_size=(28, 28),color_mode="grayscale")
  img.show()
  img_arr=tf.keras.utils.img_to_array(img)
  arr=predict_image(img_arr, model1)
  plot_value_array(arr,3)

def predictImages(x, models):
  list = []
  for m in models:
    list.append(predict_image(x, m))
  return list

def evalAvg(path): 
  img=tf.keras.utils.load_img(path,target_size=(28, 28),color_mode="grayscale")
  img.show()
  img_arr=tf.keras.utils.img_to_array(img)
  arrs=predictImages(img_arr, models)
  arr=np.mean(np.array(arrs), axis=0)
  plot_value_array(arr, 3)