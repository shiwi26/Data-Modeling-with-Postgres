# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays
                            (
                            songplay_id SERIAL PRIMARY KEY,
                            start_time timestamp REFERENCES time(start_time),
                            user_id int REFERENCES users(user_id),
                            level varchar,
                            song_id text REFERENCES songs(song_id),
                            artist_id text REFERENCES artists(artist_id),
                            session_id int,
                            location varchar,
                            user_agent varchar
                            );""")

user_table_create = ("""create table if not exists users 
                        (
                        user_id INT PRIMARY KEY, 
                        first_name varchar, 
                        last_name varchar, 
                        gender varchar, 
                        level varchar
                        );""")

song_table_create = ("""create table if not exists songs 
                        (
                        song_id text PRIMARY KEY, 
                        title varchar, 
                        artist_id text, 
                        year int, 
                        duration numeric
                        );""")

artist_table_create = ("""create table if not exists artists 
                            (
                            artist_id text PRIMARY KEY, 
                            name varchar, 
                            location varchar, 
                            latitude numeric, 
                            longitude numeric
                            );""")

time_table_create = ("""create table if not exists time 
                        (
                        start_time timestamp PRIMARY KEY, 
                        hour int, day int, 
                        week int, 
                        month int,
                        Year int, 
                        weekday TEXT
                        );""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays (
                            start_time,
                            user_id,
                            level,
                            song_id,
                            artist_id,
                            session_id,
                            location,
                            user_agent)
                        values (%s,%s,%s,%s,%s,%s,%s,%s)
                        """)

user_table_insert = ("""insert into users (user_id, 
                        first_name, 
                        last_name, 
                        gender, 
                        level)
                        values (%s,%s,%s,%s,%s)
                        on conflict (user_id)
                        do update
                            set level = excluded.level
                        """)

song_table_insert = ("""insert into songs (song_id,
                        title,
                        artist_id,
                        year,
                        duration)
                        values (%s,%s,%s,%s,%s)
                        on conflict (song_id)
                        do nothing
                        """)

artist_table_insert = ("""insert into artists (artist_id,
                        name,
                        location,
                        latitude,
                        longitude)
                        values (%s,%s,%s,%s,%s)
                        on conflict (artist_id)
                        do nothing
                        """)


time_table_insert = ("""insert into time (start_time, 
                        hour, day, 
                        week, 
                        month,
                        Year, 
                        weekday)
                        values (%s,%s,%s,%s,%s,%s,%s)
                        on conflict (start_time)
                        do nothing
                        """)

# FIND SONGS

song_select = ("""select songs.song_id, artists.artist_id
                from songs join artists on songs.artist_id = artists.artist_id
                where songs.title = %s
                  AND
                artists.name = %s
                  AND
                songs.duration = %s
                """)

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]