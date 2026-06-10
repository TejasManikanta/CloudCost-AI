# Pricing Engine Module
from backend.apis.aws_pricing import AWSPricingClient
from backend.apis.azure_pricing import AzurePricingClient
from backend.apis.gcp_pricing import GCPPricingClient
import json

class PricingEngine:
    def __init__(self):
        self.aws = AWSPricingClient()
        self.azure = AzurePricingClient()
        self.gcp = GCPPricingClient()

    def compare_compute_pricing(self, cpu, memory, region, monthly_usage_hours=730):
        """
        Compare compute pricing across cloud providers
        
        Args:
            cpu: Number of vCPU
            memory: Memory in GB
            region: Cloud region
            monthly_usage_hours: Hours per month (default: 730 = 24*365/12)
        
        Returns:
            Dictionary with pricing comparison
        """
        results = {
            'aws': self._calculate_aws_compute(cpu, memory, region, monthly_usage_hours),
            'azure': self._calculate_azure_compute(cpu, memory, region, monthly_usage_hours),
            'gcp': self._calculate_gcp_compute(cpu, memory, region, monthly_usage_hours),
        }
        
        results['cheapest'] = min(results.items(), key=lambda x: x[1]['monthly_cost'])[0]
        results['estimated_yearly_cost'] = {provider: cost['monthly_cost'] * 12 for provider, cost in results.items()}
        results['estimated_3yr_cost'] = {provider: cost['monthly_cost'] * 36 for provider, cost in results.items()}
        
        return results

    def _calculate_aws_compute(self, cpu, memory, region, hours):
        """Calculate AWS EC2 pricing"""
        # Simplified calculation - in production, fetch from actual API
        instance_type = self._get_aws_instance_type(cpu, memory)
        pricing_data = self.aws.get_ec2_pricing(instance_type, region)
        
        hourly_cost = self.aws.parse_pricing_data(pricing_data) or 0.1
        monthly_cost = hourly_cost * hours
        
        return {
            'provider': 'AWS',
            'instance_type': instance_type,
            'hourly_cost': hourly_cost,
            'monthly_cost': monthly_cost,
            'region': region
        }

    def _calculate_azure_compute(self, cpu, memory, region, hours):
        """Calculate Azure VM pricing"""
        vm_size = self._get_azure_vm_size(cpu, memory)
        pricing_data = self.azure.get_vm_pricing(vm_size, region)
        
        hourly_cost = 0.15 if pricing_data else 0.15  # Default pricing
        monthly_cost = hourly_cost * hours
        
        return {
            'provider': 'Azure',
            'vm_size': vm_size,
            'hourly_cost': hourly_cost,
            'monthly_cost': monthly_cost,
            'region': region
        }

    def _calculate_gcp_compute(self, cpu, memory, region, hours):
        """Calculate GCP Compute Engine pricing"""
        machine_type = self._get_gcp_machine_type(cpu, memory)
        pricing_data = self.gcp.get_compute_pricing(machine_type, region)
        
        hourly_cost = 0.12 if pricing_data else 0.12  # Default pricing
        monthly_cost = hourly_cost * hours
        
        return {
            'provider': 'GCP',
            'machine_type': machine_type,
            'hourly_cost': hourly_cost,
            'monthly_cost': monthly_cost,
            'region': region
        }

    def _get_aws_instance_type(self, cpu, memory):
        """Map CPU/Memory to AWS instance type"""
        if cpu <= 2 and memory <= 4:
            return 't3.medium'
        elif cpu <= 4 and memory <= 8:
            return 't3.large'
        else:
            return 'm5.xlarge'

    def _get_azure_vm_size(self, cpu, memory):
        """Map CPU/Memory to Azure VM size"""
        if cpu <= 2 and memory <= 4:
            return 'Standard_B2s'
        elif cpu <= 4 and memory <= 8:
            return 'Standard_D2s_v3'
        else:
            return 'Standard_D4s_v3'

    def _get_gcp_machine_type(self, cpu, memory):
        """Map CPU/Memory to GCP machine type"""
        if cpu <= 2 and memory <= 4:
            return 'n1-standard-2'
        elif cpu <= 4 and memory <= 8:
            return 'n1-standard-4'
        else:
            return 'n1-standard-8'
