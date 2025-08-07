#!/usr/bin/env python3
"""
Test New Supabase Setup
This script tests the new Supabase setup with proper user authentication.
"""

import requests
import json

def test_new_supabase_setup():
    """Test the new Supabase setup."""
    
    base_url = "http://localhost:4000"
    session = requests.Session()
    
    print("🧪 Testing New Supabase Setup")
    print("=" * 50)
    
    # Test 1: Check if server is running
    try:
        response = session.get(f"{base_url}/api/auth/check")
        print(f"✅ Server is running (Status: {response.status_code})")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the application first:")
        print("   python3 fantasy_draft_web_enhanced.py")
        return
    
    # Test 2: Try login with user credentials
    print("\n🔐 Testing login with egclessuras@gmail.com...")
    login_data = {
        "email": "egclessuras@gmail.com",
        "password": "JohnWall2"
    }
    
    response = session.post(f"{base_url}/api/auth/login", json=login_data)
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Login successful!")
        print(f"   User ID: {result.get('user', {}).get('id', 'Unknown')}")
        print(f"   Email: {result.get('user', {}).get('email', 'Unknown')}")
        print(f"   Message: {result.get('message', 'Unknown')}")
    else:
        print(f"❌ Login failed: {response.text}")
        return
    
    # Test 3: Check authentication status
    print("\n🔍 Checking authentication status...")
    response = session.get(f"{base_url}/api/auth/check")
    if response.status_code == 200:
        result = response.json()
        print(f"✅ Authentication check successful!")
        print(f"   Authenticated: {result.get('authenticated', False)}")
        print(f"   User ID: {result.get('user_id', 'Unknown')}")
    else:
        print(f"❌ Authentication check failed: {response.text}")
    
    # Test 4: Try to save a custom projection
    print("\n💾 Testing custom projection save...")
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
    
    # Test 5: Try to load custom projections
    print("\n📥 Testing custom projection loading...")
    response = session.get(f"{base_url}/api/available_players?position=QB")
    if response.status_code == 200:
        print("✅ Available players loaded successfully!")
    else:
        print(f"❌ Failed to load available players: {response.text}")
    
    print("\n🎉 New Supabase Setup Test Complete!")
    print("=" * 50)

if __name__ == "__main__":
    test_new_supabase_setup() 