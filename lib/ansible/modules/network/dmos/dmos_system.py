#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2020 Datacom (Teracom Telematica S/A) <datacom.com.br>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for dmos_system
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
module: dmos_system
version_added: '2.10'
short_description: Configure system on DATACOM DmOS devices.
description: Configure system of dmos devices.
author:
  - Vinicius Kleinubing (@vgkleinubing) <vinicius.grubel@datacom.com.br>
  - LDS Labs (@lds-labs)
notes:
  - Tested against DmOS version 5.2.0.
options:
  hour:
    description: DmOS system hour.
    type: int
    required: true
  minute:
    description: DmOS system minute.
    type: int
    required: true
  second:
    description: DmOS system second.
    type: int
    required: false
  year:
    description: DmOS system year.
    type: int
    required: true
  month:
    description: DmOS system month.
    type: int
    required: true
  day:
    description: DmOS system day.
    type: int
    required: true
"""

EXAMPLES = """
- name: Set DmOS device system time
  dmos_system:
    hour: 19
    minute: 18
    second: 47
    year: 2018
    month: 10
    day: 18
"""

RETURN = """
changed:
  description: If configuration resulted in any change.
  type: str
  returned: always
  sample: True or False
command:
  description: Executed commands.
  type: str
  returned: always
  sample: set system clock 19:18:47 20181018
stdout:
  description: Raw output of command.
  type: str
  returned: always
  sample: ["Clock is set."]
stdout_lines:
  description: Raw output of command splitted in lines.
  type: list
  returned: always
  sample: ["Clock is set."]
"""

import json

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.network.common.utils import to_lines
from ansible.module_utils.network.dmos.dmos import run_commands
from ansible.module_utils.network.dmos.dmos import dmos_argument_spec


def parse_command(module, warnings):
    command = """set system clock {0:02d}:{1:02d}:{2:02d} """.format(
        module.params['hour'], module.params['minute'], module.params['second'])

    command += """{0:04d}{1:02d}{2:02d}""".format(
        module.params['year'], module.params['month'], module.params['day'])

    return command


def main():
    """ main entry point for module execution
    """
    argument_spec = dict(
        hour=dict(required=True, type='int', choices=range(0, 24)),
        minute=dict(required=True, type='int', choices=range(0, 61)),
        second=dict(type='int', choices=range(0, 61), default=0),
        year=dict(required=True, type='int', choices=range(1970, 2099)),
        month=dict(required=True, type='int', choices=range(1, 13)),
        day=dict(required=True, type='int', choices=range(1, 32))
    )

    argument_spec.update(dmos_argument_spec)

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    result = {'changed': True}

    warnings = list()

    command = parse_command(module, warnings)
    result['command'] = command

    responses = run_commands(module, [command])

    result['warnings'] = warnings
    result.update({
        'stdout': responses,
        'stdout_lines': list(to_lines(responses)),
    })

    module.exit_json(**result)


if __name__ == '__main__':
    main()
