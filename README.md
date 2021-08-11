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

## Run for production
```bash
./bin/deploy_prod <tag> [scale]
```

## Dataset


## License
This project is licensed under the MIT License - see the LICENSE file for details