Summary
Jay Shah, Meet Patel, and Daksh Vyas worked together on this project for the COMP2006 course. This project aims to show how a machine learning pipeline is created from start to finish and then deployed to a website. In order to complete the project, data from three distinct datasets must be gathered, processed, and analyzed. Machine learning models must be trained for both regression and classification tasks, and the predictions of the models must be displayed via a web interface.

Project Organization
The project repository is organized in a systematic manner.

scripts or notebooks for gathering data from several sources are included in the data collection section.
data processing: Consists of preprocessing, cleaning, and transformation code for the gathered data.
database: Consists of files or scripts linked to SQLite databases used to store the processed data.
models: Contains saved models and folders for every machine learning model that has been trained.
website: Contains the Flask-built web interface's code.
Readme.md: Offers usage instructions and a project description.
requirements.txt: Provides a list of all the packages needed to complete the project.


STEPS TO USE 

clone this repository:- git clone https://github.com/markcassar/COMP2006_project_Group_8.git
Install packages :- pip install -r requirements.txt
Open and run :- cd website
                python webpage.py


Pages on a Website
Homepage: gives a summary of the team members and the project.
Data Pages: Dedicated pages with example data from each dataset (weather, titanic, diabetes) are displayed.
Users can enter their data on the prediction page to receive predictions from the machine learning models that have been trained.

Data Entry and Model Development
Every dataset's data is gathered, examined, and kept in a SQLite database.
The savedmodels directory contains machine learning models that have been trained and saved for both regression and classification tasks.
When required, feature engineering and data pretreatment methods are used to enhance model performance.

Technologies Employed
Python: Used for model training, data processing, and website development throughout the project.
The web framework of choice for creating the interactive web interface is Flask.
SQLite: Used in relational databases to store processed data.


MEMBERS :- Jay Shah, Daksh Vyas, Meet Patel

