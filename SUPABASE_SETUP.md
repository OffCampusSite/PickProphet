# Supabase Setup Guide

## 1. Create a Supabase Account
1. Go to https://supabase.com
2. Sign up for a free account
3. Create a new project

## 2. Get Your Credentials
1. In your Supabase dashboard, go to Settings > API
2. Copy your Project URL and anon/public key
3. Create a `.env` file in the project root with:
```
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_anon_key_here
```

## 3. Database Schema
The application will automatically create the required table when it first connects to Supabase.

The `custom_projections` table will have the following structure:
- `user_id` (text): User identifier
- `player_name` (text): Player name
- `position` (text): Player position (QB, RB, WR, TE, K, DST)
- `custom_stats` (jsonb): Custom player statistics
- `ppr_projection` (numeric): PPR scoring projection
- `half_ppr_projection` (numeric): Half-PPR scoring projection
- `non_ppr_projection` (numeric): Standard scoring projection
- `created_at` (timestamp): Record creation time
- `updated_at` (timestamp): Record last update time

## 4. Features
- **Persistent Storage**: Custom projections are saved to Supabase and persist across sessions
- **User-Specific**: Each user's custom projections are stored separately
- **Automatic Sync**: Changes are automatically synced between local cache and database
- **Fallback Mode**: If Supabase is not configured, the app runs in local-only mode

## 5. Troubleshooting
- If you see "Supabase credentials not found" messages, the app will run in local-only mode
- Check your `.env` file has the correct credentials
- Ensure your Supabase project is active and accessible 