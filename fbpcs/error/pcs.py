#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict


class PcsError(Exception):
    pass


class InvalidParameterError(PcsError):
    pass


class ThrottlingError(PcsError):
    pass
