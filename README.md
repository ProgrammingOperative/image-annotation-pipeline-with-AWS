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
* [Apache Airflow](https://jquery.com)
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

 TO BE CONTINUED...