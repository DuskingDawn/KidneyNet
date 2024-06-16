# KidneyNet
A Deep Learning Framework for Kidney Disease Classification

## Description

Welcome to the KidneyNet project! This repository contains a machine learning pipeline designed to classify kidney diseases using CT scans. The project integrates MLOps practices, ensuring modularity, reproducibility, and scalability.

## Project Flow

![Setup](https://github.com/DuskingDawn/KidneyNet/assets/62723803/e4c88d98-ef6d-40a4-beca-4dab6990d29e)

## Dataset
You can find the dataset used in this project [here](https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone).

## Getting Started

### Using Virtual Environment

1. Clone the Project Repository
```
git clone https://github.com/your-username/kidney-net.git
cd kidney-net
```
2. Create and Activate a Virtual Environment
 ```
# Create a virtual environment
conda create -n env_name python==3.8

# Activate the virtual environment (Windows)
conda activate env_name

```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Run the Application
```
python src/main.py
```
### Using Docker
Prerequisites: Install Docker

1. Clone the Project Repository
```
git clone https://github.com/your-username/kidney-net.git
cd kidney-net
```
2. Build the Docker Image
 ```
docker build -t kidney-net-app .
```
3. Run the Docker Container
```
docker run -d -p 80:80 --name kidney-net-container kidney-net-app
```
4. Access the Application
```
Open a web browser and go to http://localhost.
```
## Report
A doc named 'Report' has been attached which showcases the results and the whole process of this project.

## Contact
Feel free to reach out if you have any questions or want to connect:

* [Twitter](https://twitter.com/Sneha_Kurmi)
* [Kaggle](https://www.kaggle.com/snehakurmi)
* [LinkedIn](http://www.linkedin.com/in/sneha-kurmi)
* [Email](kurmisneha9@gmail.com)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

