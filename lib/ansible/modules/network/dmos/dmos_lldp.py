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
The module file for dmos_lldp
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
module: dmos_lldp
version_added: '2.10'
short_description: Manages Link Layer Discovery Protocol on DATACOM DmOS devices.
description:
  - This module provides a declarative management of Link Layer Discovery Protocol
    on DATACOM DmOS devices.
author:
  - Vinicius Kleinubing (@vgkleinubing) <vinicius.grubel@datacom.com.br>
  - LDS Labs (@lds-labs)
notes:
  - Tested against DmOS version 5.2.0.
options:
  config:
    description: A list of Link Layer Discovery Protocol configurations.
    type: list
    elements: dict
    suboptions:
      interface:
        description: Link Layer Discovery Protocol Interface Configuration.
        type: list
        elements: dict
        suboptions:
          name:
            description: Link Layer Discovery Protocol Interface name.
            type: str
            required: true
          admin_status:
            description: Administrative LLDP port status.
            type: str
            choices:
              - disabled
              - rx-only
              - tx-and-rx
              - tx-only
          notification:
            description: Enable LLDP notifications for this interface.
            type: bool
          tlv_port_description:
            description: Port Description TLV.
            type: bool
          tlv_system_capabilities:
            description: System Capabilities TLV.
            type: bool
          tlv_system_description:
            description: System Description TLV.
            type: bool
          tlv_system_name:
            description: System Name TLV.
            type: bool
      msg_fast_tx:
        description: <1-3600> Time interval at which LLDP frames are transmitted during fast transmission period.
        type: int
      msg_tx_hold_multi:
        description: <2-10> TTL value expressed as a multiple of message-tx-interval.
        type: int
      msg_tx_interval:
        description: <5-32768> Time interval at which LLDP frames are transmitted.
        type: int
      notification_interval:
        description: <5-3600> Time interval between transmissions of LLDP notifications.
        type: int
      reinit_delay:
        description: <1-10> Amount of delay until a re-initialization attempt.
        type: int
      tx_credit_max:
        description: <1-100> Maximum number of consecutive LLDP frames that can be transmitted in a second.
        type: int
      tx_fast_init:
        description: <1-8> Number of LLDP frames sent in fast transmission period.
        type: int
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

dmos_lldp:
  config:
    - interface:
      - name: gigabit-ethernet-1/1/1
        admin_status: rx-only
        notification: true
        tlv_port_description: false
        tlv_system_capabilities: true
        tlv_system_description: false
        tlv_system_name: true

      - name: gigabit-ethernet-1/1/2
        admin_status: rx-only
        notification: true
        tlv_port_description: false
        tlv_system_capabilities: true
        tlv_system_description: false
        tlv_system_name: true
      msg_fast_tx: 2020
      msg_tx_hold_multi: 3
      msg_tx_interval: 2020
      notification_interval: 2020
      reinit_delay: 3
      tx_credit_max: 33
      tx_fast_init: 3
  state: merged

# This configuration will result in the following commands:

# - lldp interface gigabit-ethernet-1/1/1 admin-status rx-only
# - lldp interface gigabit-ethernet-1/1/1 notification
# - no lldp interface gigabit-ethernet-1/1/1 tlvs-tx port-description
# - lldp interface gigabit-ethernet-1/1/1 tlvs-tx system-capabilities
# - no lldp interface gigabit-ethernet-1/1/1 tlvs-tx system-description
# - lldp interface gigabit-ethernet-1/1/1 tlvs-tx system-name
# - lldp interface gigabit-ethernet-1/1/2 admin-status rx-only
# - lldp interface gigabit-ethernet-1/1/2 notification
# - no lldp interface gigabit-ethernet-1/1/2 tlvs-tx port-description
# - lldp interface gigabit-ethernet-1/1/2 tlvs-tx system-capabilities
# - no lldp interface gigabit-ethernet-1/1/2 tlvs-tx system-description
# - lldp interface gigabit-ethernet-1/1/2 tlvs-tx system-name
# - lldp message-fast-tx 2020
# - lldp message-tx-hold-multiplier 3
# - lldp message-tx-interval 2020
# - lldp notification-interval 2020
# - lldp reinit-delay 3
# - lldp tx-credit-max  33
# - lldp tx-fast-init 3

### Using Delete ###

dmos_lldp:
  config:
    - interface:
      - name: gigabit-ethernet-1/1/1
        tlv_system_capabilities: true
        tlv_system_name: true
      - name: gigabit-ethernet-1/1/2
      tx_credit_max: 33
      tx_fast_init: 3
  state: deleted

# This configuration will result in the following commands:

# - no lldp interface gigabit-ethernet-1/1/1 tlvs-tx system-capabilities
# - no lldp interface gigabit-ethernet-1/1/1 tlvs-tx system-name
# - no lldp interface gigabit-ethernet-1/1/2
# - no lldp tx-credit-max
# - no lldp tx-fast-init


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
from ansible.module_utils.network.dmos.argspec.lldp.lldp import LldpArgs
from ansible.module_utils.network.dmos.config.lldp.lldp import Lldp


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=LldpArgs.argument_spec,
                           supports_check_mode=True)

    result = Lldp(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()
