import numpy as np
import pandas as pd

# Palabras
palabras = ["feliz", "orgullo", "exito", "muerto", "desprecio", "inflacion","trabajo", "bondiola", "sanguche"]
positivas = ["feliz", "orgullo", "exito"]
neutras = ["trabajo", "bondiola", "sanguche"]
negativas = ["muerto", "desprecio", "inflacion"]

# Tweets
tweet1="Que desprecio que me genera el gobierno de Fernandez! Es impresionante la inflacion que se genero. Es un muerto! Aun con trabajo no podes vivir!"
tweet2="Estoy muy feliz, al fin me recibi de Ingeniero en Informatica, que orgullo!"
tweet3="Hoy tuve un gran dia en el trabajo, muy feliz de formar parte de esta empresa. El exito solo llega para quienes confian en el proceso. "
tweet4="Ayer me estaba comiendo un sanguche de bondiola, no saben lo orgulloso que estoy del buen trabajo del de la fiambreria. Este sanguche es un exito."

tweets = [tweet1, tweet2, tweet3, tweet4]

# Crea un vector con las palabras del tweet
def convertirTweet(tweet):
    vector = tweet.replace("!","").replace(",","").replace(".","").split(" ")
    return vector

# Crea el vector W a partir del tweet
def crearVectorW(tweet):
    vector = np.zeros(len(palabras)) # crea un vector de ceros con la longitud de palabras
    for palabra in tweet:
        if palabra in palabras:
            vector[palabras.index(palabra)] += 1
    return vector

# Crea el vector S a partir del tweet
def crearVectorS(tweet):
    vector = np.zeros(3)
    for palabra in tweet:
        if palabra in positivas:
            vector[0] += 1
        elif palabra in neutras:
            vector[1] += 1
        elif palabra in negativas:
            vector[2] += 1
    return vector

# Calcula el average de un vector
def average(vector):
    n = len(vector)
    escalar = 1/n
    return escalar * vector

# Calcula el score de un vector
def score(vector):
    valores = np.array([1, 0, -1])
    productoInterno = np.dot(valores, vector)
    return productoInterno

# Imprime las palabras, positivas, neutras y negativas
print("Palabras: ")
PPalabras = ", ".join(palabras)
print(PPalabras)
print()
print("Positivas: ")
PPositivas = ", ".join(positivas)
print(PPositivas)
print()
print("Neutras: ")
PNeutras = ", ".join(neutras)
print(PNeutras)
print()
print("Negativas: ")
PNegativas = ", ".join(negativas)
print(PNegativas)
print()

# Imprime los tweets, su average y su score
for index, tweet in enumerate(tweets):
    print(f"------------------- TWEET {index+1} ----------------------")
    print(tweet)
    print()
    tw = convertirTweet(tweet)
    w = crearVectorW(tw)
    s = crearVectorS(tw)
    print("Average: ")
    print(average(w))
    print()
    print("Score: ")
    print(score(s))
    print()
    print()