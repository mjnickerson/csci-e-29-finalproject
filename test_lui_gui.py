#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `lui_gui` package."""

import os
from unittest import TestCase


class FakeFileFailure(IOError):
    """
    Fake Error, that File Failed to Write
    """
    pass


class FileExistsError(IOError):
    """
    Fake Error, that file already exists
    """
    pass


class sample_tests(TestCase):
    """
    Example Unit Test Cases to be modified
    """
    def test_will_pass(self):
        some_number = 0
        assert some_number == 0
        assert not some_number == 1