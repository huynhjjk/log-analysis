# Project 3: Log Analysis
A python program that connects to the news database to get the top popular articles, popular authors, and days that have requests being errors. This is the third project assignment from [Udacity's Full Stack Web Developer Nanodegree](https://www.udacity.com/nanodegree).

## Prerequisites
Python 2.x is required to run the project. Python can be downloaded [here](https://www.python.org/downloads/).

## Create Views on PostgreSQL (PSQL) Command Line

### articles_view
```
CREATE OR REPLACE VIEW articles_view AS
SELECT title, author, count(title) AS views
FROM articles, log
WHERE log.path LIKE concat('%', articles.slug)
GROUP BY articles.title, articles.author
ORDER BY views DESC;
```

### authors_view
```
CREATE OR REPLACE VIEW authors_view AS
SELECT name, sum(articles_view.views) AS views
FROM articles_view, authors
WHERE authors.id = articles_view.author
GROUP BY authors.name
ORDER BY views DESC;
```

### percent_errors_view
```
CREATE OR REPLACE VIEW percent_errors_view AS
SELECT date(TIME) AS date,
round((100.0 * sum(case when status != '200 OK' then 1 else 0 end)) / count(status), 2) AS percent_error
FROM log
GROUP BY date
ORDER BY percent_error DESC;
```

## Authors
- Code contributed by Johnson Huynh
