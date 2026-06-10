# Cloud Pricing API Integration - AWS
import boto3
import json
from datetime import datetime

class AWSPricingClient:
    def __init__(self, access_key_id=None, secret_access_key=None, region='us-east-1'):
        self.client = boto3.client(
            'pricing',
            region_name=region,
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key
        )
        self.ec2_client = boto3.client('ec2', region_name=region)

    def get_ec2_pricing(self, instance_type='t3.medium', region='us-east-1'):
        """Get EC2 instance pricing"""
        try:
            response = self.client.get_products(
                ServiceCode='AmazonEC2',
                Filters=[
                    {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': region},
                    {'Type': 'TERM_MATCH', 'Field': 'instanceType', 'Value': instance_type},
                ]
            )
            return response.get('PriceList', [])
        except Exception as e:
            print(f"Error fetching EC2 pricing: {e}")
            return []

    def get_rds_pricing(self, db_engine='MySQL', instance_class='db.t3.micro'):
        """Get RDS pricing"""
        try:
            response = self.client.get_products(
                ServiceCode='AmazonRDS',
                Filters=[
                    {'Type': 'TERM_MATCH', 'Field': 'engine', 'Value': db_engine},
                    {'Type': 'TERM_MATCH', 'Field': 'databaseEngine', 'Value': db_engine},
                ]
            )
            return response.get('PriceList', [])
        except Exception as e:
            print(f"Error fetching RDS pricing: {e}")
            return []

    def get_s3_pricing(self, region='us-east-1', storage_class='STANDARD'):
        """Get S3 storage pricing"""
        try:
            response = self.client.get_products(
                ServiceCode='AmazonS3',
                Filters=[
                    {'Type': 'TERM_MATCH', 'Field': 'location', 'Value': region},
                    {'Type': 'TERM_MATCH', 'Field': 'storageClass', 'Value': storage_class},
                ]
            )
            return response.get('PriceList', [])
        except Exception as e:
            print(f"Error fetching S3 pricing: {e}")
            return []

    def parse_pricing_data(self, pricing_data):
        """Parse AWS pricing JSON data"""
        try:
            for price in pricing_data:
                data = json.loads(price)
                sku_info = data.get('product', {})
                pricing_terms = data.get('terms', {})
                
                on_demand = pricing_terms.get('OnDemand', {})
                if on_demand:
                    for term_sku, term_data in on_demand.items():
                        for price_dimension, price_info in term_data.get('priceDimensions', {}).items():
                            price_per_unit = price_info.get('pricePerUnit', {}).get('USD', 0)
                            return float(price_per_unit)
        except Exception as e:
            print(f"Error parsing pricing data: {e}")
        return 0
