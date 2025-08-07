# PickProphet - Fantasy Football Draft Assistant

A comprehensive fantasy football draft assistant with custom projections, simulations, and real-time recommendations.

## Features

- **Custom Projections**: Save and load custom player projections
- **Draft Simulations**: Run 40 simulations for accurate recommendations
- **Real-time Recommendations**: Get live draft advice based on your roster
- **User Authentication**: Secure login with Supabase
- **Multiple Scoring Formats**: PPR, Half-PPR, and Non-PPR support
- **Bench Value Optimization**: Smart bench value calculations

## Railway Deployment

This app is configured for Railway deployment with the following files:

- `fantasy_draft_web_enhanced.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `Procfile` - Railway process definition
- `railway.json` - Railway configuration
- `templates/` - HTML templates
- `*.csv` - Player projection data

## Environment Variables Required

Set these in Railway dashboard:

```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-supabase-anon-key
FLASK_SECRET_KEY=your-secret-key
```

## Local Development

```bash
python3 fantasy_draft_web_enhanced.py
```

Access at: http://localhost:4000 