# TFD Preplan

A project to combine data sources and provide responders with property details.

## Project Goals
1. Discover php calls to county assessor site
2. Build single page app with address input
3. ...


## Tulsa County Assessor Site

The Tulsa County assessor makes property information available a this [property search](
http://www.assessor.tulsacounty.org/assessor-property-search.php)link.



## Property Scraper

```
pip install -r requirements.txt
python
>> from property_scraper import get_property_data
>> resp = get_property_data('36', 'E', 'Cameron', 'St')
>> resp.content
```
