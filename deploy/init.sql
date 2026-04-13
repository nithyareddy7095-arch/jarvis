CREATE TABLE IF NOT EXISTS farmers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(120) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    farm_name VARCHAR(120) DEFAULT '',
    crop_types TEXT DEFAULT '',
    soil_type VARCHAR(80) DEFAULT '',
    gps_lat DOUBLE PRECISION DEFAULT 0,
    gps_lng DOUBLE PRECISION DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS community_videos (
    id SERIAL PRIMARY KEY,
    farmer_id INT NOT NULL REFERENCES farmers(id),
    title VARCHAR(160) NOT NULL,
    description TEXT DEFAULT '',
    video_url VARCHAR(512) NOT NULL,
    likes INT DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);
