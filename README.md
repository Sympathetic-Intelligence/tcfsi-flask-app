# tcfsi-flask-app

The TCFSI website is a python Flask application. It is hosted on AWS using ElasticBeanstalk/Route54/CodePipeline. Changes to the master branch are configured to be deployed live autonamtically via CodePipeline.

The dev branch should be used as the main development branch. Dev should always be in sync with master. When making updates to the website create a new branch and a pull request to dev for review. When your change is approved it should be merged into dev and tested. If after merging your branch into dev everything looks as expected, a pull request should be made to the master branch. An authotirsed user should merge the pull request into master which will kick off the deployment to the live site: [http://thecenterforsympatheticintelligence.org/](http://thecenterforsympatheticintelligence.org/)

## WARNING: Changes to the master branch are automatically deployed live.

## Requirements
You need python 3 and the dependencies in the requirements file. Create a new python environemt and run `pip install -r requirements.txt`

* python 3
* app/requirements.txt

## To run the app locally:

```
cd app/
pip install -r requirements.txt
python application.py
```

Go to: `localhost:5000` in your browser

We are now an organization
