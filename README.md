
# Stateful-Lambda-Layer
Complete updating and managing environment variables in AWS Lambda by itself!

If your API keys or something which expire regularly, you don't have to store the small data somewhere outside.

## Installation

1. Download [python-layer.zip](https://github.com/umihico/stateful-lambda-layer/raw/master/python-layer.zip)
1. Add python-layer.zip as one of lambda layers and attach it on your lambda function.
1. Attach policy `AWSLambdaFullAccess` or something on your lambda role to let boto3 executes `boto3.client('lambda').update_function_configuration`

## Usage

```python

from lambdaenv import LambdaEnv
def lambda_handler(event, context):
    old_val=os.getenv('example_key') # "old_data"
    lambdaenv=LambdaEnv(context)
    lambdaenv.set('example_key', "new_data")
    new_val=lambdaenv.get('example_key') # lambdaenv.get is equivalent to os.getenv
```

if you execute this lambda again or see the configuration, you see the environment variables are changed!

## Contributing

I would be happy if somebody supply the same function with other languages.
