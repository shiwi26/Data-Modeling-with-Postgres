# Project: Data Modeling with Postgres

## Context
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

My role is to create a database schema and ETL pipeline for this analysis. 

### Data
- **Song datasets**: all json files are nested in subdirectories under */data/song_data*. A sample of this files is:

```
{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}
```

- **Log datasets**: all json files are nested in subdirectories under */data/log_data*. A sample of a single row of each files is:

```
{"artist":"Slipknot","auth":"Logged In","firstName":"Aiden","gender":"M","itemInSession":0,"lastName":"Ramirez","length":192.57424,"level":"paid","location":"New York-Newark-Jersey City, NY-NJ-PA","method":"PUT","page":"NextSong","registration":1540283578796.0,"sessionId":19,"song":"Opium Of The People (Album Version)","status":200,"ts":1541639510796,"userAgent":"\"Mozilla\/5.0 (Windows NT 6.1) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"20"}
```

## Database Schema
The schema used for this exercise is the Star Schema: 
There is one main fact table containing all the measures associated to each event (user song plays), 
and 4 dimentional tables, each with a primary key that is being referenced with the fact table.

Why to use relational modeling?
- The data types are structured, no need to use NoSQL
- The volume of data is ok
- Need to model the data to answer business questions, i.e joins

#### Fact Table
**songplays** - records in log data associated with song plays i.e. records with page NextSong
- songplay_id (INT) PRIMARY KEY: ID of each user song play 
- start_time (TIMESTAMP) NOT NULL: Timestamp of beggining of user activity
- user_id (INT) NOT NULL: ID of user
- level (VARCHAR): User level {free | paid}
- song_id (TEXT) NOT NULL: ID of Song played
- artist_id (TEXT) NOT NULL: ID of Artist of the song played
- session_id (INT): ID of the user Session 
- location (VARCHAR): User location 
- user_agent (VARCHAR): Agent used by user to access Sparkify platform

#### Dimension Tables
**users** - users in the app
- user_id (INT) PRIMARY KEY: ID of user
- first_name (VARCHAR) NOT NULL: Name of user
- last_name (VARCHAR) NOT NULL: Last Name of user
- gender (VARCHAR): Gender of user {M | F}
- level (VARCHAR): User level {free | paid}

**songs** - songs in music database
- song_id (TEXT) PRIMARY KEY: ID of Song
- title (VARCHAR) NOT NULL: Title of Song
- artist_id (TEXT) NOT NULL: ID of song Artist
- year (INT): Year of song release
- duration (numeric) NOT NULL: Song duration in milliseconds

**artists** - artists in music database
- artist_id (TEXT) PRIMARY KEY: ID of Artist
- name (VARCHAR) NOT NULL: Name of Artist
- location (VARCHAR): Name of Artist city
- lattitude (numeric): Lattitude location of artist
- longitude (numeric): Longitude location of artist

**time** - timestamps of records in songplays broken down into specific units
- start_time (TIMESTAMP) PRIMARY KEY: Timestamp of row
- hour (INT): Hour associated to start_time
- day (INT): Day associated to start_time
- week (INT): Week of year associated to start_time
- month (INT): Month associated to start_time 
- year (INT): Year associated to start_time
- weekday (TEXT): Name of week day associated to start_time

### Break down of steps followed

1º Wrote DROP, CREATE and INSERT query statements in sql_queries.py

2º Run in console
 ```
python3 create_tables.py
```

3º Used test.ipynb Jupyter Notebook to interactively verify that all tables were created correctly.

4º completed etl.ipynb Notebook to create the ETL pipeline with only one file processed.

5º Verified that the above step was correct by checking with test.ipynb, and then completed etl.py program, which is to process all the data files.

6º Run etl in console:
 ```
python3 etl.py
```
6º Verified final results using test.ipynb notebook

## ETL pipeline (etl.py)

1. Start program by connecting to the sparkify database.

2. Read the songs data as dataframe
    
    a. For each row, only select the columns that I am interested in and then insert data into respective tables
     
3. Read the log data as dataframe

    a. Select rows where page = 'NextSong' only

    b. Convert the 'ts' column to datetime, Extract the timestamp, hour, day, week of year, month, year, and weekday from the column

    c. Store user data into our 'users' table

    d. Finally process the fact table 'songplays'
    Lookup song and artist id from their tables by song name, artist name and song duration that in our song play data. and then load the data together with other columns


### Analysis
%sql SELECT b.title, COUNT(a.user_id) FROM songplays a JOIN songs b ON a.song_id = b.song_id GROUP BY b.title;  

There can be more. 

