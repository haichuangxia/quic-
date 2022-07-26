#!/usr/bin/python
# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Certificate chain where the root certificate contains a basic constraints
extension that indicates it is NOT a CA."""

import sys
sys.path += ['..']

import common

# Self-signed root certificate with non-CA basic constraints.
root = common.create_self_signed_root_certificate('Root')
root.get_extensions().set_property('basicConstraints', 'critical,CA:false')

# Intermediate certificate.
intermediate = common.create_intermediate_certificate('Intermediate', root)

# Target certificate.
target = common.create_end_entity_certificate('Target', intermediate)

chain = [target, intermediate, root]
common.write_chain(__doc__, chain, 'chain.pem')
