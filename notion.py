import os, requests, json
from pprint import pprint
from notion_client import Client

with open("key.json", "r") as file:
    data = json.load(file)
api_key = data["NOTION_API_KEY"]
page_id = data["PAGE_ID"]

notion = Client(auth=api_key)
page = notion.pages.retrieve(page_id)

pprint(page.properties())