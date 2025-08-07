#!/usr/bin/env python3
"""
Debug User ID Issue
This script helps debug the foreign key constraint issue.
"""

import requests
import json

def debug_user_id_issue():
    """Debug the user ID foreign key constraint issue."""
    
    base_url = "http://localhost:4000"
    session = requests.Session()
    
    print("🔍 Debugging User ID Issue")
    print("=" * 50)
    
    # Test 1: Check current session
    print("1. Checking current session...")
    response = session.get(f"{base_url}/api/auth/check")
    print(f"Auth check: {response.text}")
    
    # Test 2: Login and get user ID
    print("\n2. Logging in...")
    login_data = {
        "email": "egclessuras@gmail.com",
        "password": "JohnWall2"
    }
    
    response = session.post(f"{base_url}/api/auth/login", json=login_data)
    print(f"Login response: {response.text}")
    
    if response.status_code == 200:
        result = response.json()
        user_id = result.get('user', {}).get('id')
        print(f"User ID from login: {user_id}")
        
        # Test 3: Try to save a custom projection
        print("\n3. Testing custom projection save...")
        save_data = {
            "player_name": "Test Player",
            "position": "QB",
            "custom_stats": {
                "passing_yards": 4000,
                "passing_tds": 30
            }
        }
        
        response = session.post(f"{base_url}/api/save_custom_projection", json=save_data)
        print(f"Save response: {response.text}")
        
        # Test 4: Check user info
        print("\n4. Checking user info...")
        response = session.get(f"{base_url}/api/auth/user")
        print(f"User info: {response.text}")
    
    print("\n🎯 Debug Complete!")

if __name__ == "__main__":
    debug_user_id_issue() 