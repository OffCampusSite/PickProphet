# PickProphet - Fantasy Draft Assistant

A comprehensive fantasy football draft assistant with real-time recommendations, player projections, and draft simulation capabilities.

## 🚀 Features

- **Real-time Draft Assistant**: Get AI-powered recommendations during your draft
- **Multiple Scoring Formats**: Support for PPR, Half-PPR, and Non-PPR leagues
- **Player Projections**: 392+ players with detailed projections and rankings
- **Draft Simulation**: Practice drafts with AI opponents
- **User Management**: Secure login and draft history tracking
- **Export Functionality**: Export draft results and team analysis

## 📊 Player Data

- **Total Players**: 392 players across all positions
- **Data Source**: OALFFL (Ohio Outcasts Fantasy Football League) rankings
- **Positions**: QB, RB, WR, TE, K, DST
- **Updated**: September 2025 projections

## 🛠️ Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: Supabase (PostgreSQL)
- **Deployment**: Railway
- **Data Processing**: Pandas, NumPy

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/egclessuras-svg/PickProphet.git
   cd PickProphet
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python3 run_port_5201.py
   ```

4. **Access the app**
   - Open http://localhost:5201 in your browser

### Railway Deployment

1. **Connect to Railway**
   - Go to [Railway.app](https://railway.app)
   - Connect your GitHub account
   - Import this repository

2. **Set Environment Variables** (Optional)
   ```
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   FLASK_SECRET_KEY=your_secret_key
   ```

3. **Deploy**
   - Railway will automatically deploy from the main branch
   - The app will be available at your Railway domain

## 📁 Project Structure

```
PickProphet/
├── fantasy_draft_web_enhanced.py    # Main Flask application
├── fantasy_draft_assistant_v2_clean.py  # Core draft logic
├── supabase_manager.py              # Database management
├── templates/                       # HTML templates
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── pre_draft.html
│   ├── draft.html
│   └── user.html
├── rankings.csv                     # Player rankings data
├── requirements.txt                 # Python dependencies
├── Procfile                        # Railway deployment config
├── railway.json                    # Railway configuration
└── README.md                       # This file
```

## 🔧 Configuration

### Environment Variables

- `PORT`: Server port (Railway sets this automatically)
- `SUPABASE_URL`: Supabase database URL (optional)
- `SUPABASE_KEY`: Supabase API key (optional)
- `FLASK_SECRET_KEY`: Flask session secret key (optional)

### CSV Data Format

The `rankings.csv` file should contain:
- Rank, Position, Team, Name, Bye Week, Projected Points
- Headers in row 6
- Data starting from row 7

## 🎯 Usage

1. **Register/Login**: Create an account or login
2. **Initialize Draft**: Set your draft position and league settings
3. **Draft**: Get real-time recommendations and make picks
4. **Export**: Download your draft results

## 🔄 Updating Player Data

To update player rankings:

1. Replace `rankings.csv` with new data
2. Ensure the format matches the expected structure
3. Restart the application

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   lsof -ti:5201 | xargs kill -9
   ```

2. **CSV file not found**
   - Ensure `rankings.csv` is in the project root
   - Check file permissions

3. **Database connection issues**
   - Verify Supabase credentials
   - Check network connectivity

## 📝 License

This project is for personal use. All rights reserved.

## 🤝 Contributing

This is a personal project. For issues or suggestions, please contact the repository owner.

## 📞 Support

For technical support or questions, please open an issue on GitHub.

---

**PickProphet** - Making fantasy drafts smarter, one pick at a time! 🏈