# Deploy your API on AWS using Chalice

This is a sample project that shows how to deploy a simple API on AWS using [Chalice]

# Prerequisites
1. Install [Python 3.9.13]
2. make pyenv virtualenv 3.9.13 aws_deployment
2. Commands to Create pyenv virtualenv
    1. pyenv virtualenv 3.9.13 aws_deployment
    2. pyenv activate aws_deployment
3. Install requirements.txt
    1. pip install -r requirements.txt


# Code Structure
1. app.py - This is the main file that contains the code for the API
2. requirements.txt - This file contains the list of dependencies that are required for the project
3. .chalice/config.json - This file contains the configuration for the project
4. .chalice/policy-dev.json - This file contains the IAM policy for the project

# Code

## app.py
This file contains the code for the API. It contains two routes:
1. / - This route returns the value of the environment variable MY_VAR. If the environment variable is not set, it returns "dev"
2. /predict - This route returns the request body that is sent to the API

```python
from chalice import Chalice
import os

app = Chalice(app_name="predictor")

@app.route("/", methods=["GET"])
def index():
    return os.environ.get("MY_VAR", "dev")

@app.route("/predict", methods=["POST"])
def predict():
    prediction = app.current_request.json_body
    return prediction
```

## Config.json
This file contains the configuration for the project. It contains the following:
1. version - This is the version of the config file.
2. app_name - This is the name of the project
3. autogen_policy - This is a boolean value that determines whether the IAM policy should be autogenerated or not
4. automatic_layer - This is a boolean value that determines whether the AWS Lambda layer should be autogenerated or not
5. environment_variables - This is a dictionary that contains the environment variables that should be set for the project
6. stages - This is a dictionary that contains the configuration for the different stages. In this case, we have only one stage called dev. The api_gateway_stage is the name of the API Gateway stage that is created for the project.

```json
{
    "version": "2.0",
    "app_name": "Test",
    "autogen_policy": true,
    "automatic_layer": true,
    "environment_variables": {
        "MY_VAR": "Welcome to the serverless world!"
    },
    "stages": {
      "dev": {
        "api_gateway_stage": "api"
      }
    }
  }
```

## policy-dev.json
This file contains the IAM policy for the project. It contains the following:
1. Version - This is the version of the policy
2. Statement - This is a list of statements that are used to define the policy. In this case, we have only one statement that allows the API Gateway to invoke the Lambda function.
    1. Sid - This is the statement ID
    2. Effect - This is the effect of the statement. It can be Allow or Deny
    3. Action - This is the action that is allowed or denied
    4. Resource - This is the resource that is allowed or denied



```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1471020565000",
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy",
                "iam:CreateRole",
                "iam:PutRolePolicy",
                "iam:GetRole",
                "iam:PassRole"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "Stmt1471020565001",
            "Effect": "Allow",
            "Action": [
                "apigateway:GET",
                "apigateway:HEAD",
                "apigateway:POST"
            ],
            "Resource": [
                "arn:aws:apigateway:ap-south-1::/restapis",
                "arn:aws:apigateway:ap-south-1::/restapis/*/resources",
                "arn:aws:apigateway:ap-south-1::/restapis/*/resources/*"
            ]
        },
        {
            "Sid": "Stmt1471020565002",
            "Effect": "Allow",
            "Action": [
                "apigateway:DELETE"
            ],
            "Resource": [
                "arn:aws:apigateway:ap-south-1::/restapis/*/resources/*"
            ]
        },
        {
            "Sid": "Stmt1471020565003",
            "Effect": "Allow",
            "Action": [
                "apigateway:POST"
            ],
            "Resource": [
                "arn:aws:apigateway:ap-south-1::/restapis/*/deployments",
                "arn:aws:apigateway:ap-south-1::/restapis/*/resources/*"
            ]
        },
        {
            "Sid": "Stmt1471020565004",
            "Effect": "Allow",
            "Action": [
                "apigateway:PUT"
            ],
            "Resource": [
                "arn:aws:apigateway:ap-south-1::/restapis/*/methods/GET",
                "arn:aws:apigateway:ap-south-1::/restapis/*/methods/GET/*",
                "arn:aws:apigateway:ap-south-1::/restapis/*/methods/POST",
                "arn:aws:apigateway:ap-south-1::/restapis/*/methods/POST/*",
                "arn:aws:apigateway:ap-south-1::/restapis/*/methods/PUT",
                "arn:aws:apigateway:ap-south-1::/restapis/*/methods/PUT/*"
            ]
        },
        {
            "Sid": "Stmt1471020565005",
            "Effect": "Allow",
            "Action": [
                "apigateway:PATCH"
            ],
            "Resource": [
                "arn:aws:apigateway:ap-south-1::/restapis/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "lambda:*",
            "Resource": "*"
        }
    ]
    }
```
# Run on local
1. chalice local --stage dev

# Deployment
1. chalice deploy --stage dev

# Testing
1. curl -X POST -H "Content-Type: application/json" -d '{"name": "John"}' https://<API Gateway URL>/predict

# Delete   
if you are done with the project, you can delete the project using the following command:
1. chalice delete --stage dev

# Conclusion
In this article, we have seen how to create a serverless API using Chalice. We have also seen how to deploy the API to AWS Lambda and API Gateway. We have also seen how to test the API. In the next article, we will see how to create a serverless API using AWS SAM.


# Author

- Sohaib Anwaar : https://www.sohaibanwaar.com
- gmail : sohaibanwaar36@gmail.com
- linkedin : [Have Some Professional Talk here](https://www.linkedin.com/in/sohaib-anwaar-4b7ba1187/)
- Stack Overflow : [Get my help Here](https://stackoverflow.com/users/7959545/sohaib-anwaar)
- Kaggle : [View my master-pieces here](https://www.kaggle.com/sohaibanwaar1203)
- Github : [View my code here](https://github.com/SohaibAnwaar)