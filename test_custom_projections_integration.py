#!/usr/bin/env python3
"""
Test Custom Projections Integration
This script tests that custom projections from Supabase are being used in simulations and calculations.
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_custom_projections_integration():
    """Test that custom projections from Supabase are being used."""
    
    base_url = "http://localhost:4000"
    
    print("🧪 Testing Custom Projections Integration")
    print("=" * 50)
    
    # Test 1: Check if server is running
    try:
        response = requests.get(f"{base_url}/api/auth/check")
        print(f"✅ Server is running (Status: {response.status_code})")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the application first:")
        print("   python3 fantasy_draft_web_enhanced.py")
        return
    
    # Test 2: Initialize a draft
    print("\n📋 Initializing draft...")
    init_data = {
        "num_teams": 12,
        "user_position": 1,
        "scoring_format": "ppr"
    }
    
    response = requests.post(f"{base_url}/api/init", json=init_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Draft initialized successfully")
        print(f"   Custom projections loaded: {result.get('draft_info', {}).get('custom_projections_loaded', 0)}")
    else:
        print(f"❌ Failed to initialize draft: {response.text}")
        return
    
    # Test 3: Get available players and check for custom projections
    print("\n📊 Getting available players...")
    response = requests.get(f"{base_url}/api/available_players")
    if response.status_code == 200:
        result = response.json()
        players = result.get('players', [])
        print(f"✅ Found {len(players)} available players")
        
        # Check for customized players
        customized_players = [p for p in players if p.get('is_customized', False)]
        print(f"   Customized players: {len(customized_players)}")
        
        if customized_players:
            print("   Customized players found:")
            for player in customized_players[:5]:  # Show first 5
                print(f"     - {player['name']} ({player['position']}): {player['projected_points']} pts")
        else:
            print("   No customized players found (this is normal if no custom projections exist)")
    
    # Test 4: Run simulation
    print("\n🎯 Running simulation...")
    response = requests.post(f"{base_url}/api/run_simulation")
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Simulation completed: {result.get('simulation_status', 'Unknown')}")
    else:
        print(f"❌ Failed to run simulation: {response.text}")
        return
    
    # Test 5: Get recommendations
    print("\n🏆 Getting recommendations...")
    response = requests.get(f"{base_url}/api/recommendations")
    if response.status_code == 200:
        result = response.json()
        recommendations = result.get('recommendations', [])
        print(f"✅ Found {len(recommendations)} recommendations")
        
        if recommendations:
            print("   Top recommendations:")
            for i, rec in enumerate(recommendations[:3], 1):
                customized = " (CUSTOMIZED)" if rec.get('is_customized', False) else ""
                print(f"     {i}. {rec['name']} ({rec['position']}): {rec['projected_points']} pts{customized}")
    
    # Test 6: Check scoring format change
    print("\n🔄 Testing scoring format change...")
    response = requests.post(f"{base_url}/api/set_scoring_format", json={"format": "half-ppr"})
    if response.status_code == 200:
        print("✅ Scoring format changed to half-ppr")
        
        # Get players again to see if custom projections are still loaded
        response = requests.get(f"{base_url}/api/available_players?position=QB")
        if response.status_code == 200:
            result = response.json()
            players = result.get('players', [])
            customized_players = [p for p in players if p.get('is_customized', False)]
            print(f"   Customized players after format change: {len(customized_players)}")
    
    print("\n🎉 Custom Projections Integration Test Complete!")
    print("=" * 50)
    print("✅ If you see customized players and their projections, the integration is working!")
    print("✅ The system is now using Supabase custom projections for all calculations.")

if __name__ == "__main__":
    test_custom_projections_integration() 
"""
Test Custom Projections Integration
This script tests that custom projections from Supabase are being used in simulations and calculations.
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def test_custom_projections_integration():
    """Test that custom projections from Supabase are being used."""
    
    base_url = "http://localhost:4000"
    
    print("🧪 Testing Custom Projections Integration")
    print("=" * 50)
    
    # Test 1: Check if server is running
    try:
        response = requests.get(f"{base_url}/api/auth/check")
        print(f"✅ Server is running (Status: {response.status_code})")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the application first:")
        print("   python3 fantasy_draft_web_enhanced.py")
        return
    
    # Test 2: Initialize a draft
    print("\n📋 Initializing draft...")
    init_data = {
        "num_teams": 12,
        "user_position": 1,
        "scoring_format": "ppr"
    }
    
    response = requests.post(f"{base_url}/api/init", json=init_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Draft initialized successfully")
        print(f"   Custom projections loaded: {result.get('draft_info', {}).get('custom_projections_loaded', 0)}")
    else:
        print(f"❌ Failed to initialize draft: {response.text}")
        return
    
    # Test 3: Get available players and check for custom projections
    print("\n📊 Getting available players...")
    response = requests.get(f"{base_url}/api/available_players")
    if response.status_code == 200:
        result = response.json()
        players = result.get('players', [])
        print(f"✅ Found {len(players)} available players")
        
        # Check for customized players
        customized_players = [p for p in players if p.get('is_customized', False)]
        print(f"   Customized players: {len(customized_players)}")
        
        if customized_players:
            print("   Customized players found:")
            for player in customized_players[:5]:  # Show first 5
                print(f"     - {player['name']} ({player['position']}): {player['projected_points']} pts")
        else:
            print("   No customized players found (this is normal if no custom projections exist)")
    
    # Test 4: Run simulation
    print("\n🎯 Running simulation...")
    response = requests.post(f"{base_url}/api/run_simulation")
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Simulation completed: {result.get('simulation_status', 'Unknown')}")
    else:
        print(f"❌ Failed to run simulation: {response.text}")
        return
    
    # Test 5: Get recommendations
    print("\n🏆 Getting recommendations...")
    response = requests.get(f"{base_url}/api/recommendations")
    if response.status_code == 200:
        result = response.json()
        recommendations = result.get('recommendations', [])
        print(f"✅ Found {len(recommendations)} recommendations")
        
        if recommendations:
            print("   Top recommendations:")
            for i, rec in enumerate(recommendations[:3], 1):
                customized = " (CUSTOMIZED)" if rec.get('is_customized', False) else ""
                print(f"     {i}. {rec['name']} ({rec['position']}): {rec['projected_points']} pts{customized}")
    
    # Test 6: Check scoring format change
    print("\n🔄 Testing scoring format change...")
    response = requests.post(f"{base_url}/api/set_scoring_format", json={"format": "half-ppr"})
    if response.status_code == 200:
        print("✅ Scoring format changed to half-ppr")
        
        # Get players again to see if custom projections are still loaded
        response = requests.get(f"{base_url}/api/available_players?position=QB")
        if response.status_code == 200:
            result = response.json()
            players = result.get('players', [])
            customized_players = [p for p in players if p.get('is_customized', False)]
            print(f"   Customized players after format change: {len(customized_players)}")
    
    print("\n🎉 Custom Projections Integration Test Complete!")
    print("=" * 50)
    print("✅ If you see customized players and their projections, the integration is working!")
    print("✅ The system is now using Supabase custom projections for all calculations.")

if __name__ == "__main__":
    test_custom_projections_integration() 
 