# Cloud Pricing API Integration - Azure
import requests
import json

class AzurePricingClient:
    def __init__(self, subscription_id=None):
        self.base_url = 'https://prices.azure.com/api/v1'
        self.subscription_id = subscription_id

    def get_vm_pricing(self, vm_size='Standard_B2s', region='eastus'):
        """Get Azure Virtual Machine pricing"""
        try:
            params = {
                'api-version': '2021-10-01',
                '$filter': f"armSkuName eq '{vm_size}' and armRegionName eq '{region}'" 
            }
            response = requests.get(
                f"{self.base_url}/retail/prices",
                params=params
            )
            return response.json().get('Items', [])
        except Exception as e:
            print(f"Error fetching Azure VM pricing: {e}")
            return []

    def get_database_pricing(self, db_type='SQL Database', region='eastus'):
        """Get Azure Database pricing"""
        try:
            params = {
                'api-version': '2021-10-01',
                '$filter': f"productName eq '{db_type}' and armRegionName eq '{region}'"
            }
            response = requests.get(
                f"{self.base_url}/retail/prices",
                params=params
            )
            return response.json().get('Items', [])
        except Exception as e:
            print(f"Error fetching Azure Database pricing: {e}")
            return []

    def get_storage_pricing(self, storage_type='General Purpose', region='eastus'):
        """Get Azure Storage pricing"""
        try:
            params = {
                'api-version': '2021-10-01',
                '$filter': f"productName eq 'Storage' and armRegionName eq '{region}'"
            }
            response = requests.get(
                f"{self.base_url}/retail/prices",
                params=params
            )
            return response.json().get('Items', [])
        except Exception as e:
            print(f"Error fetching Azure Storage pricing: {e}")
            return []

    def get_kubernetes_pricing(self, region='eastus'):
        """Get Azure Kubernetes Service (AKS) pricing"""
        try:
            params = {
                'api-version': '2021-10-01',
                '$filter': f"productName eq 'Azure Kubernetes Service (AKS)' and armRegionName eq '{region}'"
            }
            response = requests.get(
                f"{self.base_url}/retail/prices",
                params=params
            )
            return response.json().get('Items', [])
        except Exception as e:
            print(f"Error fetching AKS pricing: {e}")
            return []
