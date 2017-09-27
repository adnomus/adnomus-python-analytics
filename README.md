# adNomus Analytics SDK for Python

## File Contents
 * Fasttrack
 * Introduction
 * Authentication
 * Content Targeting API
 * Content Relevance API
 * Content Search and Indexing API
 * Follow-up


## Fasttrack
Let's face it, documentation and instructions are boring. You can simply clone the repo and run the following command:
```bash
python example_adnomus_analytics.py
```


## Introduction
adNomus Real-Time AI technologies deliver content targeting for advertising, content discovery and contextual search purposes. Our technology enables the instant and detailed matching of web/platform content to relevant 3rd party content (e.g. ads, content recommendations, search results). Our solution delivers within 1ms while guaranteeing user and content privacy. Our targeting capabilities serve web and mobile platforms and support interactive, real-time user experiences (e.g. messaging, chatbots, search).

This repository contains our Analytics SDK for python. We provide two files:
* **adnomus_analytics_sdk.py** provides the SDK implementation.
* **example_adnomus_analytics.py** demonstrates the use of the SDK.

In order to use our sdk please import it.

```python
import adnomus_analytics_sdk as adnomus
```


## Authentication

Before performing any API call, you will have to set your authentication credentials. adNomus provides you the credentials. For the purpose of this tutorial we provide testing credentials.


```python
adnomus.set_default_authentication(network='test_network',key='fff')
```

## Content Targeting API
### Functionality
The user provides arbitrary content and we deliver
a set of descriptive terms. Those terms are either generic English terms
we generate or belong to a set of desired terms provided by the user. This
API is ideal for ad targeting (matching to keywords, categories etc) and
content characterization.

### Example Use 1 -- (generic targeting terms, no scores)
```python
content='I am thinking to buy a new sports car, maybe a bmw or corvette.'
result=adnomus.targeting_request(content,num_req_terms=5)
print('Resulted Top Terms:')
print(result)
```

### Example Use 2 -- (generic targeting terms, with scores)
```python
content='I am thinking to buy a new sports car, maybe a bmw or corvette.'
result=adnomus.targeting_request(content,num_req_terms=5,scores=True)
print('Resulted Top Terms:')
print(result)
```

### Example Use 3 -- (user defined targeting terms, no scores)
```python
content='I am thinking to buy a new sports car, maybe a bmw or corvette.'
user_target_terms=['car','bmw','race','speed',
                   'auto-motive','dealership',
                   'art','physics','camping']
result=adnomus.targeting_request(content=content,
                                 user_target_terms_list=user_target_terms,
                                 num_req_terms=8)
print('Resulted Top Terms:')
print(result)
```

### Example Use 4 -- (user defined targeting terms, with scores)
```python
content='I am thinking to buy a new sports car, maybe a bmw or corvette.'
user_target_terms=['car','bmw','race','speed',
                   'auto-motive','dealership',
                   'art','physics','camping']
result=adnomus.targeting_request(content=content,
                                 user_target_terms_list=user_target_terms,
                                 num_req_terms=8,
                                 scores=True)
print('Resulted Top Terms:')
print(result)
```

### Interesting Use Cases
**Contextual Ad Targeting:** Use the API to retrieve terms(keywords) that
characterize your content. You can rely on us to provide generic terms
or you can explicitly define the terms you are interested into and we
do the targeting.

**Content Characterization**: Retrieve terms that describe your content,
again you have the option to specify the set of terms we target.

**Content Classification:** Use this API to classify your content to
categories of your choice. Here, you can specify any category you require
in plain English e.g. "cars", "Italian food", "computer security news". A
category can be a single word or a phrase.


## Content Relevance API
### Functionality
The user provides a reference content and a set of
extrinsic (e.g. external/third party) contents. We deliver contextual
ordering (e.g. Extrinsic content A is more relevant to the Reference
Content than extrinsic content B). This API is ideal for content
recommendation and service discovery.

### Example Use 1 -- (relevance ordering, no scores)
```python
content0='I like travelling to the mountains and doing camping.'
content1='New BMW and AUDI cars are amazing cars but American models like Camaro set the competition bar high.'
content2='I am thinking of buying a car or a motorbike for racing.'
content3='Pop music releases of the last years are pretty mediocre productions.'

content_dict={}
content_dict['c0']=content0
content_dict['c1']=content1
content_dict['c2']=content2
content_dict['c3']=content3

reference_content='I am thinking to buy a new sports car, maybe a bmw or corvette.'
result=adnomus.relevance_request(reference_content=reference_content,
                                 extrinsic_contents_dict=content_dict)
print('Relevance Ordering (High to Low):')
print(result)
```

### Example Use 2 -- (relevance ordering, with scores)
```python
content0='I like travelling to the mountains and doing camping.'
content1='New BMW and AUDI cars are amazing cars but American models like Camaro set the competition bar high.'
content2='I am thinking of buying a car or a motorbike for racing.'
content3='Pop music releases of the last years are pretty mediocre productions.'

content_dict={}
content_dict['c0']=content0
content_dict['c1']=content1
content_dict['c2']=content2
content_dict['c3']=content3

reference_content='I am thinking to buy a new sports car, maybe a bmw or corvette.'
result=adnomus.relevance_request(reference_content=reference_content,
                                 extrinsic_contents_dict=content_dict,
                                 scores=True)
print('Relevance Ordering (High to Low):')
print(result)
```

### Interesting Use Cases
**Content Recommendation:** There are multiple use cases (e.g. social
media) where you need to recommend relevant content to your user (show
her something relevant to what she is reading or writing). This API
allows you to do that.

**Service Recommendation:** In many scenarios, you need to suggest your
user some actions such as i) listen to a song, ii) buy a concert ticket,
iii) take care of some task. The best way to do this is by naturally
connecting those actions to the content the user reads or writes.
Please, consider the following approach: The reference content here
is your user's content and the extrinsic contents the actions you want
to recommend, described in plain English e.g. "listen to the new Metallica
song", "get a ticket to Mexico for vacation".


## Content Search and Indexing API
### Functionality
Content Search and Indexing API: The user provides an inventory description
(e.g. marketplace/content items). We generate a contextual indexing and allow
the user to search their inventory in natural language. This is NLP driven
search that goes beyond naive keyword matching and typical pattern
matching found in standard search engines.


### Example Use 1 -- (search, no scores)
```python
inventory0='$100 Giftcard, buy your favorite clothing online.'
inventory1='This car tuner accessory gives your car additional velocity and smooth suspension.'
inventory2='New phone device allows you to surf the internet with voice commands.'
inventory3='The ultimate travelling guide for Africa, Europe and Asia.'
inventory4='AUDI and BMW lease voucher, save 5k for your next car.'

inventory_dict={}
inventory_dict['entry0']=inventory0
inventory_dict['entry1']=inventory1
inventory_dict['entry2']=inventory2
inventory_dict['entry3']=inventory3
inventory_dict['entry4']=inventory4

query='I am looking for car related products'
result=adnomus.search_request(query=query,
                              inventory_entries_dict=inventory_dict,
                              num_req_results=3)
print('Top Results: ')
print(result)
```

### Example Use 2 -- (search, with scores)
```python
inventory0='$100 Giftcard, buy your favorite clothing online.'
inventory1='This car tuner accessory gives your car additional velocity and smooth suspension.'
inventory2='New phone device allows you to surf the internet with voice commands.'
inventory3='The ultimate travelling guide for Africa, Europe and Asia.'
inventory4='AUDI and BMW lease voucher, save 5k for your next car.'

inventory_dict={}
inventory_dict['entry0']=inventory0
inventory_dict['entry1']=inventory1
inventory_dict['entry2']=inventory2
inventory_dict['entry3']=inventory3
inventory_dict['entry4']=inventory4

query='I am looking for car related products'
result=adnomus.search_request(query=query,
                              inventory_entries_dict=inventory_dict,
                              num_req_results=3,
                              scores=True)
print('Top Results: ')
print(result)
```

### Interesting Use Cases
**Precise Content Search:** You can use this API to perform contextual
search on your content inventory (e.g. social media content). Our
search technology goes beyond keyword and pattern matching and delivers
high quality results.

**Marketplace Inventory Indexing and Search:** Modern marketplaces
have hundreds of millions of product entries. Traditional search
technologies fail in scaling and precision. This API fixes this.

**Contextual Indexing and Search of Ad Inventories:** Use this API
to contextually organize and search your advert inventory. We provide
you a solution for effective ad targeting and indexing.


## Follow-up
### Register with us
Register with us to receive your credentials and start using our service.

### In-house Solutions
Your service needs may require the transfer of terabytes
of data in daily base and you may require the caching of your API requests. We can
install, configure and support our services and technologies as part of your in-house
infrastructure or cloud.

### Contact information
Visit our [website](http://www.adnomus.com).
Email us at: contact@adnomus.com

