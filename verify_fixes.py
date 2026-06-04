import sys
from unittest.mock import MagicMock
sys.modules['gi'] = MagicMock()
sys.modules['gi.repository'] = MagicMock()
sys.modules['gi.repository.GObject'] = MagicMock()
sys.modules['gi.repository.Gio'] = MagicMock()
sys.modules['dbus'] = MagicMock()
sys.modules['cairo'] = MagicMock()

sys.path.insert(0, 'src')
import os
import shutil
import tempfile
import unittest
from unittest.mock import patch, MagicMock
from sugar4 import util
from sugar4.bundle.bundle import Bundle
import shutil
import subprocess

class TestFixes(unittest.TestCase):
    def test_util_mutable_default(self):
        # Test that modifying one instance doesn't affect another
        lru1 = util.LRU(10)
        lru1['a'] = 1
        
        lru2 = util.LRU(10)
        self.assertNotIn('a', lru2)
        
        # Verify default is None in signature (well, strictly speaking we check behavior)
        # Inspecting the default value using inspect module would be more direct but behavior is key
        import inspect
        sig = inspect.signature(util.LRU.__init__)
        self.assertIsNone(sig.parameters['pairs'].default)

    @patch('subprocess.call')
    def test_bundle_subprocess_call(self, mock_subprocess_call):
        # Create a dummy bundle class to test _unzip (mocking everything else)
        # but Bundle is abstract, we need to mock it carefully or sublcass
        
        # Better: check the source file content for subprocess.call usage
        with open(r'c:\Users\acer\sugar-toolkit-gtk4\src\sugar4\bundle\bundle.py', 'r') as f:
            content = f.read()
        self.assertIn('subprocess.call', content)
        self.assertNotIn('os.spawnlp', content)

    def test_datastore_mktemp_replaced(self):
         with open(r'c:\Users\acer\sugar-toolkit-gtk4\src\sugar4\datastore\datastore.py', 'r') as f:
            content = f.read()
            self.assertIn('tempfile.mkstemp', content)
            self.assertNotIn('tempfile.mktemp', content)
            self.assertIn('os.close(fd)', content)

if __name__ == '__main__':
    unittest.main()
