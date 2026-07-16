# test_agentforgex.py
"""
Tests for AgentForgeX module.
"""

import unittest
from agentforgex import AgentForgeX

class TestAgentForgeX(unittest.TestCase):
    """Test cases for AgentForgeX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgentForgeX()
        self.assertIsInstance(instance, AgentForgeX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgentForgeX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
