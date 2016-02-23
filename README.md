# Unicode Scraper

A scrappy scraper for `fileformat.info`. Will grab all characters listed from [http://www.fileformat.info/info/charset/UTF-8/list.htm](http://www.fileformat.info/info/charset/UTF-8/list.htm) and generated a huge JSON file with all the characters that were found inside.

The JSON file contains these fields:

`
{"encoded": "\u095c", "name": "DEVANAGARI LETTER DDDHA (U+095C)", "numeric": "e0a59c"},
{"encoded": "\u095d", "name": "DEVANAGARI LETTER RHA (U+095D)", "numeric": "e0a59d"},
{"encoded": "\u095e", "name": "DEVANAGARI LETTER FA (U+095E)", "numeric": "e0a59e"},
`

- `encoded` is the unicode chars as is (they are escaped in UTF-32 inside JSON)
 - `name` is the name of the character
 - `numeric` is its UTF-8 hexadecimal value.

# Run the scraper

- install scrape


`scrapy crawl fileformat --output=utf-8.json -t json`