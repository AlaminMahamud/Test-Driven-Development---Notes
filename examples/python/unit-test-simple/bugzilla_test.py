from .bugzilla import MyBugzilla
import unittest
import requests_mock
from unittest import mock
import requests


class TestBugZilla(unittest.TestCase):
    def test_bug_id(self):
        zilla = MyBugzilla(
            'tarek@mozilla.com',
            server='http://example.com'
        )
        link = zilla.bug_link(23)
        self.assertEqual(link, 'http://example.com/show_bug.cgi?id=23')

    @requests_mock.mock()
    def test_get_new_bugs(self, mocker):
        # mocking the request call and send back two args
        bugs = [
            {'id': 11223344},
            {'id': 44778899},
        ]
        mocker.get(requests_mock.ANY, json={'bugs': bugs})
        zilla = MyBugzilla('tarek@mozilla.com', server='http://example.com')
        bugs = list(zilla.get_new_bugs())
        self.assertEqual(
            bugs[0]['link'],
            'http://example.com/show_bug.cgi?id=11223344'
        )

    @mock.patch.object(requests.Session, 'get', side_effect=ConnectionError('No Network'))
    def test_network_error(self, mocked):
        # faking a connection error in request if the web is down
        zilla = MyBugzilla('tarek2mozilla.com', server='http://example.com')
        bugs = list(zilla.get_new_bugs())
        self.assertEqual(len(bugs), 0)


if __name__ == "__main__":
    unittest.main()
