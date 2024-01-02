import os
import unittest
import coverage
from flask_migrate import Migrate

from app.server import app, db

COV = coverage.coverage(
    branch=True,
    include="app/*",
    omit=[
        "app/tests/*",
        "app/server/config.py",
        "app/server/__init__.py"
    ]
)

COV.start()

migrate = Migrate(app, db, command="migrate")


def runtests():
    tests = unittest.TestLoader().discover("app/tests", pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    return result


@app.cli.command
def test():
    """Run unit tests"""
    res = runtests()
    if res.wasSuccessful():
        return 1
    return 0


@app.cli.command
def cov():
    """Run unit tests with coverage"""
    res = runtests()
    if res.wasSuccessful():
        COV.stop()
        COV.save()
        print("Coverage successful.")
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, "tmp/coverage")
        COV.html_report(directory=covdir)
        print("Coverage HTML report generated.")
        COV.stop()


@app.cli.command
def create_db():
    """Create DB tables"""
    db.create_all()


@app.cli.command
def drop_db():
    """Drops DB tables"""
    db.drop_all()


if __name__ == "__main__":
    app.run()
