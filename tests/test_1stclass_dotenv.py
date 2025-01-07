import os
import os.path
import unittest

from dotenv_dev import Dotenv


class Test1stclassDotenv(unittest.TestCase):
    def test_init(self):
        print("test __init__")
        dotenv = Dotenv()
        dotenv.load()
        self.assertEqual(os.environ.get("envfile"), ".env", ".env file is missing")

    def test_setDotenv(self):
        print("test setDotenv()")
        dotenv = Dotenv()
        dotenv.load(os.path.join(os.path.dirname(__file__), ".env.specified1"))
        self.assertEqual(
            os.environ.get("envfile"),
            ".env.specified1",
            ".env.specified1 env file is missing",
        )

    def test_setDotenv_by_constructor(self):
        print("test setDotenv_by_constructor")
        dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env.specified2"))
        dotenv.load()
        self.assertEqual(
            os.environ.get("envfile"),
            ".env.specified2",
            ".env.specified2 env file is missing",
        )

    def test_setDotenv_by_constructor2(self):
        print("test setDotenv_by_constructor2")
        dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env.specified3"))
        dotenv.load()
        self.assertEqual(
            os.environ.get("envfile"),
            ".env.specified#3",
            ".env.specified3 env file is missing",
        )


if __name__ == "__main__":
    unittest.main()
