from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_BASE = 'https://ipl-api-t4ek.onrender.com/api'


def _get(endpoint, params=None):
    """Helper — call the IPL API and return parsed JSON, or None on error."""
    try:
        r = requests.get(f'{API_BASE}/{endpoint}', params=params, timeout=5)
        if r.status_code == 200:
            return r.json()
    except requests.RequestException:
        pass
    return None


@app.route('/')
def home():
    data = _get('teams')
    teams = sorted(data['teams']) if data else []
    seasons_data = _get('season-stats')
    champions = seasons_data.get('champions', {}) if seasons_data else {}
    return render_template('index.html', teams=teams, champions=champions)


@app.route('/teamvteam')
def team_vs_team():
    team1 = request.args.get('team1', '')
    team2 = request.args.get('team2', '')
    data  = _get('teams')
    teams = sorted(data['teams']) if data else []
    result = None
    if team1 and team2:
        result = _get('teamVteam', {'team1': team1, 'team2': team2})
    return render_template('teamvteam.html', teams=teams, team1=team1, team2=team2, result=result)


@app.route('/team')
def team_record():
    team = request.args.get('team', '')
    data = _get('teams')
    teams = sorted(data['teams']) if data else []
    result = None
    if team:
        result = _get('team-record', {'team': team})
        if result:
            result = result.get(team, {})
    return render_template('team.html', teams=teams, selected=team, result=result)


@app.route('/batsman')
def batsman():
    name   = request.args.get('batsman', '')
    result = None
    if name:
        raw = _get('batting-record', {'batsman': name})
        if raw:
            result = raw.get(name, {})
    return render_template('batsman.html', name=name, result=result)


@app.route('/bowler')
def bowler():
    name   = request.args.get('bowler', '')
    result = None
    if name:
        raw = _get('bowling-record', {'bowler': name})
        if raw:
            result = raw.get(name, {})
    return render_template('bowler.html', name=name, result=result)


@app.route('/season')
def season():
    season_val = request.args.get('season', '')
    result = _get('season-stats', {'season': season_val} if season_val else {})
    top    = _get('top-performers', {'season': season_val, 'top': 10} if season_val else {'top': 10})
    seasons_list = result.get('availableSeasons', []) if result else []
    return render_template('season.html',
                           selected=season_val,
                           seasons=seasons_list,
                           stats=result,
                           top=top)


if __name__ == '__main__':
    app.run(debug=True, port=8080)
