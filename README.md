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

![Demo1](/assets/dog_cat_1.png "Demo1")
![Demo2](/assets/dog_cat_2.png "Demo2")

- Flower classification demo (daisy, dandelion, rose, sunflower, tulip)
```
http://localhost:8080/classifier/flower
```

![Demo1](/assets/flower_1.png "Demo1")
![Demo2](/assets/flower_2.png "Demo2")

- Covid19 classification demo (covid, normal, viral pneumonia)
```
http://localhost:8080/classifier/covid
```

![Demo1](/assets/covid_1.png "Demo1")
![Demo2](/assets/covid_2.png "Demo2")

## Run for production
```bash
./bin/deploy_prod <tag> [scale]
```

## Dataset
- Flowers (daisy, dandelion, rose, sunflower, tulip): https://www.kaggle.com/alxmamaev/flowers-recognition
- Covid19 (covid, normal, viral pneumonia): https://www.kaggle.com/pranavraikokte/covid19-image-dataset

## License
This project is licensed under the MIT License - see the LICENSE file for details