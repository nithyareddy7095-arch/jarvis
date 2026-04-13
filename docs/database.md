# PostgreSQL Schema

## Core Tables

### `farmers`
- `id` PK
- `full_name`
- `email` (unique)
- `hashed_password`
- `farm_name`
- `crop_types`
- `soil_type`
- `gps_lat`, `gps_lng`
- `created_at`

### `community_videos`
- `id` PK
- `farmer_id` FK -> farmers.id
- `title`
- `description`
- `video_url`
- `likes`
- `created_at`

## SQL bootstrap

See `deploy/init.sql` for executable schema.
