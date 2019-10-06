# Python_developer_technical_task

## Github_crawler

## Project overview

This is my implementation of Github crawler.

It searches for repository urls (NOT urls of code, commits, issues,...) based on search words in input file.

Input file needs to be in JSON format as shown in input_short.txt and input_long.txt. Field TYPE must allways be 'Repository', field 'keywords' can be anything and 'proxies' must be valid.

Result is printed JSON format in file that can be set in function main() in crawler.py (default name is output.txt).

Crawler can search for some extra repository data like owner of repository and language details if it is enabled.

## Running

If you want to run crawler.py you must first install some python library packages:
- requests
- beautifulsoup4
- lxml

Input file needs to be in same folder as crawler.py!

Now you can run crawler.py in:
- python IDE
- command line: python crawler.py

## Enabeling extra data search

You can enable extra data search by uncommenting two cone lines in crawler.py in function get_urls(). They are located between two boxes with instructions.

## Testing

Before testing you will need to install 'validator_collection' package.

If you want to run test, test.py needs to be in same folder as crawler.py.

Now you can run test.py in:
- python IDE
- command line: python test.py

