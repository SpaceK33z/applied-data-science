# Activity 2

Query to create the users table:

```
create table users (id int, age int, gender string, occupation string, zip_code int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '|' STORED AS TEXTFILE;
```

Put data files on HDFS:

```
hadoop fs -put ml-data/u.user
```

Load data into users table:

```
load data inpath 'u.user' overwrite into table users;
```

Query to create the movies table:

```
create table movies (id int, title string, release_date string, video_release_date string, imdb_url string, genre_unknown int, genre_action int, genre_adventure int, genre_animation int, genre_childrens int, genre_comedy int, genre_crime int, genre_documentary int, genre_drama int, genre_fantasy int, genre_film_noir int, genre_horror int, genre_musical int, genre_mystery int, genre_romance int, genre_sci_fi int, genre_thriller int, genre_war int, genre_western int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '|' STORED AS TEXTFILE;
```

Query to create the ratings table:

```
create table ratings (user_id int, item_id int, rating int, timestamp int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t' STORED AS TEXTFILE;
```

# Activity 3
## 1
F   273
M   670

```
select gender, count(*) from users group by gender;
```

## 2
administrator   F   36
artist  F   13
educator    F   26
engineer    F   2
entertainment   F   2
executive   F   3
healthcare  F   11
homemaker   F   6
lawyer  F   2
librarian   F   29
marketing   F   10
none    F   4
other   F   36
programmer  F   6
retired F   1
salesman    F   3
scientist   F   3
student F   60
technician  F   1
writer  F   19
administrator   M   43
artist  M   15
doctor  M   7
educator    M   69
engineer    M   65
entertainment   M   16
executive   M   29
healthcare  M   5
homemaker   M   1
lawyer  M   10
librarian   M   22
marketing   M   16
none    M   5
other   M   69
programmer  M   60
retired M   13
salesman    M   9
scientist   M   28
student M   136
technician  M   26
writer  M   26

```
select occupation, gender, count(*) from users group by gender, occupation;
```

## 3

M   Before the Rain (Pred dozhdot) (1994)   5.0
F   Sliver (1993)   5.0

```
SELECT users.gender, movies.title, avg(ratings.rating) as avg_rating FROM movies JOIN ratings ON (movies.id = ratings.item_id) JOIN users ON (ratings.user_id = users.id) WHERE users.occupation = 'student' GROUP BY users.gender, movies.title ORDER BY avg_rating desc LIMIT 1;
```

# Activity 4
I used AVG to get all the scores and just limited the query to display only one.

# Activity 5
IMDB says it uses a 'weighted average'. This means that the votes of some users weigh more then others.
They also try to filter out fake votes (called vote stuffing).

More info: http://www.imdb.com/help/show_leaf?votes
Each movie also has detailed voting information available: http://www.imdb.com/title/tt0368891/ratings
