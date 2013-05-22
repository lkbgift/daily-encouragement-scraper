###############################################################################
# START HERE: Tutorial 3: More advanced scraping. Shows how to follow 'next' 
# links from page to page: use functions, so you can call the same code 
# repeatedly. SCROLL TO THE BOTTOM TO SEE THE START OF THE SCRAPER.
###############################################################################

import scraperwiki
import urlparse
import lxml.html

# scrape_table function: gets passed an individual page to scrape
def scrape_table(root):
    rows = root.cssselect("div#body_right")  # selects all <tr> blocks within <table class="data">
    for row in rows:
        # Set up our data record - we'll need it later
        record = {}
        table_cells = row.cssselect("p")
        if table_cells: 
            record['Quote'] = table_cells[2].text
            # Print out the data we've gathered
            print record, '------------'
            # Finally, save the record to the datastore - 'Artist' is our unique key
            scraperwiki.datastore.save(["Quote"], record)
        
# Scrape for quote and go to next date



def scrape_metal():
    html = scraperwiki.scrape(url)
    print html
    root = lxml.html.fromstring(html)
    scrape_table(root)
    dated = '?m=' + str(month) + '&d=' + str(day) 
    recent_url = urlparse.urljoin(base_url, dated)
    scrape_and_get_next_date(recent_url)

def day_progression():
    for day in range (1,31):
        print "day " + str(day)
        scrape_metal

def scrape_and_get_next_date(url):
    for month in range (1,13):
        day_progression()
        print "month " + str(month)
        


# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then 
# call a function to scrape the first page in the series.
# ---------------------------------------------------------------------------
base_url = 'http://www.sgi-usa.org/encouragement/index.php'
date = '?m=1&d=1'
starting_url = urlparse.urljoin(base_url, date)
scrape_and_get_next_date(starting_url)
