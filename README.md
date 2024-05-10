# Cherry Leaf Mildew

This app provides insight into the health of cherry trees by assessing whether their leaves contain powdery mildew or not.

The Live link is [here](https://pp5mildew-e3fe6b06a0ce.herokuapp.com/).

Objectives:

Conduct a visual analysis of healthy and powdery mildew-infected cherry leaves to discern differences.
Predict the presence of powdery mildew in cherry leaves from real-time images.
The outcomes of this project are accessible on a dashboard - the live link is here.

Dataset Overview:

The dataset originates from Kaggle. A hypothetical user story was then constructed to apply predictive analytics to a practical scenario.

This dataset comprises over 4,000 images captured from the client's cherry orchards. These images depict both healthy cherry leaves and leaves affected by powdery mildew, a fungal ailment that afflicts numerous plant species. Given that cherry cultivation is a flagship venture for the company, they are keen on ensuring the market receives products of uncompromised quality.

Business Requirements:
.

* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypotheses

**Hypothesis: Cherry leaves with and without powdery mildew.**

* The presence of visual differences can be investigated through visual inspection of sample image montages and average and variability image studies.
* The hypothesis will be validated if the neural network model is able to make predictions of leaf health to a level of 97% accuracy.

**Hypothesis: Images of leaves with powdery mildew will have greater color variability.**

* Since healthy leaves tend to have a fairly uniform green color, while leaves with powdery mildew additionally present with white coloration, it is hypothesized that analysis of the variability of pixels in the images will reveal that the latter has higher variability, both between different images of the same class and within individual images.
* This can be validated through variability image studies between and within images, comparing the two classes.


## Data Visualizations and ML tasks

Business requirement 1: **Data Visualization**

* Display image montages for healthy and powdery mildew cherry leaves
* Display images showing the average and standard deviation of each image class
* Display an image showing the difference between the two average images
* Display plots showing variability within the images of each class

Business requirement 2: **Classifiication**

* Give the client the ability to upload a leaf image and generate a prediction of whether it has powdery mildew or not
* Provide a report of the images and predictions that can be downloaded

## ML Business Case

### Powdery mildew classification

* The client is interested in an ML model that can predict if a cherry leaf is healthy or contains powdery mildew
* The client has request a dashboard where cherry leaf images can be uploaded and that will display the classification prediction and the associated probability
* The success metric agreed upon as the criterium for project success is 97% accuracy overall

## Applikation Design (Streamlit)

### Introduction

![Introduction page](/Readmeimg/introduction.jpg)



### Leaf Health Predictor

This page relates to business requirement 2 - *The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.*

* Link to download a set of sample images for prediction testing

![Leaf health prediction page](/Readmeimg/healthy.jpg)

### ML Performance Metrics

* Label distributions for train, validation and test sets
* Model training history comparing train and validation sets
* Model evaluation result
   
![ML performance metrics page](/Readmeimg/MLpreform.jpg)

### Project Hypotheses

![Project hypotheses page](/Readmeimg/hypo.jpg)

### Images Study

This page relates to business requirement 1 - *The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.*

* Outline of image studies

![Images study page](/Readmeimg/study.jpg)

Checkboxes for each study -
* Image montage

* Average and variability images

* Difference between average healthy and powdery mildew-containing images

* Variability within images

### Project Summary

* General project information
* Business case and requirements
* Project dataset information

![Project summary page](/Readmeimg/summary.jpg)

## Project Limitations

### Non-cherry-leaf images

The model was trained using only images of healthy and powdery mildew-containing cherry leaves. Therefore, passing any other type of image will lead the model to output a "prediction" of one of these classes, even though this would have no relevance for the image.

### Image dataset quality

It was noted during the images study that there may be some qualitative differences between the images of each class in the provided dataset. The differences observed include:

* Powdery mildew leaves seem to point upward more often, while healthy leaves point up or down
* Potential differences in background or image quality.


## Testing

User testing was carried out on the deployed dashboard.

### Dashboard user testing 

#### Page 1: Introduction

| Expectation                       | Met |
| --------------------------------- | --- |
| Page displays expected content | yes | 


#### Page 2: Images Study

| Expectation                       | Met |
| --------------------------------- | --- |
| Page displays expected content | yes |
| Mage montage can be generated for each label | yes |
| All plots and tables outlined in Dashboard Design section load and display | yes |

#### Page 3: Leaf Health Predictor

| Expectation                       | Met |
| --------------------------------- | --- |
| Page displays expected content | yes |
| Sample images link opens Kaggle cherry leaves dataset | yes |
| One or multiple files can be uploaded | yes |
| Only .jpg files can be uploaded | yes |
| After uploading, the images are displayed along with their class predictions | yes |
| A table summarizing the data is displayed | yes |

#### Page 4: ML Performance Metrics

| Expectation                       | Met |
| --------------------------------- | --- |
| Page displays expected content | yes |
| All plots and tables outlined in Dashboard Design section load and display | yes |

#### Page 5: Project Hypothesis and Validation

| Expectation                       | Met |
| --------------------------------- | --- |
| Page displays expected content | yes |

#### Page 6: Project Summary

| Expectation                       | Met |
| --------------------------------- | --- |
| Page displays expected content| yes |
| Dataset link opens Kaggle cherry leaves dataset | yes |

## Unfixed Bugs

No unfixed bugs were found during testing.

## Deployment

### Heroku

* The app live link is here: [Cherry Leaf Health Dashboard](https://cherry-leaf-health-2ff1edcf83ab.herokuapp.com/)
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


## Technologies Used

* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [TensorFlow](https://www.tensorflow.org/)
----
* [Python](https://www.python.org/)
* [Jupyter Notebooks](https://jupyter.org/)
* [Streamlit](https://docs.streamlit.io/)

## Credits

### Content

The fictional business case story was created by Code Institute.

The dataset used in the project comes from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).

### Media

The sample images on the applikation were pulled from the Kaggle database.

### Acknowledgements

The site was completed as a Portfolio 4 Project piece for the Full Stack Software Developer program at the Code Institute. This time I didn't get a mentor for this project. The one I was given in the beginning I had some trouble with in PP1, and CI never got back to me with a new mentor in time. For this project, I've taken some help from ChatGPT and the walkthrough Malaria project.

Michael Sjö 2023.
