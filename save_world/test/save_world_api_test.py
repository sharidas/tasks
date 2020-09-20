"""
This test file does unit test against the public
apis created for the flask app.
"""

import pytest
import unittest
import json
from wsgi import app
from savedata.model import UserSave

class SaveWorldAPITest(unittest.TestCase):
    """
    Testing the save world api
    """
    @pytest.fixture(autouse=True)
    def initapp(self):
        """
        Initialize the app and delete the db after the tests
        """
        yield True

        if hasattr(app, 'db'):
            app.db.session.query(UserSave).delete()
            app.db.session.commit()
    

    def test_create_save_world_data(self):
        """
        Test creating save world data
        """
        client = app.test_client()

        response = client.post(
                        "/save/world/",
                        data = json.dumps(
                        dict(
                            dtime = "2020-06-10 09:10:00",
                            howsaved = "Saved from Tsunami",
                            thanks_to_people = "Max\nThomas"
                            )
                        ),
                        content_type = 'application/json',
                    )
        
        assert response.status_code == 201
        assert response.get_data().decode('utf-8') == 'Data saved'

    def test_update_save_world(self):
        """
        Test the save world data by updating the thankful members
        """
        client = app.test_client()

        response = client.post(
                        "/save/world/",
                        data = json.dumps(
                        dict(
                            dtime = "2020-06-10 09:10:00",
                            howsaved = "Saved from Tsunami",
                            thanks_to_people = "Max\nThomas"
                            )
                        ),
                        content_type = 'application/json',
                    )
        
        assert response.status_code == 201
        assert response.get_data().decode('utf-8') == 'Data saved'

        response = client.put(
                        "/save/world/",
                        data = json.dumps(
                            dict(
                                howsaved = "Saved from Tsunami",
                                thanks_to_people = "Max\nThomas\Tom"
                            )
                        ),
                        content_type = 'application/json',
                    )
        
        assert response.status_code == 201
        assert response.get_data().decode('utf-8') == '["Data updated"]\n'