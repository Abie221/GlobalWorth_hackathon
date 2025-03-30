from flask import Flask, render_template_string

app = Flask(__name__)

def render_page(title, active, content):
    base_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <title>{{ title }}</title>
      <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
      <style>
        body { padding-top: 70px; }
      </style>
    </head>
    <body>
      <nav class="navbar navbar-expand-lg navbar-dark bg-success fixed-top">
        <a class="navbar-brand" href="/">Green Points</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" 
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item {% if active=='points' %}active{% endif %}">
              <a class="nav-link" href="/points">Points Home</a>
            </li>
            <li class="nav-item {% if active=='rewards' %}active{% endif %}">
              <a class="nav-link" href="/rewards">Rewards</a>
            </li>
            <li class="nav-item {% if active=='challenges' %}active{% endif %}">
              <a class="nav-link" href="/challenges">Challenges</a>
            </li>
          </ul>
        </div>
      </nav>
      <div class="container mt-4">
        {{ content | safe }}
      </div>
      <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    '''
    return render_template_string(base_template, title=title, active=active, content=content)

# Index page: Landing page with links to the three sections
@app.route('/')
def index():
    content = '''
    <div class="jumbotron">
      <h1 class="display-4">Welcome to Green Points MVP</h1>
      <p class="lead">Track your green habits, earn points, and redeem exciting rewards while contributing to a sustainable future.</p>
      <hr class="my-4">
      <p>Get started by exploring our features.</p>
      <a class="btn btn-success btn-lg mr-2" href="/points" role="button">Green Points Home</a>
      <a class="btn btn-success btn-lg mr-2" href="/rewards" role="button">Rewards</a>
      <a class="btn btn-success btn-lg" href="/challenges" role="button">Challenges</a>
    </div>
    '''
    return render_page("Green Points MVP", "index", content)

# Page 1: Green Points Home (Habit Tracker, Points History, Current Points)
@app.route('/points')
def points_home():
    current_points = 120
    habit_tracker = {
        '2025-03-25': 1,
        '2025-03-26': 2,
        '2025-03-27': 1,
        '2025-03-28': 3,
        '2025-03-29': 0,
    }
    points_history = [
        {'date': '2025-03-25', 'description': 'Biked to work', 'points': 10},
        {'date': '2025-03-26', 'description': 'Car sharing', 'points': 15},
        {'date': '2025-03-27', 'description': 'Used natural light', 'points': 5},
    ]
    content = f'''
    <h2>Green Points Home</h2>
    <div class="card mb-3">
      <div class="card-body">
        <h4 class="card-title">Current Points: {current_points}</h4>
      </div>
    </div>
    <h3>Habit Tracker</h3>
    <table class="table table-bordered">
      <thead class="thead-light">
        <tr>
          <th>Date</th>
          <th>Points Earned</th>
        </tr>
      </thead>
      <tbody>
    '''
    for date, pts in habit_tracker.items():
        content += f'''
        <tr>
          <td>{date}</td>
          <td>{pts}</td>
        </tr>
        '''
    content += '''
      </tbody>
    </table>
    <h3>Points History</h3>
    <ul class="list-group">
    '''
    for item in points_history:
        content += f'''
      <li class="list-group-item d-flex justify-content-between align-items-center">
        {item['date']} - {item['description']}
        <span class="badge badge-success badge-pill">{item['points']} pts</span>
      </li>
      '''
    content += '''
    </ul>
    '''
    return render_page("Green Points Home", "points", content)

# Page 2: Points Spending & Rewards
@app.route('/rewards')
def rewards():
    rewards_list = [
        {'id': 1, 'category': 'Restaurant', 'title': '10% off Lunch', 'required_points': 50},
        {'id': 2, 'category': 'In-App Benefit', 'title': 'Premium Feature Unlock', 'required_points': 100},
        {'id': 3, 'category': 'Donation', 'title': 'Donate to Green Team', 'required_points': 20},
    ]
    content = '''
    <h2>Points Spending & Rewards</h2>
    <div class="row">
    '''
    for reward in rewards_list:
        content += f'''
      <div class="col-md-4">
        <div class="card mb-3">
          <div class="card-header bg-success text-white">
            {reward['category']}
          </div>
          <div class="card-body">
            <h5 class="card-title">{reward['title']}</h5>
            <p class="card-text">Requires: {reward['required_points']} points</p>
            <a href="#" class="btn btn-outline-success btn-sm">Redeem</a>
          </div>
        </div>
      </div>
      '''
    content += '''
    </div>
    <p class="text-muted"><small>You can also donate points to support the Green Team for impactful eco-projects.</small></p>
    '''
    return render_page("Rewards", "rewards", content)

# Page 3: Education & Challenges
@app.route('/challenges')
def challenges():
    challenges_list = [
        {'id': 1, 'title': 'Bike to Work Challenge', 'description': 'Cycle every day for a week', 'reward_points': 30},
        {'id': 2, 'title': 'Green Office Challenge', 'description': 'Reduce electricity usage in your office', 'reward_points': 25},
    ]
    education_list = [
        {'id': 1, 'title': 'Save Energy Tips', 'content': 'Turn off lights when not needed', 'points_awarded': 5},
        {'id': 2, 'title': 'Water Conservation', 'content': 'Fix leaks and use water wisely', 'points_awarded': 5},
    ]
    events_list = [
        {'id': 1, 'title': 'Green Workshop', 'description': 'Learn about eco-friendly practices', 'date': '2025-04-05'},
    ]
    content = '''
    <h2>Education & Challenges</h2>
    <h3>Challenges</h3>
    <div class="list-group mb-3">
    '''
    for challenge in challenges_list:
        content += f'''
      <a href="#" class="list-group-item list-group-item-action">
        <div class="d-flex w-100 justify-content-between">
          <h5 class="mb-1">{challenge['title']}</h5>
          <small>Reward: {challenge['reward_points']} pts</small>
        </div>
        <p class="mb-1">{challenge['description']}</p>
      </a>
      '''
    content += '''
    </div>
    <h3>Educational Content</h3>
    <div class="list-group mb-3">
    '''
    for edu in education_list:
        content += f'''
      <a href="#" class="list-group-item list-group-item-action">
        <h5 class="mb-1">{edu['title']}</h5>
        <p class="mb-1">{edu['content']}</p>
        <small>Earn: {edu['points_awarded']} pts</small>
      </a>
      '''
    content += '''
    </div>
    <h3>Events</h3>
    <div class="list-group">
    '''
    for event in events_list:
        content += f'''
      <a href="#" class="list-group-item list-group-item-action">
        <div class="d-flex w-100 justify-content-between">
          <h5 class="mb-1">{event['title']}</h5>
          <small>Date: {event['date']}</small>
        </div>
        <p class="mb-1">{event['description']}</p>
      </a>
      '''
    content += '''
    </div>
    '''
    return render_page("Education & Challenges", "challenges", content)

if __name__ == '__main__':
    app.run(debug=True)
