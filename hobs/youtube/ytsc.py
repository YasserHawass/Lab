#using youtube api, sacrap youtube chanells, and count views for each video
#Example
# dict = {
#     {
#         "name" = "",
#         "views" = ""
#     },
#     {
#         "name" ="",
#         "views" = ""
#     },
# }
# Sample Python code for user authorization
# AIzaSyB0yRpbejtxpdw4mXSeienE5qe4zWSwK9w
# 997735525119-hisvd85mn4hbjhedai7skjnftnikuqpr.apps.googleusercontent.com
# dS9X4UgcEYXMyID6qYcatVlI



# instead use this V
# https://www.googleapis.com/youtube/v3/search?key=AIzaSyCJWMH6DZ41lYxV4VPiF_Esu-fx_JGCKfU&channelId=UCudKvbd6gvbm5UCYRk5tZKA&part=snippet,id&order=viewcount
# -*- coding: utf-8 -*-

import os

import google.oauth2.credentials

import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def print_response(response):
  print(response)

# Build a resource based on a list of properties given as key-value pairs.
# Leave properties with empty values out of the inserted resource.
def build_resource(properties):
  resource = {}
  for p in properties:
    # Given a key like "snippet.title", split into "snippet" and "title", where
    # "snippet" will be an object and "title" will be a property in that object.
    prop_array = p.split('.')
    ref = resource
    for pa in range(0, len(prop_array)):
      is_array = False
      key = prop_array[pa]

      # For properties that have array values, convert a name like
      # "snippet.tags[]" to snippet.tags, and set a flag to handle
      # the value as an array.
      if key[-2:] == '[]':
        key = key[0:len(key)-2:]
        is_array = True

      if pa == (len(prop_array) - 1):
        # Leave properties without values out of inserted resource.
        if properties[p]:
          if is_array:
            ref[key] = properties[p].split(',')
          else:
            ref[key] = properties[p]
      elif key not in ref:
        # For example, the property is "snippet.title", but the resource does
        # not yet have a "snippet" object. Create the snippet object here.
        # Setting "ref = ref[key]" means that in the next time through the
        # "for pa in range ..." loop, we will be setting a property in the
        # resource's "snippet" object.
        ref[key] = {}
        ref = ref[key]
      else:
        # For example, the property is "snippet.description", and the resource
        # already has a "snippet" object.
        ref = ref[key]
  return resource

def search_list_by_keyword(client, **kwargs):
  # See full sample for function
  response = client.search().list(**kwargs).execute()

  return print_response(response['items'])


if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  client = get_authenticated_service()

  search_list_by_keyword(client,
    part='snippet',
    channelId='UCudKvbd6gvbm5UCYRk5tZKA',
    order='viewCount')






























#https://stackoverflow.com/questions/18953499/youtube-api-to-fetch-all-videos-on-a-channel
#https://www.googleapis.com/youtube/v3/search?key=AIzaSyCJWMH6DZ41lYxV4VPiF_Esu-fx_JGCKfU&channelId=UCudKvbd6gvbm5UCYRk5tZKA&part=snippet,id&order=viewcount
# {
#  "error": {
#   "errors": [
#    {
#     "domain": "global",
#     "reason": "invalidParameter",
#     "message": "Invalid string value: 'views'. Allowed values: [date, rating, relevance, title, videocount, viewcount]",
#     "locationType": "parameter",
#     "location": "order"
#    }
#   ],
#   "code": 400,
#   "message": "Invalid string value: 'views'. Allowed values: [date, rating, relevance, title, videocount, viewcount]"
#  }
# }




# ok



# import os
# import google.oauth2.credentials
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from google_auth_oauthlib.flow import InstalledAppFlow
#
# # The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# # the OAuth 2.0 information for this application, including its client_id and
# # client_secret.
# CLIENT_SECRETS_FILE = "client_secret.json"
#
# # This OAuth 2.0 access scope allows for full read/write access to the
# # authenticated user's account and requires requests to use an SSL connection.
# SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
# API_SERVICE_NAME = 'youtube'
# API_VERSION = 'v3'
#
# def get_authenticated_service():
#   flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
#   credentials = flow.run_console()
#   return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
#
# def channels_list_by_username(service, **kwargs):
#   results = service.videos().list(
#     **kwargs
#   ).execute()
#
#   print(dict(results))
#   # print('This channel\'s ID is %s. Its title is %s, and it has %s views.' %
#   #      (results['items'][0]['id'],
#   #       results['items'][0]['snippet']['title'],
#   #       results['items'][0]['statistics']['viewCount']))
#
# if __name__ == '__main__':
#   # When running locally, disable OAuthlib's HTTPs verification. When
#   # running in production *do not* leave this option enabled.
#   os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
#   service = get_authenticated_service()
#   videos_list_by_id(service,
#       part='snippet,contentDetails,statistics',
#       id='UCudKvbd6gvbm5UCYRk5tZKA ')
#https://developers.google.com/youtube/v3/docs/channels/list
