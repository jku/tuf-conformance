import pytest

__version__ = "3.0.0"

# register pytest asserts before the imports happen in conftest.py
pytest.register_assert_rewrite("tuf_conformance._internal.client_runner")
