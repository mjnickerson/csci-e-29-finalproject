#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `lui_gui` package."""

import os
import random
import pathlib
from unittest import TestCase
import mock
from luigi.mock import MockTarget
from luigi import LocalTarget
from luigi.contrib.opener import OpenerTarget, NoOpenerError


class LuigiTestExternalTasks(TestCase):
    """ Test Luigi function for external Mock Connections
    Code Source Referenced: https://github.com/spotify/luigi/blob/master/test/contrib/opener_test.py
    """
    def setUp(self):
        MockTarget.fs.clear()

        self.local_file = '/tmp/{}/xyz/test.txt'.format(
            random.randint(0, 999999999)
        )

        if LocalTarget.fs.exists(self.local_file):
            LocalTarget.fs.remove(self.local_file)

    def test_invalid_target(self):
        '''Verify invalid types raises NoOpenerError
        '''
        self.assertRaises(NoOpenerError, OpenerTarget, 'foo://bar.txt')

    @mock.patch('luigi.file.LocalTarget.__init__')
    @mock.patch('luigi.file.LocalTarget.__del__')
    def test_local_tmp_target(self, lt_del_patch, lt_init_patch):
        '''Verify local target url with query string
        '''
        lt_init_patch.return_value = None
        lt_del_patch.return_value = None

        local_file = "file://{}?is_tmp".format(self.local_file)
        OpenerTarget(local_file)
        lt_init_patch.assert_called_with(self.local_file, is_tmp=True)

    @mock.patch('luigi.contrib.s3.S3Target.__init__')
    def test_s3_parse(self, s3_init_patch):
        '''Verify basic s3 target url
        '''
        s3_init_patch.return_value = None

        local_file = "s3://zefr/foo/bar.txt"
        OpenerTarget(local_file)
        s3_init_patch.assert_called_with("s3://zefr/foo/bar.txt")

    @mock.patch('luigi.contrib.s3.S3Target.__init__')
    def test_s3_parse_param(self, s3_init_patch):
        '''Verify s3 target url with params
        '''
        s3_init_patch.return_value = None

        local_file = "s3://zefr/foo/bar.txt?foo=hello&bar=true"
        OpenerTarget(local_file)
        s3_init_patch.assert_called_with("s3://zefr/foo/bar.txt",
                                         foo='hello',
                                         bar='true')

    def tearDown(self):
        if LocalTarget.fs.exists(self.local_file):
            LocalTarget.fs.remove(self.local_file)


class LuigiLocalTargetTest(TestCase):
    """ Test Luigi function processing of Local Targets
    Code Source Referenced: https://github.com/spotify/luigi/blob/master/test/local_target_test.py
    """
    PATH_PREFIX = '/tmp/test.txt'

    def setUp(self):
        self.path = self.PATH_PREFIX + '-' + str(self.id())
        self.copy = self.PATH_PREFIX + '-copy-' + str(self.id())
        if os.path.exists(self.path):
            os.remove(self.path)
        if os.path.exists(self.copy):
            os.remove(self.copy)

    def create_target(self, format=None):
        return LocalTarget(self.path, format=format)

    def test_exists(self):
        t = self.create_target()
        p = t.open('w')
        self.assertEqual(t.exists(), os.path.exists(self.path))
        p.close()
        self.assertEqual(t.exists(), os.path.exists(self.path))

    def test_copy(self):
        t = LocalTarget(self.path)
        f = t.open('w')
        test_data = 'test'
        f.write(test_data)
        f.close()
        self.assertTrue(os.path.exists(self.path))
        self.assertFalse(os.path.exists(self.copy))
        t.copy(self.copy)
        self.assertTrue(os.path.exists(self.path))
        self.assertTrue(os.path.exists(self.copy))
        self.assertEqual(t.open('r').read(), LocalTarget(self.copy).open('r').read())

    def test_move(self):
        t = LocalTarget(self.path)
        f = t.open('w')
        test_data = 'test'
        f.write(test_data)
        f.close()
        self.assertTrue(os.path.exists(self.path))
        self.assertFalse(os.path.exists(self.copy))
        t.move(self.copy)
        self.assertFalse(os.path.exists(self.path))
        self.assertTrue(os.path.exists(self.copy))

    def assertCleanUp(self, tmp_path=''):
        self.assertFalse(os.path.exists(tmp_path))

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)
        if os.path.exists(self.copy):
            os.remove(self.copy)


class no_leaked_secrets(TestCase):
    """
    Test cases to verify no secret variables were released
    """
    def test_verify_no_dotenv(self):
        """
        Verify no dotenv was leaked in repo
        """
        assert not pathlib.Path(os.getcwd() + "/.env").exists()