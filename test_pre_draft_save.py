#!/usr/bin/env python3
"""
Test Pre-Draft Save
This script tests the exact data structure that the pre-draft page sends.
"""

import requests
import json

def test_pre_draft_save():
    """Test the pre-draft save functionality with real player data."""
    
    base_url = "http://localhost:4000"
    session = requests.Session()
    
    print("🧪 Testing Pre-Draft Save")
    print("=" * 50)
    
    # Login first
    print("1. Logging in...")
    login_data = {
        "email": "egclessuras@gmail.com",
        "password": "JohnWall2"
    }
    
    response = session.post(f"{base_url}/api/auth/login", json=login_data)
    if response.status_code != 200:
        print(f"Login failed: {response.text}")
        return
    
    print("✅ Login successful")
    
    # Test 2: Try to save a real player projection
    print("\n2. Testing real player save...")
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
            print("✅ Save successful!")
        else:
            print(f"❌ Save failed: {result.get('error')}")
    else:
        print(f"❌ HTTP error: {response.status_code}")
    
    # Test 3: Try to save another player
    print("\n3. Testing another player...")
    save_data2 = {
        "player_name": "Bijan Robinson",
        "position": "RB",
        "custom_stats": {
            "position": "RB",
            "rushing_yards": 1200,
            "rushing_tds": 12,
            "receptions": 45,
            "receiving_yards": 350,
            "receiving_tds": 2,
            "fumbles": 1
        }
    }
    
    response = session.post(f"{base_url}/api/save_custom_projection", json=save_data2)
    print(f"Response status: {response.status_code}")
    print(f"Response body: {response.text}")
    
    print("\n🎯 Test Complete!")

if __name__ == "__main__":
    test_pre_draft_save() 