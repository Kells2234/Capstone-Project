# streaming-05-smart-smoker
This project implements a data producer for streaming sensor data from a smart smoker system. The sensor data is stored in a CSV file, and the producer reads this data and sends it to RabbitMQ queues. The data includes temperature readings for the smoker itself and two food items (Food A and Food B), with readings taken every 30 seconds.

<br>Author: Kelly Simmons</br>
<br>Date: 09/29/23</br>


## Getting Started


 
Before running the producer, ensure the following requirements are met:

- RabbitMQ server is running.
- The `pika` library is installed in your active Python environment.

## The key features of this project include:

- Reading sensor data from the CSV file.
- Sending data to RabbitMQ queues with specified queue names.
- Simulating sensor data streaming at a rate of one value every 30 seconds.
- Opening the RabbitMQ Admin website for queue monitoring.


## How to Use

**To use the producer, follow these steps:**

1. Clone this repository to your local machine.
2. Make sure RabbitMQ is running.
3. Install the `pika` library if not already installed (`pip install pika`).
4. Execute the `bbq_producer.py` script.
5. Open the RabbitMQ Admin website for queue monitoring.
6. The producer will start sending sensor data to the specified queues.

[RabbitMQ Tutorial - Work Queues](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)


## The following modules are used in this project:
<br> csv	
<br> webbrowser
<br> signal	
<br> sys	
<br> time	
<br> pika
<b>  socket

## Prerequisites
<br>Git
<br>Python 3.10+ 
<br>VS studio Code 
<br>anaconda prompt (miniconda3)
<br>RabbitMQ


## Multiple Terminals Screenshots
![Alt text](<Screenshot 2023-10-03 191306.png>)
![Alt text](<Screenshot 2023-10-03 191330.png>)
![Alt text](<Screenshot 2023-10-03 191344.png>)


## RabbitMQ WebInterface screenshot:
![Alt text](<Screenshot 2023-10-02 174239.png>)










