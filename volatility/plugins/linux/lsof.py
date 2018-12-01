"""A module containing a collection of plugins that produce data
typically found in Linux's /proc file system.
"""
import logging

from volatility.framework import renderers
from volatility.framework.automagic import linux
from volatility.framework.interfaces import plugins
from volatility.framework.objects import utility
from volatility.plugins.linux import pslist

vollog = logging.getLogger(__name__)


class Lsof(plugins.PluginInterface):
    """Lists all memory maps for all processes"""

    @classmethod
    def get_requirements(cls):
        # Since we're calling the plugin, make sure we have the plugin's requirements
        return pslist.PsList.get_requirements() + []

    def _generator(self, tasks):
        for task in tasks:
            name = utility.array_to_string(task.comm)
            pid = int(task.pid)

            for fd_num, _, full_path in linux.LinuxUtilities.files_descriptors_for_process(self.config, self.context,
                                                                                           task):
                yield (0, (pid, name, fd_num, full_path))

    def run(self):
        linux.LinuxUtilities.aslr_mask_symbol_table(self.config, self.context)

        filter = pslist.PsList.create_filter([self.config.get('pid', None)])

        plugin = pslist.PsList.list_tasks

        return renderers.TreeGrid(
            [("PID", int),
             ("Process", str),
             ("FD", int),
             ("Path", str)],
            self._generator(plugin(self.context,
                                   self.config['primary'],
                                   self.config['vmlinux'],
                                   filter = filter)))