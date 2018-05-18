# Project 3: Log Analysis
A python program that connects to the news database to get the top popular articles, popular authors, and days that have requests being errors. This is the third project assignment from [Udacity's Full Stack Web Developer Nanodegree](https://www.udacity.com/nanodegree).

## Prerequisites

### Python
Python 2.x is required to run the project. Python can be downloaded [here](https://www.python.org/downloads/).

### VirtualBox
VirtualBox is required to run on the virtual machine. The download link can be found here [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).

### Vagrant
Vagrant is required and used with VirtualBox to create a local development environment. You can download it [here](https://www.vagrantup.com/downloads.html).

### Udacity's News Data
You will need to download and extract the zip file to get newsdata.sql. Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

### Udacity's Full Stack Nanodegree VM Configuration Repository
This Virtual Machine Configuration will be provided by Udacity. It will contain the directory **fullstack-nanodegree-vm** Download the VM Connfiguration [here](https://github.com/udacity/fullstack-nanodegree-vm).

### How to use
1. Make sure that both **log.py** and **newsdata.sql** are inside the **fullstack-nanodegree-vm/vagrant** directory.
2. Open the terminal and **cd** into the **fullstack-nanodegree-vm/vagrant** directory.<br>
3. Enter the command **vagrant up** to run vagrant<br>
4. Enter the command **vagrant ssh** to login into the VM<br>
5. Enter the command **psql -d news -f newsdata.sql** to load the **newsdata.sql** onto the **news database**<br>
6. Enter the command **psql -d news** to connect to the **news database**.<br>
7. Enter the commands provided under **Create Views on PostgreSQL (PSQL) Command Line** to create the three views: **articles_view**, **authors_view**, and **percent_errors_view**.<br>
8. Enter the command **python log.py** to print out the answers for the following three questions:<br>
    1) What are the most popular three articles of all time?<br>
    2) Who are the most popular article authors of all time?<br>
    3) On which days did more than 1% of requests lead to errors?<br>

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
