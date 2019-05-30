# Customer Behavior Analysis - Converting "Freemium" users to "Premium" users.

In this project, we analyze the behavior of customers of a mobile app. Their behavior is analyzed through their interaction with the app.

### Objective
The primary objective of the project is to convert free customers to paying subscribers.

### Possible Applications 
After all is said and done, the bottom line is whether we can use this model anywhere. So following are our possible use cases for the model we created.

1. Amazon Prime - customer analysis when they are simply browsing the website while they are logged in.
2. Spotify Premium - Learning how free customers interact with the app vs. how premium customers use the app. 

A funny story: Interestingly enough, I noticed Spotify using almost the same model that we creted here (extremely advanced version of this model) on my free Spotify account. I rarely use Spotify app, but when I do, I listen to my favouirite podcasts. Throughout the winter holidays, they kept offering me 3 months for $4.99, then $9.99. That's when I listend to some music and they must have gauged my lifetime customer value to be "X" and therefore gave me that offer. But when I started to listen to Podcasts more, Spotify must have guessed my lower future impact on their premium content, and thus started offering me $0.99 for 3 months, wich Showtime and Hulu.. ALL INCLUDED! Now that's some live Machine Learning right there!

3. Similaryly any business with a Freemium business model can use this model to make templting offers to borderline customers and to attract new paid users. The applications are limitless.

### Methodology
The methodology used here was to analyze customer interaction with the app screens. i.e. look at how many people used premium features, how many people interacted with each specific type of loan (there are several loans available to customers), etc. There are a nubmer of features and their interactions with one another, i.e. positively or negatively correlated, available to us in the dataset.

Please note that this is NOT the data from real customers. However, this data was generated using the EXACT same distributions of real data and customers. Python library "Faker" was used to generate this data.

### One-hot encoding - using a for loop in scikitlearn
Since we are not using deep learning here, we are relying on scikitlearn to work for us. Which means performing one-hot encoding yourself in a for loop. This was a bit wierd for me as I have used one-hot encoding with Keras before this project. 

There are 2 python code files. One files prepares the data and the other creates the model. This is a nice break up of code as we can use either file to easily with other source files and we can use the same data processing for similar projects.

### Dataset
The dataset I used is a 50000 instance dataset. I created a 80-20 train test split and then ran further processing on those splits.

After preprocessing the main data file, I created a new datafile with the correlated screens merged into one column and then deleting those screen columns from the database subsequently.

#### top_screens.csv
The file top_screens.csv contains a list of the most popular screens. One reason why you might see that some screen which is a top screen but is not present in our sample dataset, is that our dataset is a "sample" of 50,000 instances of a much larger dataset, possibly containing millions of rows. The most common screens we have, were sampled from that dataset. Consider these screens to be "absolute" truth, i.e. we can use the same top screens to perform analytics on the whole dataset with possibly similar results.

### Check out the codebase

Please check out the code to see further explanation of each and every step. If you find anything you don't understand simply by looking at the code, please let me know. I will try my best to help you out. Also if you find an error, please open up an issue. That will be much easier for all of us to learn and solve.

### Conclusion
The project gave us ~77% accurate results. You sould check out the final metrics calculated by the model in order to understand the model performance. We could tune it further and have gotten an even better results. I have some machine learning projects already inside the Deep_learning Specialization from Coursera in one of the repos. There I have explained ML model tuning in detail. Although those solutions are specifically for Deep Learning, we can apply "similar" techniques, to this model as well and make it better.

Thank you for reading the whole readme file. Hope you enjoyed it!




