#!/usr/bin/env python3

# Testing pagination on Webex Teams API. Created mock requests module in mock_requests.py
# First we provide a precoded example of an API call to webex teams (mocked).
# A rel="next" link header will be present if another page of results is available.
# We will use the 'beforeMessage' cursor (which points to a message id), not 'before' (which is a date cursor)

from lib import mock_requests
from messenger import Messenger
import unittest
from pprint import pprint
import json


class MessageTest(unittest.TestCase):
    def setUp(self):
        self.msg = Messenger(requests=mock_requests)

    def test_get_messages(self):
        # Check if any messages exist
        messages = self.msg.get_messages().json().get('items')
        self.assertGreater(len(messages), 0)

    def test_has_next_page(self):
        # Check if there are more pages of messages available
        self.msg.get_messages()
        self.assertTrue(self.msg.has_next_page())

    def test_get_next_page(self):
        # Get the first page
        print('GET FIRST PAGE')
        messages = self.msg.get_messages().json().get('items')
        self.assertGreater(len(messages), 0)
        self.assertTrue(self.msg.has_next_page())

        # Get the next page
        print('GET NEXT PAGE')
        messages = self.msg.get_messages().json().get('items')
        self.assertGreater(len(messages), 0)


