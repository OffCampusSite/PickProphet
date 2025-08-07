#!/usr/bin/env python3
"""
Test Frontend Data Structure
This script tests different data structures that the frontend might be sending.
"""

import requests
import json

def test_frontend_data_structures():
    """Test different data structures that the frontend might be sending."""
    
    base_url = "http://localhost:4000"
    session = requests.Session()
    
    print("🧪 Testing Frontend Data Structures")
    print("=" * 50)
    
    # Login first
    login_data = {
        "email": "egclessuras@gmail.com",
        "password": "JohnWall2"
    }
    
    response = session.post(f"{base_url}/api/auth/login", json=login_data)
    if response.status_code != 200:
        print(f"❌ Login failed: {response.text}")
        return
    
    print("✅ Login successful")
    
    # Test different data structures that might be sent
    test_cases = [
        {
            "name": "Missing position field",
            "data": {
                "player_name": "Lamar Jackson",
                "custom_stats": {
                    "passing_yards": 4200,
                    "passing_tds": 35
                }
            }
        },
        {
            "name": "Empty position field",
            "data": {
                "player_name": "Lamar Jackson",
                "position": "",
                "custom_stats": {
                    "passing_yards": 4200,
                    "passing_tds": 35
                }
            }
        },
        {
            "name": "Null position field",
            "data": {
                "player_name": "Lamar Jackson",
                "position": None,
                "custom_stats": {
                    "passing_yards": 4200,
                    "passing_tds": 35
                }
            }
        },
        {
            "name": "Missing player_name",
            "data": {
                "position": "QB",
                "custom_stats": {
                    "passing_yards": 4200,
                    "passing_tds": 35
                }
            }
        },
        {
            "name": "Correct data structure",
            "data": {
                "player_name": "Lamar Jackson",
                "position": "QB",
                "custom_stats": {
                    "passing_yards": 4200,
                    "passing_tds": 35
                }
            }
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n📋 Test {i}: {test_case['name']}")
        print(f"Data: {json.dumps(test_case['data'], indent=2)}")
        
        response = session.post(f"{base_url}/api/save_custom_projection", json=test_case['data'])
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print("✅ SUCCESS")
            else:
                print(f"❌ FAILED: {result.get('error')}")
        else:
            print(f"❌ HTTP ERROR: {response.status_code}")
    
    print("\n🎉 All Tests Complete!")
    print("=" * 50)

if __name__ == "__main__":
    test_frontend_data_structures() 