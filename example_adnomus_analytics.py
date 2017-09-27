#Copyright 2017 adNomus Inc. All rights reserved.

import adnomus_analytics_sdk as adnomus
from collections import OrderedDict
import os
import sys

if sys.version_info[0]==3: #python3/python2 compatibility
    raw_input=input

#http://code.activestate.com/recipes/577058/
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

adnomus.set_default_authentication(network='test_network',key='fff')

os.system('clear')
#targeting api test
print('===============---- Content Targeting API ----==============')
print(
"""Content Targeting API: The user provides arbitrary content and we deliver
a set of descriptive terms. Those terms are either generic English terms
we generate or belong to a set of desired terms provided by the user. This
API is ideal for ad targeting (matching to keywords, categories etc) and
content characterization.\n""")

content='I am thinking to buy a new sports car, maybe a bmw or corvette.'

print('Targeting Request Use Case 1 (no scores)...')
print('Input Content: '+content)
result=adnomus.targeting_request(content,num_req_terms=5)
print('Resulted Top Terms:')
print(result[0])
print('--------------\n')

print('Targeting Request Use Case 2 (with scores)...')
print('Input Content: '+content)
result=adnomus.targeting_request(content,num_req_terms=5,scores=True)
print('Resulted Top Terms and Scores:')
print(str(list(zip(result[0],result[1]))))
print('--------------\n')

user_target_terms=['car','bmw','race','speed',
                   'auto-motive','dealership',
                   'art','physics','camping']

print('Targeting Request Use Case 3 (USER DEFINED targeting terms + no scores)...')
print('Input Content: '+content)
print('User\'s terms to target: '+str(user_target_terms))
result=adnomus.targeting_request(content=content,
                                 user_target_terms_list=user_target_terms,
                                 num_req_terms=8)
print('Resulted Top Terms:')
print(result[0])
print('--------------\n')

print('Targeting Request Use Case 4 (USER DEFINED targeting terms + with scores)...')
print('Input Content: '+content)
print('User\'s terms to target: '+str(user_target_terms))
result=adnomus.targeting_request(content=content,
                                 user_target_terms_list=user_target_terms,
                                 num_req_terms=8,
                                 scores=True)
print('Resulted Top Terms and Scores:')
print(str(list(zip(result[0],result[1]))))
print('--------------\n')

proceed=query_yes_no('Do you want to check the next API Demo (Content Relevance)?')
if proceed==False:
    sys.exit(0)
os.system('clear')

#relevance api test
print('===============---- Content Relevance API ----===============')
print(
"""Content Relevance API: The user provides a reference content and a set of
extrinsic (e.g. external/third party) contents. We deliver contextual
ordering (e.g. Extrinsic content A is more relevant to the Reference
Content than extrinsic content B). This API is ideal for content
recommendation and service discovery.\n""")

content0='I like travelling to the mountains and doing camping.'
content1='New BMW and AUDI cars are amazing cars but American models like Camaro set the competition bar high.'
content2='I am thinking of buying a car or a motorbike for racing.'
content3='Pop music releases of the last years are pretty mediocre productions.'
content_dict=OrderedDict()
content_dict['c0']=content0
content_dict['c1']=content1
content_dict['c2']=content2
content_dict['c3']=content3

reference_content='I am thinking to buy a new sports car, maybe a bmw or corvette.'

print('Relevance Request Use Case 1 (no scores)...')
print('Reference Content: '+reference_content)
print('Extrinsic Contents: ')
for i in content_dict:
    print(i+' : '+content_dict[i])
result=adnomus.relevance_request(reference_content=reference_content,
                            	 extrinsic_contents_dict=content_dict)
print('Relevance Ordering (High to Low):')
print(result[0])
print('--------------\n')


print('Relevance Request Use Case 2 (with scores)...')
print('Reference Content: '+reference_content)
print('Extrinsic Contents: ')
for i in content_dict:
    print(i+' : '+content_dict[i])
result=adnomus.relevance_request(reference_content=reference_content,
                            	 extrinsic_contents_dict=content_dict,
                            	 scores=True)
print('Relevance Ordering and Scores (High to Low):')
print(str(list(zip(result[0],result[1]))))
print('--------------\n')

proceed=query_yes_no('Do you want to check the next API Demo (Content Search and Indexing)?')
if proceed==False:
    sys.exit(0)
os.system('clear')

#search api test
print('===============---- Content Search and Indexing API ----===============')
print("""Content Search and Indexing API: The user provides an inventory description
(e.g. marketplace/content items). We generate a contextual indexing and allow
the user to search their inventory in natural language. This is NLP driven
search that goes beyond naive keyword matching and typical pattern
matching found in standard search engines.\n""")

inventory0='$100 Giftcard, buy your favorite clothing online.'
inventory1='This car tuner accessory gives your car additional velocity and smooth suspension.'
inventory2='New phone device allows you to surf the internet with voice commands.'
inventory3='The ultimate travelling guide for Africa, Europe and Asia.'
inventory4='AUDI and BMW lease voucher, save 5k for your next car.'
inventory_dict=OrderedDict()
inventory_dict['entry0']=inventory0
inventory_dict['entry1']=inventory1
inventory_dict['entry2']=inventory2
inventory_dict['entry3']=inventory3
inventory_dict['entry4']=inventory4

query='I am looking for car related products'

print('Search Request Use Case 1 (no scores)...')
print('Search Query: '+query)
print('Inventory Entries: ')
for i in inventory_dict:
    print(i+' : '+inventory_dict[i])

result=adnomus.search_request(query=query,
                              inventory_entries_dict=inventory_dict,
			      num_req_results=3)
print('Top Results: ')
print(result[0])
print('--------------\n')

print('Search Request Use Case 2 (with scores)...')
print('Search Query: '+query)
print('Inventory Entries: ')
for i in inventory_dict:
    print(i+' : '+inventory_dict[i])


result=adnomus.search_request(query=query,
                              inventory_entries_dict=inventory_dict,
                              num_req_results=3,
			      scores=True)
print('Top Results and Scores:')
print(str(list(zip(result[0],result[1]))))
print('--------------\n')

print('=====================---- More Info ----======================')
print("""In-house solutions: Your service needs may require the transfer of terabytes
of data in daily base and you may require the caching of your API requests. We can
install, configure and support our services and technologies as part of your in-house
infrastructure or cloud.""")

print('\n')
print('Contact us at: contact@adnomus.com')


