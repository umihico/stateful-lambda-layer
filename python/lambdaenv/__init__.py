import boto3
import os
from pprint import pprint

class LambdaEnv():
    def __init__(self, context, aws_access_key_id=None, aws_secret_access_key=None):
        self.function_name=context.function_name
        self._create_boto3client(aws_access_key_id, aws_secret_access_key)

    def _create_boto3client(self, aws_access_key_id, aws_secret_access_key):
        if not aws_access_key_id and not aws_secret_access_key:
            self.client = boto3.client('lambda')
        else:
            self.client = boto3.client('lambda', aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)

    def get(self, key, default_value=None):
        return os.getenv(key)

    def set(self, key, value):
        response = self.client.update_function_configuration(
            FunctionName=self.function_name,
            Environment={
                'Variables': {
                    key : value,
                }
            }
        )
        os.environ[key] = value
