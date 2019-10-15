import io
from unittest import mock
import pytest

import settings
from app import library_app


class TestLibraryApp:

    @pytest.fixture
    def test_parse_document_list(self):
        book_info_list = open("../Step3Data.txt").readlines()
        library_app.parse_document_list(book_info_list)
        assert len(settings.LIBRARY) > 0

    def test_parse_user_input_book(self, test_parse_document_list):
        key = "Norris2013"
        with mock.patch('sys.stdout', new=io.StringIO()) as console_print:
            library_app.parse_user_input(key)
            expected_string = "Harper Collins Publishers"
            assert expected_string in console_print.getvalue().strip()

    def test_parse_user_input_journal(self, test_parse_document_list):
        key = "Inclezan2015"
        with mock.patch('sys.stdout', new=io.StringIO()) as console_print:
            library_app.parse_user_input(key)
            expected_string = "An Application of ASP to the Field of Second Language Acquisition"
            assert expected_string in console_print.getvalue().strip()

    def test_parse_user_input_conference(self, test_parse_document_list):
        key = "Abernethy2000"
        with mock.patch('sys.stdout', new=io.StringIO()) as console_print:
            library_app.parse_user_input(key)
            expected_string = "March 6-8, 2000"
            assert expected_string in console_print.getvalue().strip()

    def test_parse_user_input_invalid_key(self, test_parse_document_list):
        key = "FRANKOCEAN"
        with mock.patch('sys.stdout', new=io.StringIO()) as console_print:
            library_app.parse_user_input(key)
            expected_string = "Document Not found! Please use a valid key"
            assert expected_string in console_print.getvalue().strip()
