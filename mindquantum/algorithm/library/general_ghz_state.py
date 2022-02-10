# -*- coding: utf-8 -*-
# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""General GHZ State."""

from mindquantum.core.gates import X, H
from mindquantum.core.circuit import Circuit


def general_ghz_state(qubits):
    """
    General GHZ State.

    Args:
        qubits (list[int]): Qubits you want to apply general GHZ state.

    Examples:
        >>> from mindquantum.algorithm.library import general_ghz_state
        >>> print(general_ghz_state(range(3)).get_qs(ket=True))
        √2/2¦000⟩
        √2/2¦111⟩
    """
    circuit = Circuit()

    for i in range(len(qubits)):
        if i == 0:
            circuit += H.on(qubits[i])
        else:
            circuit += X.on(qubits[i], qubits[i - 1])

    return circuit