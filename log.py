#!/usr/bin/env python2

import psycopg2

DB_NAME = 'news'
NUMBER_OF_ARTICLES = 3
PERCENT_ERROR = 1


def connectDB():
    """ Connect to the PSQL database """
    try:
        return psycopg2.connect(database=DB_NAME)
    except BaseException:
        print("There was an error connecting to the " + DB_NAME + "database")


def get_top_popular_articles(num):
    """ Get the top popular articles """
    query = "select title, \
            views from articles_view limit " + str(num)
    return get_query_results(query)


def get_popular_authors():
    """ Get popular authors """
    query = "select * from authors_view"
    return get_query_results(query)


def get_percent_error_dates(num):
    """ Get dates that have more than X percent request errors """
    percent = float(num)
    query = "select to_char(date,'MON DD,YYYY') as date, \
            percent_error from percent_errors_view \
            where percent_error > " + str(percent)
    return get_query_results(query)


def get_query_results(query):
    """ Query to the database to return results """
    db = connectDB()
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


def print_results(results, text):
    """ Log the results on the terminal """
    for item in results:
        print(str(item[0]) + ' - ' + str(item[1]) + ' ' + str(text))

if __name__ == "__main__":
    print("THE TOP " + str(NUMBER_OF_ARTICLES) + " POPULAR ARTICLES:")
    print_results(get_top_popular_articles(NUMBER_OF_ARTICLES), 'views')
    print("\n")
    print("POPULAR AUTHORS:")
    print_results(get_popular_authors(), 'views')
    print("\n")
    print("DAYS THAT HAVE MORE THAN " + str(float(PERCENT_ERROR))+"% ERRORS:")
    print_results(get_percent_error_dates(PERCENT_ERROR), '% errors')
