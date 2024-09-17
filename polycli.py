
import os
import datetime
import warnings
from gnews import GNews

global max_results_parm, period_parm, start_date_parm, end_date_parm, google_news

google_news = GNews()
google_news.max_results = 5
google_news.period = '1d'
google_news.country = 'United States'
google_news.language = 'english'

def print_defaults():

    print("\ndefault values set:\n")
    print(f"max results: {google_news.max_results}")
    print(f"period: {google_news.period}")
    if isinstance(google_news.start_date, tuple):
        print(f"start date: {'-'.join(map(str, google_news.start_date))}")
    else:
        print(f"start date: {google_news.start_date}")
        
    if isinstance(google_news.end_date, tuple):
        print(f"end date: {'-'.join(map(str, google_news.end_date))}")
    else:
        print(f"end date: {google_news.end_date}")

    print(f"country: {google_news.country}")
    print(f"language: {google_news.language}")

def set_defaults():
    
    print("\nset default values:\n")
    google_news.max_results = int(input("Enter max results (default=5): ") or 5)

    print("\nSelect date option:")
    print("1. Specify period (e.g., 1d, 7d, 1m)")
    print("2. Specify start and end dates")
    
    date_option = input("Enter choice (1/2, default=1): ") or '1'
    
    if date_option == '1':
        google_news.period = input("Enter period (default=1d, e.g., 1d, 7d, 1m): ") or '1d'
        google_news.start_date = None
        google_news.end_date = None
    elif date_option == '2':
        google_news.period = None
        
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        
        start_date_input = input(f"Enter start date (default={yesterday.strftime('%Y-%m-%d')}, YYYY-MM-DD): ")
        google_news.start_date = tuple(map(int, start_date_input.split('-'))) if start_date_input else (yesterday.year, yesterday.month, yesterday.day)
        
        end_date_input = input(f"Enter end date (default={today.strftime('%Y-%m-%d')}, YYYY-MM-DD): ")
        google_news.end_date = tuple(map(int, end_date_input.split('-'))) if end_date_input else (today.year, today.month, today.day)
    else:
        print("Invalid choice. Using default period.")
        google_news.period = '1d'
        google_news.start_date = None
        google_news.end_date = None


    available_countries = GNews().countries
    available_languages = GNews().languages

    print("\navailable countries:")
    for country in available_countries:
        print(country)

    country_input = input(f"Enter country (default=United States): ")
    google_news.country = country_input if country_input else 'United States'


    print("\nAvailable languages:")
    for language in available_languages:
        print(language)

    language_input = input(f"Enter language (default=english): ").lower()
    google_news.language = language_input if language_input else 'english'   
    
    print_defaults()


def erase_defaults():
    
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)    

    google_news.max_results = 5
    google_news.period = '1d'
    google_news.start_date = None
    google_news.end_date = None
    google_news.country = 'United States'
    google_news.language = 'english'
    
    print("\ndefault values erased. Reset to original values.")

    print_defaults()

def print_news(news):
    for i in range(len(news)):
        print(f"{i+1}. {news[i]['title']}")
        print(f"{news[i]['published date']}")
        print(f"{news[i]['url']}")
        print()

def filter_by_site():

    while True:
        try:
            print("\n============================")
            print("*** site filter sub-menu ***")
            print("============================\n")

            # Define a dictionary mapping user inputs to site names
            sites = {
                '1': 'wsj.com',
                '2': 'apnews.com',
                '3': 'reuters.com',
                '4': 'bloomberg.com',
                '5': 'cnbc.com',
                '6': 'foxnews.com',
                '7': 'cnn.com',
                '8': 'baltimoresun.com'
            }

            print("Enter:\n")
            print('\n'.join([f"'{key}' {value}" for key, value in sites.items()]))
            print("'9' to enter a different site")
            print("'q' to return to main menu:\n")

            action = input()

            if action.lower() == 'q':
                # Return to main menu
                break
            elif action == '9':
                custom_domain = input("Enter a custom domain (e.g., nbcnews.com): ")
                if not custom_domain.startswith('http'):
                    custom_domain = f"www.{custom_domain}"
                print("\nnews by site:\n")
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", category=UserWarning)
                    news = google_news.get_news_by_site(custom_domain)
                    print_news(news)
            elif action in sites:
                # Code to filter by site
                print("\nnews by site:\n")
                site = sites[action]
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", category=UserWarning)                
                    news = google_news.get_news_by_site(site)
                    print_news(news)
            else:
                print("Invalid input. Please try again.")

        except KeyboardInterrupt:
            print("\nreturning to main menu...")
            break

def get_news():

    global google_news
    
    while True:
        try:

            print("\n============================")
            print("*** google news sub-menu ***")
            print("============================\n")

            action = input("""Enter:
            '1' to get latest news headlines
            '2' to get news by site
            '3' to get news by keyword
            '4' to set default values
            '5' to erase default values
            '6' to print default values
            'q' to return to main menu:
            
            """)

            if action == '1':
                # Code to get news headlines
                print("\nnews headlines:\n")
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore", category=UserWarning)
                    news = google_news.get_top_news()
                    print_news(news)
            
            elif action == '2':
                # Code to get news by site
                print("\nnews by site:")
                filter_by_site()
            elif action == '3':
                # Code to get news by keyword

                keyword = input("\nenter keyword: ")

                print("\nnews by keyword:\n")
                news = google_news.get_news(keyword)
                print_news(news)

            elif action == '4':
                set_defaults()
            elif action == '5':
                erase_defaults()
            elif action == '6':
                print_defaults()
            elif action == 'q':
                break
            else:
                print("invalid input. Please try again.")

        except KeyboardInterrupt:
            print("\nreturning to main menu...")
            break



def main():

    while True:
        try:

            print("\x1b[5 q")

            print("\n==================================")
            print("*** Welcome to the polyCLI app ***")
            print("==================================\n")

            action = input("""Enter:
            '1' to get google news
            'q' to exit:
            
            """)
            if action == '1':
                get_news()
            elif action == 'q':
                break
            else:
                print("invalid input. Please try again.")

        except KeyboardInterrupt:
            print("\nexiting polyCLI...")
            break

if __name__ == "__main__":
    main()