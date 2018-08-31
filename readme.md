# aws cli command reference for cfn

## to validate template
aws cloudformation validate-template \
--template-body file://sampletemplate.json

## launch cfn template
aws cloudformation create-stack \
--stack-name redshift-vpc \
--template-body file://vpc_cloudformation_template.yml \
--region us-west-2 \
--profile baws


