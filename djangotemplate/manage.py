#!/usr/bin/env python
# coding:utf-8

import os
import sys
import django.conf

if __name__ == "__main__":
    os.environ["DJANGO_SETTINGS_MODULE"] = "core.settings"

    from django.core.management import execute_from_command_line

    # プロジェクトのプロパティで渡される"Settings Module"の値は無視
    argv = sys.argv
    if "--settings" in argv:
        idx = argv.index("--settings")
        del argv[idx:(idx+2)]

    execute_from_command_line(argv)
