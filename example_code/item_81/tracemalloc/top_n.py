#!/usr/bin/env PYTHONHASHSEED=1234 python3

# Copyright 2014-2019 Brett Slatkin, Pearson Education Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tracemalloc

tracemalloc.start(10)                      # Set stack depth
time1 = tracemalloc.take_snapshot()        # Before snapshot

import waste_memory

x = waste_memory.run()                     # Usage to debug
time2 = tracemalloc.take_snapshot()        # After snapshot

stats = time2.compare_to(time1, 'lineno')  # Compare snapshots
for stat in stats[:3]:
    print(stat)

# waste_memory.py:22: size=2392 KiB (+2392 KiB), count=29992 (+29992), average=82 B
# waste_memory.py:27: size=547 KiB (+547 KiB), count=10001 (+10001), average=56 B
# waste_memory.py:28: size=82.8 KiB (+82.8 KiB), count=100 (+100), average=848 B