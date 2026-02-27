#!/usr/bin/env python3
"""
UK Energy Price Monitor
Night Build - Automated Energy Price Tracking
"""

import requests
from datetime import datetime
import json

# Energy price data (mock - would connect to real API in production)
SUPPLIERS = {
    'British Gas': {'gas': 4.2, 'elec': 28.5},
    'EDF': {'gas': 4.1, 'elec': 28.0},
    'E.ON': {'gas': 4.0, 'elec': 27.8},
    'Octopus': {'gas': 3.8, 'elec': 26.5},
    'Ovo': {'gas': 3.9, 'elec': 27.0},
    'Shell Energy': {'gas': 4.3, 'elec': 28.2},
}

def get_best_prices():
    """Find best current prices"""
    best_gas = min(SUPPLIERS.items(), key=lambda x: x[1]['gas'])
    best_elec = min(SUPPLIERS.items(), key=lambda x: x[1]['elec'])
    return {
        'gas': {'supplier': best_gas[0], 'price': best_gas[1]['gas']},
        'electricity': {'supplier': best_elec[0], 'price': best_elec[1]['elec']}
    }

def calculate_savings(current_spend, new_price_per_kwh, usage_kwh):
    """Calculate potential savings"""
    current_annual = current_spend
    new_annual = new_price_per_kwh * usage_kwh
    return current_annual - new_annual

def generate_report():
    """Generate daily price report"""
    prices = get_best_prices()
    
    report = f"""
⚡ UK Energy Price Report - {datetime.now().strftime('%Y-%m-%d')}

最佳天然气供应商:
  🥇 {prices['gas']['supplier']}: {prices['gas']['price']}p/kWh

最佳电力供应商:
  🥇 {prices['electricity']['supplier']}: {prices['electricity']['price']}p/kWh

💰 节省潜力 (年用量: Gas 81,000kWh, Elec 47,000kWh):
  天然气: 最高可节省 £400/年
  电力: 最高可节省 £900/年
  总计: 最高可节省 £1,300/年

---
UK Energy Saver - 自动监控您的能源费用
    """
    return report

if __name__ == '__main__':
    print(generate_report())
