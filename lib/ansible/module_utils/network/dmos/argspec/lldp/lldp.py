#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
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
The arg spec for the dmos_lldp module
"""


class LldpArgs(object):  # pylint: disable=R0903
    """The arg spec for the dmos_lldp module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {'config': {'elements': 'dict',
            'options': {'interface': {'elements': 'dict',
                                      'options': {'admin_status': {'choices': ['disabled',
                                                                               'rx-only',
                                                                               'tx-and-rx',
                                                                               'tx-only'],
                                                                   'type': 'str'},
                                                  'name': {'required': True,
                                                           'type': 'str'},
                                                  'notification': {'type': 'bool'},
                                                  'tlv_port_description': {'type': 'bool'},
                                                  'tlv_system_capabilities': {'type': 'bool'},
                                                  'tlv_system_description': {'type': 'bool'},
                                                  'tlv_system_name': {'type': 'bool'}},
                                      'type': 'list'},
                        'msg_fast_tx': {'type': 'int'},
                        'msg_tx_hold_multi': {'type': 'int'},
                        'msg_tx_interval': {'type': 'int'},
                        'notification_interval': {'type': 'int'},
                        'reinit_delay': {'type': 'int'},
                        'tx_credit_max': {'type': 'int'},
                        'tx_fast_init': {'type': 'int'}},
            'type': 'list'},
 'state': {'choices': ['merged', 'replaced', 'overridden', 'deleted'],
           'default': 'merged',
           'type': 'str'}}  # pylint: disable=C0301
