# PickProphet - Fantasy Football Draft Assistant

A comprehensive fantasy football draft assistant with custom projections, simulations, and real-time recommendations.

## Features

- **Custom Projections**: Save and load custom player projections via Supabase
- **Draft Simulations**: Run 40 simulations for accurate recommendations
- **Real-time Recommendations**: Get live draft advice based on your roster
- **User Authentication**: Secure login with Supabase
- **Multiple Scoring Formats**: PPR, Half-PPR, and Non-PPR support
- **Bench Value Optimization**: Smart bench value calculations

## Recent Updates

- **Bench Values**: TE (5%), RB/WR first (27%), RB/WR second (18%)
- **Simulation Count**: Increased to 40 simulations for better accuracy
- **Supabase Integration**: All data saved to and loaded from Supabase
- **Railway Deployment Ready**: Clean repository with essential files only

## Railway Deployment

### Prerequisites
1. **Supabase Project**: Set up with the required tables
2. **GitHub Repository**: Code pushed to GitHub
3. **Railway Account**: Connected to GitHub

### Deployment Steps

1. **Connect to Railway**
   - Go to [railway.app](https://railway.app)
   - Sign in with your GitHub account
   - Click **"New Project"**
   - Select **"Deploy from GitHub repo"**
   - Choose your repository

2. **Configure Environment Variables**
   - Go to your project's **"Variables"** tab
   - Add these environment variables:
   ```
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-supabase-anon-key
   FLASK_SECRET_KEY=your-secret-key
   ```

3. **Deploy**
   - Railway will automatically detect the Python project
   - It will install dependencies from `requirements.txt`
   - The app will start using the `Procfile`

### Environment Variables

Create a `.env` file locally (not committed to git):
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-anon-key
FLASK_SECRET_KEY=your-secret-key
```

## Local Development

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Environment Variables**
   - Create `.env` file with your Supabase credentials

3. **Run the Application**
   ```bash
   python3 fantasy_draft_web_enhanced.py
   ```

4. **Access the Application**
   - Open http://localhost:4000
   - Login with your credentials

## File Structure

```
├── fantasy_draft_web_enhanced.py    # Main Flask application
├── requirements.txt                  # Python dependencies
├── Procfile                         # Railway deployment
├── railway.json                     # Railway configuration
├── templates/                       # HTML templates
│   ├── index.html                   # Main dashboard
│   ├── draft.html                   # Draft room
│   ├── pre_draft.html              # Pre-draft analysis
│   ├── login.html                   # Login page
│   ├── register.html                # Registration page
│   └── user.html                    # User profile
├── *.csv                           # Player projection data
└── README.md                       # This file
```

## Database Setup

The application requires a Supabase project with the following tables:
- `users` - User authentication
- `user_custom_projections` - Custom player projections
- `user_draft_sessions` - Draft session data
- `user_rosters` - User roster data
- `completed_drafts` - Completed draft data

## Support

For deployment issues, check:
1. Environment variables are correctly set
2. Supabase project is properly configured
3. Railway logs for any error messages 