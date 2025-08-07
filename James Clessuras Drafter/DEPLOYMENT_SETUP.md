# PickProphet Deployment Setup Guide

## Database Setup (Supabase)

### 1. Create Supabase Project
1. Go to [supabase.com](https://supabase.com)
2. Create a new project
3. Note your project URL and anon key

### 2. Database Schema
Run these SQL commands in your Supabase SQL editor:

```sql
-- Enable Row Level Security
ALTER TABLE auth.users ENABLE ROW LEVEL SECURITY;

-- User custom projections table
CREATE TABLE user_custom_projections (
    id SERIAL PRIMARY KEY,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    player_name VARCHAR(255) NOT NULL,
    position VARCHAR(10) NOT NULL,
    custom_stats JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(user_id, player_name)
);

-- User draft sessions table
CREATE TABLE user_draft_sessions (
    id SERIAL PRIMARY KEY,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    session_name VARCHAR(255),
    league_settings JSONB,
    draft_order JSONB,
    drafted_players JSONB,
    current_pick INTEGER DEFAULT 1,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- User rosters table
CREATE TABLE user_rosters (
    id SERIAL PRIMARY KEY,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    draft_session_id INTEGER REFERENCES user_draft_sessions(id) ON DELETE CASCADE,
    team_name VARCHAR(255),
    players JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Enable RLS on all tables
ALTER TABLE user_custom_projections ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_draft_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_rosters ENABLE ROW LEVEL SECURITY;

-- Create RLS policies
CREATE POLICY "Users can view own custom projections" ON user_custom_projections
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own custom projections" ON user_custom_projections
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own custom projections" ON user_custom_projections
    FOR UPDATE USING (auth.uid() = user_id);

CREATE POLICY "Users can delete own custom projections" ON user_custom_projections
    FOR DELETE USING (auth.uid() = user_id);

CREATE POLICY "Users can view own draft sessions" ON user_draft_sessions
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own draft sessions" ON user_draft_sessions
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own draft sessions" ON user_draft_sessions
    FOR UPDATE USING (auth.uid() = user_id);

CREATE POLICY "Users can delete own draft sessions" ON user_draft_sessions
    FOR DELETE USING (auth.uid() = user_id);

CREATE POLICY "Users can view own rosters" ON user_rosters
    FOR SELECT USING (auth.uid() = user_id);

CREATE POLICY "Users can insert own rosters" ON user_rosters
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Users can update own rosters" ON user_rosters
    FOR UPDATE USING (auth.uid() = user_id);

CREATE POLICY "Users can delete own rosters" ON user_rosters
    FOR DELETE USING (auth.uid() = user_id);
```

### 3. Environment Configuration
Create a `.env` file in your project root:

```env
# Supabase Configuration
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key

# Flask Configuration
FLASK_SECRET_KEY=your_flask_secret_key_here
FLASK_ENV=development
```

## Deployment Options

### Option 1: Vercel (Recommended)
1. Install Vercel CLI: `npm i -g vercel`
2. Add `vercel.json` to your project:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "fantasy_draft_web_enhanced.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "fantasy_draft_web_enhanced.py"
    }
  ]
}
```

3. Deploy: `vercel --prod`

### Option 2: Railway
1. Connect your GitHub repo to Railway
2. Set environment variables in Railway dashboard
3. Deploy automatically

### Option 3: Heroku
1. Create `Procfile`:
```
web: python fantasy_draft_web_enhanced.py
```

2. Deploy using Heroku CLI or GitHub integration

## Features Added

### User Authentication
- ✅ Login/Register pages
- ✅ Session management
- ✅ Protected routes

### User-Specific Data
- ✅ Custom projections per user
- ✅ Draft sessions per user
- ✅ Roster management per user

### Database Integration
- ✅ Supabase connection
- ✅ Row Level Security (RLS)
- ✅ User data isolation

## Next Steps

1. **Set up Supabase project** and run the SQL schema
2. **Configure environment variables** with your Supabase credentials
3. **Deploy to your preferred platform**
4. **Test user registration and login**
5. **Test custom projections functionality**

## Security Features

- ✅ Row Level Security (RLS) on all tables
- ✅ User authentication required for all data access
- ✅ Session-based authentication
- ✅ Password validation
- ✅ CSRF protection (Flask built-in)

## Data Flow

1. **User registers/logs in** → Supabase Auth
2. **User creates custom projections** → Stored in `user_custom_projections`
3. **User starts draft session** → Stored in `user_draft_sessions`
4. **User drafts players** → Stored in `user_rosters`
5. **All data is user-specific** → RLS ensures data isolation 