from troposphere import Output, Ref, Template
from troposphere.s3 import Bucket, PublicRead


t = Template()

t.add_description(
    "AWS CloudFormation Sample Template S3_Bucket: Sample template showing "
    "how to create a publicly accessible S3 bucket. "
    "**WARNING** This template creates an Amazon S3 Bucket. "
    "You will be billed for the AWS resources used if you create "
    "a stack from this template.")

s3bucket = t.add_resource(Bucket("S3Bucket", AccessControl=PublicRead,))

t.add_output(Output(
    "BucketName",
    Value=Ref(s3bucket),
    Description="Name of S3 bucket to hold website content"
))

print(t.to_yaml())

'''
aws cloudformation create-stack \
--stack-name my-s3-stack \
--template-body file://s3_cfn_template.yml \
--parameters ParameterKey=S3BucketName,ParameterValue=redshift-s3-baws
'''