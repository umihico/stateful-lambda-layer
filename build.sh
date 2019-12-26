#!/bin/bash
set -e
python python/lambdaenv/__init__.py
python lambda-function-python/lambda_function.py
zip -r python-layer.zip python
LayerVersionArn=$(aws lambda publish-layer-version --layer-name stateful-lambda-layer --zip-file fileb://python-layer.zip --compatible-runtimes python3.7 | python -c 'import sys, json, pprint; response=json.load(sys.stdin);print(str(response["LayerVersionArn"]));')
echo $LayerVersionArn
aws lambda update-function-configuration --function-name stateful-lambda-layer-playground --layers $LayerVersionArn > /dev/null
cd lambda-function-python
zip -r package.zip *
aws lambda update-function-code --function-name stateful-lambda-layer-playground --zip-file fileb://./package.zip > /dev/null
rm package.zip
cd ..
aws lambda invoke --function-name stateful-lambda-layer-playground response.txt
cat response.txt
aws lambda invoke --function-name stateful-lambda-layer-playground response.txt
cat response.txt
rm response.txt
