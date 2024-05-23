# image-annotation-pipeline-with-AWS

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This project implements a comprehensive image annotation pipeline leveraging AWS, Apache Kafka and Airflow. It features a Flask web application where users can label images, which are then processed and uploaded to an S3 bucket. The pipeline ensures efficient data handling, real-time processing, and scalable storage for annotated image.

### Built With

Tech Stack used in this project
* [Apache Airflow](https://airflow.apache.org/)
* [kafka](https://kafka.apache.org/quickstart)
* [AWS](https://aws.amazon.com/)
* [Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/)


<!-- GETTING STARTED -->
## Getting Started

  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/ProgrammingOperative/image-annotation-pipeline-with-AWS.git
   ```


### Configurations directory setup: 
For security purposes, the configurations directory is important for masking of important credentials when working with cloud. You shall create your own directory and file locally following the structures below
- Within the route directory of this project, create the `configurations` directory and then the `annotations.config` file
   ```sh
   mkdir configurations
   cd configurations
   touch annotation.config

   ```
- within the *annotation.config* file have the following configuration format where you will replace the provided variable assignments to the actuals
   ```sh
    [AWS]
    ACCESS_KEY=XXXXXXXXXXXXXXXXXX
    SECRET_KEY=XXXXXXXXXXXXXXXXXX
    REGION=us-east-2
    BUCKET_NAME=XXXXXXXXXXXXXXXXX
    LABELED_IMAGE_BUCKET_NAME=XXXXXXXXXXXXXXX

   ```

### Data directory setup: 
Within this directory is where we shall have our image data stored on-premise. Just to be align with the notebooks I shall have my data directory structure build as below. Assuming I am in the root directory
   ```sh
    mkdir data
    cd data
    mkdir recived_images to_Send
   ```
You can however have your data directory structure as you wish

### AWS: 
  We first need the cloud infrastructure span
   ```sh
   - First, we shall create two s3 buckets that shall hold our initial image upload and another for the labeled one
   - Second, We shall spin up an ec2 and install kafka 
   - We shall then setup our lambda environment to trigger image transfer once an image is uploaded to s3

   ```
### WEB SERVER
  This is the flask application that we shall spin up to facilitate the viewing and actual image annotation
   ```sh
   cd web_application
   flask --app annotator run


   Navigate to `http://localhost:5000` on the browser once you have your server started

   ```

### Airflow: 
  Airflow is used for aurchestration and automation. This will automate thev uploading of our images files and shall act as the trigger for this whole pipeline
   ```sh
   Navigate to `http://localhost:8080/` on the browser once you have your airflow span
   use `admin` for username
   use `admin` for password

   If not the two credentials above, you can check your terminal once airflow is span, the credentials shall be provided there
   ```


 TO BE CONTINUED...