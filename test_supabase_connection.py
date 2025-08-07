#!/usr/bin/env python3
"""
Test Supabase Connection
This script tests the Supabase connection and verifies the database setup.
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client

def test_supabase_connection():
    """Test the Supabase connection and database setup."""
    
    print("🧪 Testing Supabase Connection")
    print("=" * 50)
    
    # Load environment variables
    load_dotenv()
    
    # Get Supabase credentials
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")
    
    print(f"Supabase URL: {supabase_url}")
    print(f"Supabase Key: {supabase_key[:20]}...")
    
    if not supabase_url or not supabase_key:
        print("❌ Missing Supabase credentials in .env file")
        return
    
    try:
        # Create Supabase client
        supabase: Client = create_client(supabase_url, supabase_key)
        print("✅ Supabase client created successfully")
        
        # Test connection by checking if tables exist
        print("\n📋 Checking database tables...")
        
        # Check users table
        try:
            result = supabase.table('users').select('*').limit(1).execute()
            print("✅ users table exists")
        except Exception as e:
            print(f"❌ users table error: {e}")
        
        # Check user_custom_projections table
        try:
            result = supabase.table('user_custom_projections').select('*').limit(1).execute()
            print("✅ user_custom_projections table exists")
        except Exception as e:
            print(f"❌ user_custom_projections table error: {e}")
        
        # Check user_draft_sessions table
        try:
            result = supabase.table('user_draft_sessions').select('*').limit(1).execute()
            print("✅ user_draft_sessions table exists")
        except Exception as e:
            print(f"❌ user_draft_sessions table error: {e}")
        
        # Check if user exists
        print("\n👤 Checking user account...")
        try:
            result = supabase.table('users').select('*').eq('email', 'egclessuras@gmail.com').execute()
            if result.data:
                print("✅ User account exists")
                print(f"   User ID: {result.data[0]['id']}")
            else:
                print("❌ User account not found")
        except Exception as e:
            print(f"❌ Error checking user: {e}")
        
        print("\n🎉 Supabase connection test complete!")
        
    except Exception as e:
        print(f"❌ Failed to connect to Supabase: {e}")

if __name__ == "__main__":
    test_supabase_connection() 