#Copyright 2017 adNomus Inc. All rights reserved.

VERSION=1.0

import json
import itertools
import sys

class Authentication(object):
    def set_native_values(self, network, key, user=''):
        self.network=network
        self.key=key
        self.user=user


class AnalyticsRequest(object):
    class RequestTypes:
        #set enum type:
        @staticmethod
        def get_type():
            return str

        #enum values:
        terms='terms'
        terms_scores='terms+scores'

    def set_content(self, content):
        self.content=content

    def set_num_req_terms(num_req_terms):
        self.num_req_terms=num_req_terms

    def set_terms_request(self):
        self.request_type=self.RequestTypes.terms

    def set_terms_scores_request(self):
        self.request_type=self.RequestTypes.terms_scores


class TargetingRequest(object):
    class RequestTypes:
        #set enum type:
        @staticmethod
        def get_type():
            return str

        #enum values:
        terms='terms'
        terms_scores='terms+scores'
        user_terms='user_terms'
        user_terms_scores='user_terms+scores'

    def set_content(self, content):
        self.content=content

    def set_num_req_terms(self, num_req_terms):
        self.num_req_terms=num_req_terms

    def set_user_target_terms(self, user_terms_list):
        self.user_terms=user_terms_list

    def set_terms_request(self):
        self.request_type=self.RequestTypes.terms

    def set_terms_scores_request(self):
        self.request_type=self.RequestTypes.terms_scores

    def set_user_terms_request(self):
        self.request_type=self.RequestTypes.user_terms

    def set_user_terms_scores_request(self):
        self.request_type=self.RequestTypes.user_terms_scores


class RelevanceRequest(object):
    class RequestTypes:
        #set enum type:
        @staticmethod
        def get_type():
            return str

        #enum values:
        ordering='ordering'
        ordering_scores='ordering+scores'

    def set_reference_content(self, reference_content):
        self.reference_content=reference_content

    def set_extrinsic_contents(self,content_dict):
        self.extrinsic_contents=content_dict

    def set_ordering_request(self):
        self.request_type=self.RequestTypes.ordering

    def set_ordering_scores_request(self):
        self.request_type=self.RequestTypes.ordering_scores


class SearchRequest(object):
    class RequestTypes:
        #set enum type:
        @staticmethod
        def get_type():
            return str

        #enum values:
        search='search'
        search_scores='search+scores'

    def set_query(self, query):
        self.query=query

    def set_inventory_entries(self,entries_dict):
        self.inventory_entries=entries_dict

    def set_num_req_results(self,num_req_results):
        self.num_req_results=num_req_results

    def set_search_request(self):
        self.request_type=self.RequestTypes.search

    def set_search_scores_request(self):
        self.request_type=self.RequestTypes.search_scores



#Response classes
class ResponseStatus(object):
    class ResponseTypes:
        #set enum type:
        @staticmethod
        def get_type():
            return str

        #enum values:
        success='success'
        failure='failure'

    class FailureTypes:
        #set enum type:
        @staticmethod
        def get_type():
            return str

        #enum values:
        authentication_failure='authentication_failure'
        client_info_failure='client_info_failure'
        bad_request='bad_request'
        system_unavailable='system_unavailable'

    def is_successful(self):
        return self.response_type==self.ResponseTypes.success

    def get_failure_type(self):
        return self.failure_type


class AnalyticsResponse(object):
    def get_terms(self):
        return self.terms

    def get_scores(self):
        return self.scores


class TargetingResponse(object):
    def get_terms(self):
        return self.terms

    def get_scores(self):
        return self.scores


class RelevanceResponse(object):
    def get_ordering(self):
        return self.ordering

    def get_scores(self):
        return self.scores


class SearchResponse(object):
    def get_results(self):
        return self.results

    def get_scores(self):
        return self.scores

if sys.version_info[0]==3: #python3
    string_types=[str]
else: #python2
    string_types=[str,unicode]

class JsonObjectDictProxy(object):
    def __init__(self):
        pass

    @classmethod
    def json_to_objects(cls, json_input, *class_types):
        if json_input.__class__ in string_types:
            try:
                jdict=json.loads(json_input)
            except UnicodeDecodeError:
                jdict=json.loads(json_input.decode('utf-8', 'ignore').encode('utf-8'))
        else:
            jdict=json_input

        objs=[]

        for ct in class_types:
            data=jdict.get(ct.__name__)
            if data!=None:
                obj=ct()
                obj.__dict__.update(data)
                objs.append(obj)

        return objs

    @classmethod
    def objects_to_json(cls, *objects):
        data={}

        for obj in objects:
            data[obj.__class__.__name__]=obj.__dict__

        return json.dumps(data).replace("</", "<\\/")


try:
    import requests
except:
    print('Please install the requests package for python')
    print('command: pip install requests')
    sys.exit(-1)

class adNomusError(Exception):
    def __init__(self, cmessage=None):
        if cmessage!=None:
            self.cmessage=cmessage
    def __str__(self):
        if hasattr(self,'cmessage'):
            return 'adNomus SDK Error, '+self.cmessage

        return 'adNomus SDK Error'


def report_error(obj):
    raise adNomusError(str(obj.__dict__))

default_authentication=None
def set_default_authentication(network,
                              key,
                              user=''):
    global default_authentication
    default_authentication=Authentication()
    default_authentication.set_native_values(network,key,user)


API_BASE='https://api.adnomus.com/api/v1.0/'

def targeting_request(content,
                      num_req_terms=10,
                      user_target_terms_list=None,
                      scores=False,
                      authentication=None):
    """Content Targeting API: The user provides arbitrary content and we deliver
      a set of descriptive terms. Those terms are either generic English terms
      we generate or belong to a set of desired terms provided by the user. This
      API is ideal for ad targeting (matching to keywords, categories etc) and
      content characterization."""

    API=API_BASE+'targeting'

    global default_authentication
    if authentication==None:
        authentication=default_authentication

    request=TargetingRequest()
    request.set_content(content)
    request.set_num_req_terms(num_req_terms)

    if user_target_terms_list!=None:
        request.set_user_target_terms(user_target_terms_list)

    if scores==False:
        if user_target_terms_list==None:
            request.set_terms_request()
        else:
            request.set_user_terms_request()
    else:
        if user_target_terms_list==None:
            request.set_terms_scores_request()
        else:
            request.set_user_terms_scores_request()

    req_data=JsonObjectDictProxy.objects_to_json(authentication,request)
    #print(req_data)
    try:
        r=requests.post(API,data=req_data)
    except Exception as e:
        report_error(e)
    objs=JsonObjectDictProxy.json_to_objects(r.json(),ResponseStatus,TargetingResponse)
    if not objs[0].is_successful():
        report_error(objs[0])
    else:
        if scores==False:
            return (objs[1].get_terms(),None)
        else:
            return (objs[1].get_terms(),objs[1].get_scores())

def relevance_request(reference_content,
                      extrinsic_contents_dict,
                      scores=False,
                      authentication=None):
    """Content Relevance API: The user provides a reference content and a set of
      extrinsic (e.g. external/third party) contents. We deliver contextual
      ordering (e.g. Extrinsic content A is more relevant to the Reference
      Content than extrinsic content B). This API is ideal for content
      recommendation and service discovery."""

    API=API_BASE+'relevance'

    global default_authentication
    if authentication==None:
        authentication=default_authentication

    request=RelevanceRequest()
    request.set_reference_content(reference_content)
    request.set_extrinsic_contents(extrinsic_contents_dict)

    if scores==False:
        request.set_ordering_request()
    else:
        request.set_ordering_scores_request()

    req_data=JsonObjectDictProxy.objects_to_json(authentication,request)
    #print(req_data)
    try:
        r=requests.post(API,data=req_data)
    except Exception as e:
        report_error(e)
    objs=JsonObjectDictProxy.json_to_objects(r.json(),ResponseStatus,RelevanceResponse)
    if not objs[0].is_successful():
        report_error(objs[0])
    else:
        if scores==False:
            return (objs[1].get_ordering(),None)
        else:
            return (objs[1].get_ordering(),objs[1].get_scores())


def search_request(query,
                   inventory_entries_dict,
                   num_req_results=10,
                   scores=False,
                   authentication=None):
    """Content Search and Indexing API: The user provides an inventory description
      (e.g. marketplace/content items). We generate a contextual indexing and allow
      the user to search their inventory in natural language. This is NLP driven
      search that goes beyond naive keyword matching and typical pattern
      matching found in standard search engines."""

    API=API_BASE+'search'

    global default_authentication
    if authentication==None:
        authentication=default_authentication

    request=SearchRequest()
    request.set_query(query)
    request.set_inventory_entries(inventory_entries_dict)
    request.set_num_req_results(num_req_results)

    if scores==False:
        request.set_search_request()
    else:
        request.set_search_scores_request()

    req_data=JsonObjectDictProxy.objects_to_json(authentication,request)
    #print(req_data)
    try:
        r=requests.post(API,data=req_data)
    except Exception as e:
        report_error(e)
    objs=JsonObjectDictProxy.json_to_objects(r.json(),ResponseStatus,SearchResponse)
    if not objs[0].is_successful():
        report_error(objs[0])
    else:
        if scores==False:
            return (objs[1].get_results(),None)
        else:
            return (objs[1].get_results(),objs[1].get_scores())



