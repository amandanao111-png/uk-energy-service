#!/usr/bin/env python3
"""
UK Energy Price Calculator - Residential
Calculate potential savings based on energy usage
"""

# Average UK energy prices (estimate)
AVERAGE_UNIT_RATES = {
    "electricity": {
        "direct_debit": 0.28,  # £/kWh
        "prepayment": 0.33,
        "credit": 0.35
    },
    "gas": {
        "direct_debit": 0.07,  # £/kWh
        "prepayment": 0.09,
        "credit": 0.10
    }
}

AVERAGE_STANDING_CHARGES = {
    "electricity": {
        "direct_debit": 0.53,  # £/day
        "prepayment": 0.46,
        "credit": 0.54
    },
    "gas": {
        "direct_debit": 0.31,
        "prepayment": 0.29,
        "credit": 0.40
    }
}


def calculate_annual_cost(electricity_kwh: float, gas_kwh: float, 
                         payment_method: str = "direct_debit") -> dict:
    """Calculate annual energy costs"""
    
    elec_rate = AVERAGE_UNIT_RATES["electricity"].get(payment_method, 0.28)
    gas_rate = AVERAGE_UNIT_RATES["gas"].get(payment_method, 0.07)
    
    elec_standing = AVERAGE_STANDING_CHARGES["electricity"].get(payment_method, 0.53)
    gas_standing = AVERAGE_STANDING_CHARGES["gas"].get(payment_method, 0.31)
    
    # Calculate costs
    elec_units = electricity_kwh * elec_rate
    elec_standing_total = elec_standing * 365
    
    gas_units = gas_kwh * gas_rate
    gas_standing_total = gas_standing * 365
    
    electricity_total = elec_units + elec_standing_total
    gas_total = gas_units + gas_standing_total
    
    return {
        "electricity": {
            "units": electricity_kwh,
            "unit_rate": elec_rate,
            "standing_charge": elec_standing,
            "units_cost": elec_units,
            "standing_total": elec_standing_total,
            "total": electricity_total
        },
        "gas": {
            "units": gas_kwh,
            "unit_rate": gas_rate,
            "standing_charge": gas_standing,
            "units_cost": gas_units,
            "standing_total": gas_standing_total,
            "total": gas_total
        },
        "grand_total": electricity_total + gas_total,
        "payment_method": payment_method
    }


def estimate_savings(electricity_kwh: float, gas_kwh: float,
                    current_supplier: str = "Big 6") -> dict:
    """Estimate potential savings by switching"""
    
    # Current costs (assume expensive)
    current = calculate_annual_cost(electricity_kwh, gas_kwh, "direct_debit")
    
    # Cheapest available (estimate)
    # Using typical savings from switching: 15-25%
    savings_low = current["grand_total"] * 0.15
    savings_high = current["grand_total"] * 0.25
    
    return {
        "current_annual": current["grand_total"],
        "potential_savings_low": savings_low,
        "potential_savings_high": savings_high,
        "new_annual_low": current["grand_total"] - savings_high,
        "new_annual_high": current["grand_total"] - savings_low,
        "savings_percentage": "15-25%"
    }


def print_report(electricity_kwh: float, gas_kwh: float, 
                payment_method: str = "direct_debit"):
    """Print energy cost report"""
    
    print("\n" + "="*60)
    print("🏠 UK RESIDENTIAL ENERGY CALCULATOR")
    print("="*60)
    
    # Usage summary
    print(f"\n📊 ANNUAL USAGE")
    print(f"  Electricity: {electricity_kwh:,} kWh")
    print(f"  Gas: {gas_kwh:,} kWh")
    print(f"  Payment: {payment_method.replace('_', ' ').title()}")
    
    # Calculate costs
    costs = calculate_annual_cost(electricity_kwh, gas_kwh, payment_method)
    
    print(f"\n💷 ESTIMATED ANNUAL COSTS")
    print(f"  Electricity: £{costs['electricity']['total']:,.2f}")
    print(f"    - Unit cost: £{costs['electricity']['units_cost']:,.2f}")
    print(f"    - Standing charge: £{costs['electricity']['standing_total']:,.2f}")
    print(f"  Gas: £{costs['gas']['total']:,.2f}")
    print(f"    - Unit cost: £{costs['gas']['units_cost']:,.2f}")
    print(f"    - Standing charge: £{costs['gas']['standing_total']:,.2f}")
    print(f"  ─────────────────────")
    print(f"  TOTAL: £{costs['grand_total']:,.2f}")
    
    # Savings estimate
    savings = estimate_savings(electricity_kwh, gas_kwh)
    
    print(f"\n💰 POTENTIAL SAVINGS (by switching)")
    print(f"  Current: £{savings['current_annual']:,.2f}/year")
    print(f"  Could save: £{savings['potential_savings_low']:,.0f} - £{savings['potential_savings_high']:,.0f}")
    print(f"  New annual: £{savings['new_annual_high']:,.0f} - £{savings['new_annual_low']:,.0f}")
    print(f"  Savings: {savings['savings_percentage']}")
    
    print("\n" + "="*60)
    print("📝 Note: Actual savings depend on supplier & tariff")
    print("="*60 + "\n")


# Test with example data
if __name__ == "__main__":
    # Example: User's usage (from earlier conversation)
    USER_ELEC = 46677  # kWh
    USER_GAS = 81758   # kWh
    
    print_report(USER_ELEC, USER_GAS)
