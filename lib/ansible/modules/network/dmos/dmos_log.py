#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Datacom (Teracom Telematica S/A) <datacom.com.br>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for dmos_log
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = """
---
module: dmos_log
version_added: '2.10'
short_description: Manages Log on DATACOM DmOS devices.
description:
  - This module provides a declarative management of System Log
    on DATACOM DmOS devices.
author:
  - Vinicius Kleinubing (@vgkleinubing) <vinicius.grubel@datacom.com.br>
  - LDS Labs (@lds-labs)
notes:
  - Tested against DmOS version 5.2.0.
options:
  config:
    description: A dict of system log messages configuration.
    type: list
    elements: dict
    suboptions:
      syslog:
        description: IP address of syslog server to be notified.
        type: list
        elements: str
      severity:
        type: str
        description:
        - Severity level of the log messages.
        choices:
        - alert
        - critical
        - emergency
        - error
        - informational
        - notice
        - warning
  state:
    description:
    - The state the configuration should be left in.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    default: merged
"""
EXAMPLES = """
### Using Merged ###

dmos_log:
  config:
    - syslog:
        - 192.168.1.1
        - 192.168.2.1
      severity: alert
  state: merged

# This configuration will result in the following commands:

# - log severity alert
# - log syslog 192.168.1.1
# - log syslog 192.168.2.1

### Using Delete ###

dmos_log:
  config:
    - syslog:
        - 192.168.1.1
        - 192.168.2.1
      severity: informational
  state: deleted

# This configuration will result in the following commands:

# - no log severity
# - no log syslog 192.168.1.1
# - no log syslog 192.168.2.1


"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.dmos.argspec.log.log import LogArgs
from ansible.module_utils.network.dmos.config.log.log import Log


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=LogArgs.argument_spec,
                           supports_check_mode=True)

    result = Log(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
