import json
import traceback
import datetime


def lambda_handler(event, context):
    try:
        from lambdaenv import LambdaEnv
        lambdaenv=LambdaEnv(context)
        prev_dynamic_val=lambdaenv.get('dynamic_val')
        lambdaenv.set('dynamic_val', datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        new_dynamic_val=lambdaenv.get('dynamic_val')
        body="Environment variables {'dynamic_val':"+prev_dynamic_val+"} in "+lambdaenv.function_name+" became {'dynamic_val':"+new_dynamic_val+"}"
    except Exception as e:
        body=traceback.format_exc()
    return body
