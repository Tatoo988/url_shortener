#!/usr/bin/env python
import json
import unittest

from app import create_app, db
from app.models import ShortenURL
from config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ShortenUrlModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.test_client = self.app.test_client()
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Authorization': 'Bearer <redacted>'
        }
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_shorten_url_creation(self):
        request_data = {
            "url": "www.instagram.com",
            "shortcode": "instag"
        }
        result = self.test_client.post('api/shorten', headers=self.headers,
                                       data=json.dumps(request_data))
        self.assertEqual(result.status_code, 201)

    def test_shorten_url_creation_without_shortcode(self):
        request_data = {
            "url": "www.google.com",
        }
        result = self.test_client.post('api/shorten', headers=self.headers,
                                       data=json.dumps(request_data))
        self.assertEqual(result.status_code, 201)

    def test_shorten_url_creation_existing_shortcode(self):
        shortcode = 'testshort'
        shorten = ShortenURL(url='www.facebook.com', shortcode=shortcode)
        db.session.add(shorten)
        db.session.commit()
        request_data = {
            "url": "www.google.com",
            "shortcode": shortcode
        }
        result = self.test_client.post('api/shorten', headers=self.headers,
                                       data=json.dumps(request_data))
        self.assertEqual(result.status_code, 409)

    def test_shorten_url_creation_existing_url(self):
        shorten = ShortenURL(url='www.facebook.com', shortcode='testshort')
        db.session.add(shorten)
        db.session.commit()
        request_data = {
            "url": "www.facebook.com",
            "shortcode": "blabla"
        }
        result = self.test_client.post('api/shorten', headers=self.headers,
                                       data=json.dumps(request_data))
        self.assertEqual(result.status_code, 409)

    def test_shorten_url_get_success(self):
        shortcode = 'testshort'
        shorten = ShortenURL(url='www.facebook.com', shortcode=shortcode)
        db.session.add(shorten)
        db.session.commit()

        result = self.test_client.get('api/{}'.format(shortcode))
        self.assertEqual(result.status_code, 302)

    def test_shorten_url_stats_success(self):
        shortcode = 'testshort'
        shorten = ShortenURL(url='www.facebook.com', shortcode=shortcode)
        db.session.add(shorten)
        db.session.commit()

        result = self.test_client.get('api/{}/stats'.format(shortcode))
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main(verbosity=2)
