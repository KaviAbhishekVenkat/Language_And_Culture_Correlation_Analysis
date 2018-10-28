## Getting Started

Python3 is used. 

### Prerequisites

Install the client library

```
Google Cloud Translate
```

### Installing


Set up python3 environment

```
python3 -m venv env
```

Install Google library

```
pip install --upgrade google-cloud-translate
```

Export Google credentials to global environment

```
export GOOGLE_APPLICATION_CREDENTIALS="PathToTheFile.json"

```


## Running the tests

First clean the Subtitle file to remove the time stamps and than run the translation 

### Steps

Clean the Subtitle File

```
python clean.py <filename.srt>
```

Translate the clead file(rename the file name in the translate.py file)

```
python translate.py
```

## Built With

* [GoogleCloudPlatform](https://cloud.google.com/translate/docs/quickstart-client-libraries#client-libraries-install-python) - Google Cloud Platform Translate Library


## Authors

* **Kavi Abhishek Venkat** 


