import os
import subprocess

from .. import utils

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2018, Helium Edu'
__version__ = '1.1.9'

child_processes = []


class StartServersAction:
    def __init__(self):
        self.name = "start-servers"
        self.help = "Launch known project servers to run locally"

    def setup(self, subparsers):
        parser = subparsers.add_parser(self.name, help=self.help)
        parser.set_defaults(action=self)

    def run(self, args):
        config = utils.get_config()
        projects_dir = utils.get_projects_dir()

        # Identify dev servers (if present) and launch them
        processes = []
        for project in config["projects"]:
            runserver_bin = os.path.join(projects_dir, project, config["serverBinFilename"])

            if os.path.exists(runserver_bin):
                processes.append(subprocess.Popen(runserver_bin))

        if len(processes) > 0:
            processes[-1].wait()
