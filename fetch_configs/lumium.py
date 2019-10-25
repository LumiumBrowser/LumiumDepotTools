# Copyright (c) 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
# Modified copy of fetch_configs/chromium.py

import ast
import sys

import config_util  # pylint: disable=import-error


# This class doesn't need an __init__ method, so we disable the warning
# pylint: disable=no-init
class Lumium(config_util.Config):
  """Basic Config class for Lumium (mostly a copy from the chromium template)."""

  @staticmethod
  def fetch_spec(props):
    url = 'https://github.com/LumiumBrowser/chromium.git'
    solution = { 'name'   :'src',
                 'url'    : url,
                 'managed'   : False,
                 'custom_deps': {},
                 'custom_vars': {},
    }
    if props.get('webkit_revision', '') == 'ToT':
      solution['custom_vars']['webkit_revision'] = ''
    if ast.literal_eval(props.get('internal', 'False')):
      solution['custom_vars']['checkout_src_internal'] = True

      if not ast.literal_eval(props.get('flash', 'False')):
        solution['custom_deps'].update({
            'src/third_party/adobe/flash/binaries/ppapi/linux': None,
            'src/third_party/adobe/flash/binaries/ppapi/linux_x64': None,
            'src/third_party/adobe/flash/binaries/ppapi/mac_64': None,
            'src/third_party/adobe/flash/binaries/ppapi/win': None,
            'src/third_party/adobe/flash/binaries/ppapi/win_x64': None,
            'src/third_party/adobe/flash/symbols/ppapi/linux': None,
            'src/third_party/adobe/flash/symbols/ppapi/linux_x64': None,
            'src/third_party/adobe/flash/symbols/ppapi/mac_64': None,
            'src/third_party/adobe/flash/symbols/ppapi/win': None,
            'src/third_party/adobe/flash/symbols/ppapi/win_x64': None,
        })
    spec = {
      'solutions': [solution],
    }
    if props.get('target_os'):
      spec['target_os'] = props['target_os'].split(',')
    if props.get('target_os_only'):
      spec['target_os_only'] = props['target_os_only']

    return {
      'type': 'gclient_git',
      'gclient_git_spec': spec,
    }

  @staticmethod
  def expected_root(_props):
    return 'src'


def main(argv=None):
  return Lumium().handle_args(argv)


if __name__ == '__main__':
  sys.exit(main(sys.argv))
