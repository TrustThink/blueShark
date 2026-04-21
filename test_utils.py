import unittest
from unittest import mock
from Utils import read_capture_file, extract_known_protocols

class TestReadCaptureFile(unittest.TestCase):

    @mock.patch("Utils.pyshark.FileCapture")
    @mock.patch("Utils.asyncio.set_event_loop")
    @mock.patch("Utils.asyncio.new_event_loop")
    def test_read_capture_file(self, mock_new_event_loop, mock_set_event_loop, mock_file_capture):

        pass


class TestExtractKnownProtocols(unittest.TestCase):
    @mock.patch('Utils.read_capture_file')
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

        # fake capture object
        mock_capture = mock.MagicMock()
        mock_capture.__iter__.return_value = iter([packet1, packet2, packet3, packet4, packet5])


        # read_capture_file() returns fake capture
        mock_read_capture.return_value = mock_capture

        # Act
        result = extract_known_protocols("fake.pcap")

        # Assert
        self.assertEqual(set(result["protocols"]), {"UDP", "TCP", "HTTP"}) 
        self.assertEqual(result["count"], 3) 