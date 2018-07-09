from .windows import WindowManager, WindowRegistry, WindowLike
from .sessions import Session
from .test_session import TestClient, test_config

import unittest


class WindowRegistryTests(unittest.TestCase):

    def test_can_get_window_state(self):
        windows = WindowRegistry(None, None, None, None)
        test_window = WindowLike()
        window_state = windows.lookup(test_window)
        self.assertIsNotNone(window_state)


class WindowManagerTests(unittest.TestCase):

    def test_has_no_sessions(self):
        state = WindowManager(None, None, None, None, None)
        self.assertIsNone(state.get_session('asdf'))

    def test_can_add_session(self):
        state = WindowManager(None, None, None, None, None)
        self.assertIsNone(state.get_session('asdf'))
        state.add_session('asdf', Session(test_config, "", TestClient()))
        self.assertIsNotNone(state.get_session('asdf'))

    # def test_can_(self):
    #     state = WindowState()
    #     state.request_session