#!/usr/bin/env python

'''
/*
* Name: instance.py
* Author: Alexandru Todicescu
* Description: Helper script to stop/start EC2 instances based on Environment tag
* Usage:
* 
* Notes: (TODO) DescribeTags is paginated with max 1000 results. If number of instance ids returned > 1000, need to do additional DescribeTags operations.
* https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTags.html
*
*/
'''

import boto3
import argparse
import json
import logging
logging.basicConfig(level=logging.INFO)

# Read in command-line parameters
parser = argparse.ArgumentParser()
parser.add_argument("-o", "--operation", action="store", required=True, dest="operation", help="EC2 oepration to be perfromed.")
parser.add_argument("-e", "--environment", action="store", required=True, dest="environment", help="Value of the Environment tag on which the operation will be performed")
parser.add_argument("-r", "--region", action="store", required=False, dest="region", default="eu-west-1", help="Region where the operation will be performed. Default: eu-west-1")

args = parser.parse_args()
operation = args.operation
environment = args.environment
region = args.region

# Retrieve instance ids with the specified environment tag
ec2 = boto3.client('ec2', region_name=region)
response = ec2.describe_tags(
    DryRun=False,
    Filters=[{'Name': 'key', 'Values': ['Environment']},
             {'Name': 'value', 'Values': [environment]},
            ], 
    MaxResults=1000, 
#    NextToken='string'
)
logging.info (response)
