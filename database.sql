-- Relational database schema for a green habit category
-- Users table: stores user profile and authentication details
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Sessions table: manages user sessions for authentication
CREATE TABLE sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    token VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Points Ledger table: records every points transaction (earned or spent)
CREATE TABLE points_ledger (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    transaction_type ENUM('earned', 'spent'),
    source VARCHAR(255) COMMENT 'e.g., Habit, Challenge, Redemption, Donation',
    description VARCHAR(255),
    points INT,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- User Habits table: tracks daily green actions (habit calendar)
CREATE TABLE user_habits (
    habit_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    habit_date DATE,
    habit_type VARCHAR(255) COMMENT 'e.g., Bike to Work, Turned off Lights',
    points_awarded INT,
    details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Rewards Catalog table: lists available rewards and spending options
CREATE TABLE rewards_catalog (
    reward_id INT AUTO_INCREMENT PRIMARY KEY,
    category VARCHAR(255) COMMENT 'e.g., Restaurant, In-App Benefit, Donation',
    title VARCHAR(255),
    description TEXT,
    required_points INT,
    active BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Reward Redemptions table: records rewards that users have redeemed
CREATE TABLE reward_redemptions (
    redemption_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    reward_id INT NOT NULL,
    redemption_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    points_spent INT,
    status ENUM('pending', 'completed', 'cancelled'),
    notes VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (reward_id) REFERENCES rewards_catalog(reward_id)
);

-- Challenges table: defines the green challenges available to users
CREATE TABLE challenges (
    challenge_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    challenge_type ENUM('solo', 'team'),
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    reward_points INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Challenge Participation table: links users with the challenges they join
CREATE TABLE challenge_participation (
    participation_id INT AUTO_INCREMENT PRIMARY KEY,
    challenge_id INT NOT NULL,
    user_id INT NOT NULL,
    status ENUM('in_progress', 'completed'),
    points_awarded INT,
    completed_at TIMESTAMP NULL,
    FOREIGN KEY (challenge_id) REFERENCES challenges(challenge_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Educational Content table: stores green tips, quizzes, and other educational materials
CREATE TABLE educational_content (
    content_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    content_type ENUM('tip', 'quiz', 'video', 'article'),
    content_text TEXT,
    points_awarded INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User Educational Progress table: tracks which educational items users have completed
CREATE TABLE user_educational_progress (
    progress_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    content_id INT NOT NULL,
    completion_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    score INT,
    points_awarded INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (content_id) REFERENCES educational_content(content_id)
);

-- Events table: holds details of eco-friendly events
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    event_date TIMESTAMP,
    location VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Event Participation table: records user registrations/participation in events
CREATE TABLE event_participation (
    participation_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    user_id INT NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status ENUM('registered', 'attended', 'cancelled'),
    FOREIGN KEY (event_id) REFERENCES events(event_id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Green Team Donations table: tracks points donated by users for communal green initiatives
CREATE TABLE green_team_donations (
    donation_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    donation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    points_donated INT,
    purpose VARCHAR(255) COMMENT 'e.g., Tree Planting',
    notes TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
