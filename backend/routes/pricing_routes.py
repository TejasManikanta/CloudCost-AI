# Routes - Pricing
from flask import Blueprint, request, jsonify
from backend.auth.security import token_required
from backend.pricing.pricing_engine import PricingEngine
from backend.pricing.currency_converter import CurrencyConverter
from datetime import datetime

bp = Blueprint('pricing', __name__, url_prefix='/api/pricing')
pricer = PricingEngine()
converter = CurrencyConverter()

@bp.route('/compare', methods=['POST'])
@token_required
def compare_pricing():
    """Compare cloud pricing"""
    data = request.get_json()
    user_id = request.user_id
    
    cpu = data.get('cpu', 2)
    memory = data.get('memory', 4)
    region = data.get('region', 'us-east-1')
    currency = data.get('currency', 'USD')
    
    # Get pricing comparison
    pricing = pricer.compare_compute_pricing(cpu, memory, region)
    
    # Convert to requested currency
    if currency != 'USD':
        for provider in ['aws', 'azure', 'gcp']:
            pricing[provider]['monthly_cost'] = converter.convert(
                pricing[provider]['monthly_cost'],
                'USD',
                currency
            )
    
    # TODO: Save pricing request and results to database
    
    return jsonify({
        'success': True,
        'request_id': 1,
        'pricing': pricing,
        'currency': currency,
        'timestamp': datetime.now().isoformat()
    }), 200

@bp.route('/history', methods=['GET'])
@token_required
def get_pricing_history():
    """Get pricing comparison history"""
    user_id = request.user_id
    
    # TODO: Fetch pricing history from database
    
    return jsonify({'history': []}), 200

@bp.route('/forecast', methods=['POST'])
@token_required
def forecast_costs():
    """Forecast future costs"""
    data = request.get_json()
    user_id = request.user_id
    
    current_monthly_cost = data.get('monthly_cost', 1000)
    growth_rate = data.get('growth_rate', 0.1)  # 10% monthly growth
    months = data.get('months', 12)
    
    forecast = []
    for month in range(1, months + 1):
        cost = current_monthly_cost * ((1 + growth_rate) ** month)
        forecast.append({
            'month': month,
            'estimated_cost': round(cost, 2)
        })
    
    return jsonify({
        'success': True,
        'forecast': forecast,
        'total_forecast': sum([item['estimated_cost'] for item in forecast])
    }), 200
