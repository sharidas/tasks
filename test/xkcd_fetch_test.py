"""
This module tests the xkcd fetch problem
"""
import os
import shutil
import unittest
import xkcd_fetch

class XkcdTest(unittest.TestCase):
    """
    This class has the unit tests for our xkcd problem
    """

    def tearDown(self):
        """
        Clean up the images folder created for testing
        """
        shutil.rmtree("images")

    def test_xkcd_fetch(self):
        """
        Test for single download
        """
        xkcd_fetch.get_xkcd()

        xkcd_images = os.listdir("images")
        assert len(xkcd_images) == 1
        assert xkcd_images[0].startswith('xkcd')

    def test_xkcd_double_fetch(self):
        """
        Test for twice download from xkcd
        """
        # first
        xkcd_fetch.get_xkcd()

        # second
        xkcd_fetch.get_xkcd()

        xkcd_images = os.listdir("images")

        assert len(xkcd_images) == 2

        assert xkcd_images[0].startswith('xkcd')
        assert xkcd_images[1].startswith('xkcd')

    def test_xkcd_fetch_old_image_deleted(self):
        """
        Test to make sure our images folder has only 2 images
        """
        # first
        xkcd_fetch.get_xkcd()

        # second
        xkcd_fetch.get_xkcd()

        # third
        xkcd_fetch.get_xkcd()

        xkcd_images2 = os.listdir("images")

        assert len(xkcd_images2) == 2

        assert xkcd_images2[0].startswith('xkcd')
        assert xkcd_images2[1].startswith('xkcd')
