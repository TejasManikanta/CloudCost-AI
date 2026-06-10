# Cloud Pricing API Integration - GCP
import requests
import json

class GCPPricingClient:
    def __init__(self, project_id=None):
        self.base_url = 'https://cloudpricing.googleapis.com/pricing/v1'
        self.project_id = project_id

    def get_compute_pricing(self, machine_type='n1-standard-1', region='us-central1'):
        """Get GCP Compute Engine pricing"""
        try:
            # GCP uses Cloud Billing API
            response = requests.get(
                f"{self.base_url}/machines",
                params={
                    'machineType': machine_type,
                    'region': region
                }
            )
            return response.json()
        except Exception as e:
            print(f"Error fetching GCP Compute pricing: {e}")
            return {}

    def get_cloud_sql_pricing(self, db_type='mysql', instance_class='db-f1-micro', region='us-central1'):
        """Get GCP Cloud SQL pricing"""
        try:
            response = requests.get(
                f"{self.base_url}/cloudsql",
                params={
                    'databaseType': db_type,
                    'instanceClass': instance_class,
                    'region': region
                }
            )
            return response.json()
        except Exception as e:
            print(f"Error fetching GCP Cloud SQL pricing: {e}")
            return {}

    def get_storage_pricing(self, storage_class='STANDARD', region='us-central1'):
        """Get GCP Cloud Storage pricing"""
        try:
            response = requests.get(
                f"{self.base_url}/storage",
                params={
                    'storageClass': storage_class,
                    'region': region
                }
            )
            return response.json()
        except Exception as e:
            print(f"Error fetching GCP Storage pricing: {e}")
            return {}

    def get_kubernetes_pricing(self, region='us-central1'):
        """Get GCP Kubernetes Engine (GKE) pricing"""
        try:
            response = requests.get(
                f"{self.base_url}/gke",
                params={'region': region}
            )
            return response.json()
        except Exception as e:
            print(f"Error fetching GKE pricing: {e}")
            return {}
