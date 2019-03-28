#!/usr/bin/env python

import boto3
import logging
import argparse

# Hardcoding variables for testing. Will get them as command line parameters
aws_profile = ""
aws_region = "eu-west-1"
source_cw_log_group = "test_group"
destination_cw_log_group = ""

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S', level=logging.INFO)


def get_source_metric_filter(source_cw_log_group):
	paginator = cw_client.get_paginator('describe_metric_filters')
	pages = paginator.paginate(logGroupName=source_cw_log_group)

	# Merge paginated results in one single dictionary
	source_metric_filters = {'metricFilters': []}
	for page in pages:
		for item in page['metricFilters']:
			source_metric_filters['metricFilters'].append(item)

	return source_metric_filters


def put_destination_metric_filter():
	print('dummy')

def read_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--profile", action="store", required=True, dest="aws_profile", help="Select the AWS profile to be used")
	parser.add_argument("-r", "--region", action="store", required=True, dest="aws_region", help="Select the AWS region to be used")
	args = parser.parse_args()

	return args.aws_profile, args.aws_region


def main():
	#aws_profile, aws_region = read_arguments()

	global cw_client
	session = boto3.Session(profile_name=aws_profile, region_name=aws_region)
	cw_client = session.client('logs')

	source_metric_filters = get_source_metric_filter(source_cw_log_group)
	print(source_metric_filters['metricFilters'][1])


if __name__ == '__main__':
	main()