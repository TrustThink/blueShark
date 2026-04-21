#import pyshark
import collections
import asyncio
#import mock
import unittest

class read_capture_file(filepath):

    @read_capture_file.patch('capture')
    def read_capture_file_test(self, capture_mocked):
        args, kwargs = capture_mocked.call_args
        args = capture_mocked.call_args.args  # alternatively 
        self.assertEqual(args, ['metadata_example', 'action_example'])



import unittest
from unittest import mock

class TestExtractKnownProtocols(unittest.TestCase):

    def test_no_duplicates_in_protocols(self, mock_read_capture):

        # Create fake packets
        packet1 = mock.Mock()
        packet1.highest_layer = "UDP"

        packet2 = mock.Mock()
        packet2.highest_layer = "UDP"  # duplicate

        packet3 = mock.Mock()
        packet3.highest_layer = "TCP"

        packet4 = mock.Mock()
        packet4.highest_layer = "HTTP"

        packet5 = mock.Mock()
        packet5.highest_layer = "TCP"  # duplicate

        # Mock capture (acts like iterable)
        mock_read_capture.return_value = [
            packet1, packet2, packet3, packet4, packet5
        ]

        # Act
        result = extractknownprotocols("fake.pcap")

        # Assert
        self.assertEqual(result, ["UDP", "TCP", "HTTP"])  