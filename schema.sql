CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    voter_id TEXT UNIQUE,
    password TEXT,
    biometric_type TEXT
);

CREATE TABLE IF NOT EXISTS biometric_status (
    bio_id INTEGER PRIMARY KEY AUTOINCREMENT,
    voter_id TEXT,
    fingerprint TEXT,
    face TEXT
);

CREATE TABLE IF NOT EXISTS votes (
    vote_id INTEGER PRIMARY KEY AUTOINCREMENT,
    voter_id TEXT UNIQUE,
    party TEXT,
    vote_time DATETIME DEFAULT CURRENT_TIMESTAMP
);
