# Image Classifier Service

Image Classifier Service is a REST API application which written by Python (using Flask, uWSGI, Nginx, Keras, Tensorflow).\
Build an image classifier service for image classification tasks by transfer learning, use some pretrained model in Keras and Grad-CAM to interpret the results.\
List of available pretrained models in Keras (**[Link](https://keras.io/api/applications)**).

## Getting Started

These instructions will get you building and running the project on your local machine for development and testing purposes. See usage and supported commands for notes on how to use the application.

## Prerequisites

- Python3+
- Docker

## Setup
```bash
./bin/setup
```

## Run for development
- Start localhost server for development (included hot-reload)
```bash
./bin/run
```

## List of demos
- Dog Cat classification demo
```
http://localhost:8080/classifier/dogcat
```
![Demo1](/assets/dog.png "Demo1")
![Demo2](/assets/cat.png "Demo2")
![Demo3](/assets/dog_cat_1.png "Demo3")
![Demo4](/assets/dog_cat_2.png "Demo4")
![Demo5](/assets/dog_cat_3.png "Demo5")

- Flower classification demo (daisy, dandelion, rose, sunflower, tulip)
```
http://localhost:8080/classifier/flower
```

![Demo1](/assets/daisy.png "Demo1")
![Demo2](/assets/dandelion.png "Demo2")
![Demo3](/assets/rose.png "Demo3")
![Demo4](/assets/sunflower.png "Demo4")
![Demo5](/assets/tulip.png "Demo5")

- Covid19 classification demo (covid, normal, viral pneumonia)
```
http://localhost:8080/classifier/covid
```

![Demo1](/assets/covid_1.png "Demo1")
![Demo2](/assets/covid_2.png "Demo2")

- Facial expression demo (anger, contempt, disgust, fear, happy, sadness, surprise)
```
http://localhost:8080/classifier/emotion
```

![Demo1](/assets/happy.png "Demo1")
![Demo2](/assets/surprise.png "Demo2")

- Face detection demo with camera (frontal face with eyes)
```
http://localhost:8080/detector/face
```

## Run for production
```bash
./bin/deploy_prod <tag> [scale]
```

## Dataset
- Flowers (daisy, dandelion, rose, sunflower, tulip): https://www.kaggle.com/alxmamaev/flowers-recognition
- Covid19 (covid, normal, viral pneumonia): https://www.kaggle.com/pranavraikokte/covid19-image-dataset
- Facial expression small dataset (anger, contempt, disgust, fear, happy, sadness, surprise): https://www.kaggle.com/shawon10/ckplus

## License
This project is licensed under the MIT License - see the LICENSE file for details