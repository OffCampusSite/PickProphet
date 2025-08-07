#!/usr/bin/env python3
"""
Test Supabase Integration
This script tests that custom projections are being saved to and loaded from Supabase.
"""

import requests
import json

def test_supabase_integration():
    """Test that custom projections are saved to and loaded from Supabase."""
    
    base_url = "http://localhost:4000"
    session = requests.Session()
    
    print("🧪 Testing Supabase Integration")
    print("=" * 50)
    
    # Test 1: Check if server is running
    try:
        response = session.get(f"{base_url}/api/auth/check")
        print(f"✅ Server is running (Status: {response.status_code})")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running. Please start the application first:")
        print("   python3 fantasy_draft_web_enhanced.py")
        return
    
    # Test 2: Login
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
    
    # Test 3: Save a custom projection to Supabase
    print("\n💾 Testing custom projection save to Supabase...")
    save_data = {
        "player_name": "Test Player QB",
        "position": "QB",
        "custom_stats": {
            "passing_yards": 4500,
            "passing_tds": 30,
            "interceptions": 12,
            "rushing_yards": 300,
            "rushing_tds": 3
        }
    }
    
    response = session.post(f"{base_url}/api/save_custom_projection", json=save_data)
    if response.status_code == 200:
        result = response.json()
        if result.get('success'):
            print("✅ Custom projection saved to Supabase successfully!")
            print(f"   Message: {result.get('message')}")
            print(f"   Projections: {result.get('projections')}")
        else:
            print(f"❌ Save failed: {result.get('error')}")
            return
    else:
        print(f"❌ Save request failed: {response.text}")
        return
    
    # Test 4: Initialize draft to load custom projections
    print("\n🎯 Testing draft initialization with custom projections...")
    init_data = {
        "num_teams": 12,
        "user_position": 1,
        "scoring_format": "ppr"
    }
    
    response = session.post(f"{base_url}/api/init", json=init_data)
    if response.status_code == 200:
        result = response.json()
        if result.get('success'):
            print("✅ Draft initialized successfully!")
            print(f"   Custom projections loaded: {result.get('draft_info', {}).get('custom_projections_loaded', 0)}")
        else:
            print(f"❌ Draft initialization failed: {result.get('error')}")
    else:
        print(f"❌ Draft initialization request failed: {response.text}")
    
    # Test 5: Get available players to see if custom projections are loaded
    print("\n📊 Testing available players with custom projections...")
    response = session.get(f"{base_url}/api/available_players?position=QB")
    if response.status_code == 200:
        result = response.json()
        players = result.get('players', [])
        print(f"✅ Found {len(players)} available QB players")
        
        # Look for our test player
        test_player = None
        for player in players:
            if player['name'] == 'Test Player QB':
                test_player = player
                break
        
        if test_player:
            print(f"✅ Found our test player: {test_player['name']}")
            print(f"   Is customized: {test_player.get('is_customized', False)}")
            print(f"   Projected points: {test_player.get('projected_points', 'N/A')}")
        else:
            print("⚠️  Test player not found in available players")
    
    # Test 6: Reset the test player
    print("\n🔄 Testing custom projection reset...")
    reset_data = {
        "player_name": "Test Player QB"
    }
    
    response = session.post(f"{base_url}/api/reset_custom_projection", json=reset_data)
    if response.status_code == 200:
        result = response.json()
        if result.get('success'):
            print("✅ Custom projection reset successfully!")
        else:
            print(f"❌ Reset failed: {result.get('error')}")
    else:
        print(f"❌ Reset request failed: {response.text}")
    
    print("\n🎉 Supabase Integration Test Complete!")
    print("=" * 50)
    print("✅ If all tests passed, Supabase integration is working correctly!")

if __name__ == "__main__":
    test_supabase_integration() 