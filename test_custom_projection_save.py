#!/usr/bin/env python3
"""
Test Custom Projection Save
This script tests what data is being sent when saving custom projections.
"""

import requests
import json

def test_custom_projection_save():
    """Test saving a custom projection with the data structure the frontend sends."""
    
    base_url = "http://localhost:4000"
    
    # Create a session to maintain cookies
    session = requests.Session()
    
    print("🧪 Testing Custom Projection Save")
    print("=" * 50)
    
    # Test 1: Check if server is running
    try:
        response = session.get(f"{base_url}/api/auth/check")
        print(f"✅ Server is running (Status: {response.status_code})")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the application first:")
        print("   python3 fantasy_draft_web_enhanced.py")
        return
    
    # Test 2: Login first
    print("\n🔐 Logging in...")
    login_data = {
        "email": "egclessuras@gmail.com",
        "password": "JohnWall2"
    }
    
    response = session.post(f"{base_url}/api/auth/login", json=login_data)
    if response.status_code != 200:
        print(f"❌ Login failed: {response.text}")
        return
    
    print("✅ Login successful")
    
    # Test 3: Check authentication status
    print("\n🔍 Checking authentication...")
    response = session.get(f"{base_url}/api/auth/check")
    print(f"Auth check response: {response.text}")
    
    # Test 4: Try to save a custom projection with the exact data structure the frontend sends
    print("\n💾 Testing custom projection save...")
    
    # Simulate the data structure that the frontend sends
    save_data = {
        "player_name": "Lamar Jackson",
        "position": "QB",
        "custom_stats": {
            "position": "QB",
            "passing_yards": 4200,
            "passing_tds": 35,
            "interceptions": 8,
            "rushing_yards": 800,
            "rushing_tds": 5,
            "fumbles": 2
        }
    }
    
    print(f"Sending data: {json.dumps(save_data, indent=2)}")
    
    response = session.post(f"{base_url}/api/save_custom_projection", json=save_data)
    print(f"Response status: {response.status_code}")
    print(f"Response body: {response.text}")
    
    if response.status_code == 200:
        result = response.json()
        if result.get('success'):
            print("✅ Custom projection saved successfully!")
            print(f"   Message: {result.get('message', 'Unknown')}")
            print(f"   Projections: {result.get('projections', {})}")
        else:
            print(f"❌ Save failed: {result.get('error', 'Unknown error')}")
    else:
        print(f"❌ Request failed with status {response.status_code}")
    
    print("\n🎉 Test Complete!")
    print("=" * 50)

if __name__ == "__main__":
    test_custom_projection_save() 