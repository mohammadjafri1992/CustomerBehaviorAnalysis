# Customer Behavior Analysis

In this project, we analyze the behavior of customers of a mobile app. Their behavior is analyzed through their interaction with the app.

### Objective
The primary objective of the project is to convert free customers to paying subscribers.

### Methodology
The methodology used here was to analyze customer interaction with the app screens. i.e. look at how many people used premium features,
how many people interacted with each specific type of loan (there are several loans available to customers), etc. There are a nubmer of 
features and their interactions with one another, i.e. positively or negatively correlated, available to us in the dataset.

Please note that this is NOT the data from real customers. However, this data was generated using the EXACT same distributions of real
data and customers. Python library "Faker" was used to generate this data.

### One-hot encoding - using a for loop in scikitlearn
Since we are not using deep learning here, we are relying on scikitlearn to work for us. Which means performing one-hot encoding yourself
in a for loop. This was a bit wierd for me as I have used one-hot encoding with Keras before this project. 

There are 2 python code files. One files prepares the data and the other creates the model. This is a nice break up of code as we can 
use either file to easily with other source files and we can use the same data processing for similar projects.

### Dataset
The dataset I used is a 50000 instance dataset. I created a 80-20 train test split and then ran further processing on those splits.

After preprocessing the main data file, I created a new datafile with the correlated screens merged into one column and then deleting those
screen columns from the database subsequently.

#### top_screens.csv
The file top_screens.csv contains a list of the most popular screens. One reason why you might see that some screen which is a top screen
but is not present in our sample dataset, is that our dataset is a "sample" of 50,000 instances of a much larger dataset, possibly containing
millions of rows. The most common screens we have, were sampled from that dataset. Consider these screens to be "absolute" truth, i.e. 
we can use the same top screens to perform analytics on the whole dataset with possibly similar results.

