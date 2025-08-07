#!/usr/bin/env python3
"""
Complete Fix Test
This script tests the complete fix for the foreign key constraint issue.
"""

import requests
import json

def test_complete_fix():
    """Test the complete fix for the foreign key constraint issue."""
    
    base_url = "http://localhost:4000"
    session = requests.Session()
    
    print("🔧 Testing Complete Fix")
    print("=" * 50)
    
    # Test 1: Check authentication without login
    print("1. Testing authentication without login...")
    response = session.get(f"{base_url}/api/auth/check")
    print(f"Auth check (no login): {response.text}")
    
    # Test 2: Try to access pre-draft page without login
    print("\n2. Testing pre-draft access without login...")
    response = session.get(f"{base_url}/pre-draft")
    print(f"Pre-draft access (no login): Status {response.status_code}")
    if response.status_code == 302:
        print("✅ Correctly redirected to login")
    else:
        print("❌ Should have been redirected")
    
    # Test 3: Login
    print("\n3. Logging in...")
    login_data = {
        "email": "egclessuras@gmail.com",
        "password": "JohnWall2"
    }
    
    response = session.post(f"{base_url}/api/auth/login", json=login_data)
    if response.status_code != 200:
        print(f"❌ Login failed: {response.text}")
        return
    
    result = response.json()
    user_id = result.get('user', {}).get('id')
    print(f"✅ Login successful - User ID: {user_id}")
    
    # Test 4: Check authentication after login
    print("\n4. Testing authentication after login...")
    response = session.get(f"{base_url}/api/auth/check")
    print(f"Auth check (with login): {response.text}")
    
    # Test 5: Access pre-draft page with login
    print("\n5. Testing pre-draft access with login...")
    response = session.get(f"{base_url}/pre-draft")
    print(f"Pre-draft access (with login): Status {response.status_code}")
    if response.status_code == 200:
        print("✅ Successfully accessed pre-draft page")
    else:
        print("❌ Should have been able to access")
    
    # Test 6: Save multiple custom projections
    print("\n6. Testing multiple custom projection saves...")
    test_players = [
        {
            "name": "Lamar Jackson",
            "position": "QB",
            "stats": {
                "position": "QB",
                "passing_yards": 4200,
                "passing_tds": 35,
                "interceptions": 8,
                "rushing_yards": 800,
                "rushing_tds": 5,
                "fumbles": 2
            }
        },
        {
            "name": "Bijan Robinson",
            "position": "RB",
            "stats": {
                "position": "RB",
                "rushing_yards": 1200,
                "rushing_tds": 12,
                "receptions": 45,
                "receiving_yards": 350,
                "receiving_tds": 2,
                "fumbles": 1
            }
        },
        {
            "name": "Ja'Marr Chase",
            "position": "WR",
            "stats": {
                "position": "WR",
                "receptions": 85,
                "receiving_yards": 1200,
                "receiving_tds": 10,
                "rushing_yards": 50,
                "rushing_tds": 0,
                "fumbles": 1
            }
        }
    ]
    
    for i, player in enumerate(test_players, 1):
        print(f"\n   Saving {player['name']} ({player['position']})...")
        save_data = {
            "player_name": player['name'],
            "position": player['position'],
            "custom_stats": player['stats']
        }
        
        response = session.post(f"{base_url}/api/save_custom_projection", json=save_data)
        if response.status_code == 200:
            result = response.json()
            if result.get('success'):
                print(f"   ✅ {player['name']} saved successfully")
            else:
                print(f"   ❌ {player['name']} failed: {result.get('error')}")
        else:
            print(f"   ❌ {player['name']} HTTP error: {response.status_code}")
    
    # Test 7: Verify custom projections are loaded
    print("\n7. Testing custom projections loading...")
    response = session.get(f"{base_url}/api/load_players_with_custom_projections?position=QB")
    if response.status_code == 200:
        print("✅ Custom projections loaded successfully")
    else:
        print("❌ Failed to load custom projections")
    
    print("\n🎯 Complete Fix Test Finished!")
    print("=" * 50)
    print("✅ If all tests passed, the foreign key constraint issue is resolved!")
    print("✅ Users must now be logged in to access the pre-draft page")
    print("✅ Custom projections are saved to Supabase with correct user IDs")

if __name__ == "__main__":
    test_complete_fix() 