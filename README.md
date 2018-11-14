# Language and Culture Correlation Analysis

  The language is a product of the culture associated with its speakers. This means, if a community identifies something as positive, then the language should support it by providing words that have a positive sentiment. This brings up an interesting hypothesis, if a set of distinct scenarios with varying sentiments associated for each community is analyzed for each community, given a particular test scenario and a language describing it, we can identify the community. 
  To test this hypothesis, we choose the scenarios as the movies produced in different languages. The interpretation of the scenario is given by the set of dialogues retrieved from the subtitle files. 
  Due to our limitation of performing sentiment analysis only for the English language, we perform a translation of all the other languages int english before starting our analysis. 


## Getting Started

We have written the project as jupyter notebooks using python3. To simply run the project, clone this repo and open the notebook through jupyter. make sure all the data files are downloaded properly and are in the same directory as the notebook.
### Prerequisites


Install the library

```
TextBlob
Pandas
Matplotlib
Sklearn
Numpy
```

### Installing

Set up python3 environment

```
python3 -m venv env
```

Install TextBlob

```
pip install textblob
```

Install pandas

```
pip install pandas
```

Install Matplotlib

```
pip install matplotlib
```

Install Sklearn

```
pip install scikit-learn
```

Install Numpy

```
pip install numpy
```

## Running the tests

Run all the cells sequentially to test the project for the given 21 movie data set


## Built With

* [scikit-learn](https://github.com/scikit-learn/scikit-learn) - Machine Learning Library

## Results

For the given set of movies, we find that the english language generally has a higher positive sentiments and tends have more meaningful than the chinese counterparts. This can also the effect of using the english as the common ground of evaluation rather than an actual disparity. 
Trying to evaluate correlation between the polarity and subjectivity values for each language, we find there is a high correlation between the polarity values and not so much in the subjectivity values. This provides a minor support for our hypothesis described in the introduction.

To test our hypothesis we then train a Nearest Centroid Model after creating a train and test set from the given dataset. This gives an average prediction success of 66%.

## Authors

* **Arif Awate** 
* **Kavi Abhishek Venkat** 

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


