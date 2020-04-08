.. _dmos_platform_options:

***************************************
DmOS Platform Options
***************************************

Datacom DmOS Ansible modules only supports CLI connections today. This page offers details on how to use ``network_cli`` on DmOS in Ansible.

.. contents:: Topics

Connections Available
================================================================================

.. table::
    :class: documentation-table

    ====================  ==========================================
    ..                    CLI
    ====================  ==========================================
    Protocol              SSH

    Credentials           uses SSH keys / SSH-agent if present

                          accepts ``-u myuser -k`` if using password

    Indirect Access       via a bastion (jump host)

    Connection Settings   ``ansible_connection: network_cli``

    |enable_mode|         not supported by DmOS

    Returned Data Format  ``stdout[0].``
    ====================  ==========================================

.. |enable_mode| replace:: Enable Mode |br| (Privilege Escalation)


Using CLI in Ansible
====================

Example CLI ``group_vars/ios.yml``
----------------------------------

.. code-block:: yaml

   ansible_connection: network_cli
   ansible_network_os: dmos
   ansible_user: myuser
   ansible_password: !vault...
   ansible_become: yes
   ansible_become_method: enable
   ansible_become_password: !vault...
   ansible_ssh_common_args: '-o ProxyCommand="ssh -W %h:%p -q bastion01"'


- If you are using SSH keys (including an ssh-agent) you can remove the ``ansible_password`` configuration.
- If you are accessing your host directly (not through a bastion/jump host) you can remove the ``ansible_ssh_common_args`` configuration.
- If you are accessing your host through a bastion/jump host, you cannot include your SSH password in the ``ProxyCommand`` directive. To prevent secrets from leaking out (for example in ``ps`` output), SSH does not support providing passwords via environment variables.

Example CLI Task
----------------

.. code-block:: yaml

   - name: Show current switch config)
     dmos_command:
       commands: show running-config
     register: running_config
     when: ansible_network_os == 'dmos'

   - name: Example of VLAN configuration
     dmos_vlan:
       config:
         - vlan_id: 2019
           interface:
             - name: gigabit-ethernet-1/1/1
               tagged: true
           name: null
         - vlan_id: 2020
           name: dmos_vlan
           interface:
             - name: gigabit-ethernet-1/1/2
               tagged: false
         - vlan_id: 2021
       state: merged


.. include:: shared_snippets/SSH_warning.txt

.. seealso::

       :ref:`timeout_options`
