# Copyright 2021 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http: //www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Vigo."""
from mindquantum.core.gates import DepolarizingChannel, KrausChannel, BitFlipChannel
from mindquantum.core.circuit import Circuit

vigo_noise_model = {
    ('readout', 0): BitFlipChannel(0.07509999999999994).on(0),
    ('readout', 1): BitFlipChannel(0.022499999999999964).on(1),
    ('readout', 2): BitFlipChannel(0.014599999999999946).on(2),
    ('readout', 3): BitFlipChannel(0.021500000000000075).on(3),
    ('readout', 4): BitFlipChannel(0.033299999999999996).on(4),
    ('I', (0,)): Circuit(
        [
            KrausChannel(
                'TRC',
                [
                    [[0.9994059999443119, 0.0], [0.0, 0.9994059999443119]],
                    [[0.02992577119137957, 0.0], [0.0, -0.02992577119137957]],
                    [[0.017090801441453293, 0.0], [0.0, 0.0]],
                    [[0.0, 0.017090801441453293], [0.0, 0.0]],
                ],
            ).on([0]),
        ]
    ),
    ('I', (1,)): Circuit(
        [
            DepolarizingChannel(0.0007186372517291595).on([1]),
            KrausChannel(
                'TRC',
                [
                    [[0.9999724761491264, 0.0], [0.0, 0.9998132980399747]],
                    [[-0.007419362788326022, 0.0], [0.0, 0.007420544009001996]],
                    [[0.0, 0.017841092708676405], [0.0, 0.0]],
                ],
            ).on([1]),
        ]
    ),
    ('I', (2,)): Circuit(
        [
            DepolarizingChannel(0.0003408990146348545).on([2]),
            KrausChannel(
                'TRC',
                [
                    [[0.9997838649709938, 0.0], [0.0, 0.9997838649709938]],
                    [[0.009115135454344928, 0.0], [0.0, -0.009115135454344928]],
                    [[0.018685225428411324, 0.0], [0.0, 0.0]],
                    [[0.0, 0.018685225428411324], [0.0, 0.0]],
                ],
            ).on([2]),
        ]
    ),
    ('I', (3,)): Circuit(
        [
            DepolarizingChannel(0.0008527211397835188).on([3]),
            KrausChannel(
                'TRC',
                [
                    [[0.9998203597342686, 0.0], [0.0, 0.9998203597342686]],
                    [[0.007393978661671322, 0.0], [0.0, -0.007393978661671322]],
                    [[0.017452144291987638, 0.0], [0.0, 0.0]],
                    [[0.0, 0.017452144291987638], [0.0, 0.0]],
                ],
            ).on([3]),
        ]
    ),
    ('I', (4,)): Circuit(
        [
            DepolarizingChannel(0.0006197081231643642).on([4]),
            KrausChannel(
                'TRC',
                [
                    [[0.9997079306196736, 0.0], [0.0, 0.9997079306196736]],
                    [[0.013210359259065274, 0.0], [0.0, -0.013210359259065274]],
                    [[0.020237091302267404, 0.0], [0.0, 0.0]],
                    [[0.0, 0.020237091302267404], [0.0, 0.0]],
                ],
            ).on([4]),
        ]
    ),
    ('RZ', (0,)): Circuit([]),
    ('RZ', (1,)): Circuit([]),
    ('RZ', (2,)): Circuit([]),
    ('RZ', (3,)): Circuit([]),
    ('RZ', (4,)): Circuit([]),
    ('X^0.5', (0,)): Circuit(
        [
            KrausChannel(
                'TRC',
                [
                    [[0.9994059999443119, 0.0], [0.0, 0.9994059999443119]],
                    [[0.02992577119137957, 0.0], [0.0, -0.02992577119137957]],
                    [[0.017090801441453293, 0.0], [0.0, 0.0]],
                    [[0.0, 0.017090801441453293], [0.0, 0.0]],
                ],
            ).on([0]),
        ]
    ),
    ('X^0.5', (1,)): Circuit(
        [
            DepolarizingChannel(0.0007186372517291595).on([1]),
            KrausChannel(
                'TRC',
                [
                    [[0.9999724761491264, 0.0], [0.0, 0.9998132980399747]],
                    [[-0.007419362788326022, 0.0], [0.0, 0.007420544009001996]],
                    [[0.0, 0.017841092708676405], [0.0, 0.0]],
                ],
            ).on([1]),
        ]
    ),
    ('X^0.5', (2,)): Circuit(
        [
            DepolarizingChannel(0.0003408990146348545).on([2]),
            KrausChannel(
                'TRC',
                [
                    [[0.9997838649709938, 0.0], [0.0, 0.9997838649709938]],
                    [[0.009115135454344928, 0.0], [0.0, -0.009115135454344928]],
                    [[0.018685225428411324, 0.0], [0.0, 0.0]],
                    [[0.0, 0.018685225428411324], [0.0, 0.0]],
                ],
            ).on([2]),
        ]
    ),
    ('X^0.5', (3,)): Circuit(
        [
            DepolarizingChannel(0.0008527211397835188).on([3]),
            KrausChannel(
                'TRC',
                [
                    [[0.9998203597342686, 0.0], [0.0, 0.9998203597342686]],
                    [[0.007393978661671322, 0.0], [0.0, -0.007393978661671322]],
                    [[0.017452144291987638, 0.0], [0.0, 0.0]],
                    [[0.0, 0.017452144291987638], [0.0, 0.0]],
                ],
            ).on([3]),
        ]
    ),
    ('X^0.5', (4,)): Circuit(
        [
            DepolarizingChannel(0.0006197081231643642).on([4]),
            KrausChannel(
                'TRC',
                [
                    [[0.9997079306196736, 0.0], [0.0, 0.9997079306196736]],
                    [[0.013210359259065274, 0.0], [0.0, -0.013210359259065274]],
                    [[0.020237091302267404, 0.0], [0.0, 0.0]],
                    [[0.0, 0.020237091302267404], [0.0, 0.0]],
                ],
            ).on([4]),
        ]
    ),
    ('X', (0,)): Circuit(
        [
            KrausChannel(
                'TRC',
                [
                    [[0.9994059999443119, 0.0], [0.0, 0.9994059999443119]],
                    [[0.02992577119137957, 0.0], [0.0, -0.02992577119137957]],
                    [[0.017090801441453293, 0.0], [0.0, 0.0]],
                    [[0.0, 0.017090801441453293], [0.0, 0.0]],
                ],
            ).on([0]),
        ]
    ),
    ('X', (1,)): Circuit(
        [
            DepolarizingChannel(0.0007186372517291595).on([1]),
            KrausChannel(
                'TRC',
                [
                    [[0.9999724761491264, 0.0], [0.0, 0.9998132980399747]],
                    [[-0.007419362788326022, 0.0], [0.0, 0.007420544009001996]],
                    [[0.0, 0.017841092708676405], [0.0, 0.0]],
                ],
            ).on([1]),
        ]
    ),
    ('X', (2,)): Circuit(
        [
            DepolarizingChannel(0.0003408990146348545).on([2]),
            KrausChannel(
                'TRC',
                [
                    [[0.9997838649709938, 0.0], [0.0, 0.9997838649709938]],
                    [[0.009115135454344928, 0.0], [0.0, -0.009115135454344928]],
                    [[0.018685225428411324, 0.0], [0.0, 0.0]],
                    [[0.0, 0.018685225428411324], [0.0, 0.0]],
                ],
            ).on([2]),
        ]
    ),
    ('X', (3,)): Circuit(
        [
            DepolarizingChannel(0.0008527211397835188).on([3]),
            KrausChannel(
                'TRC',
                [
                    [[0.9998203597342686, 0.0], [0.0, 0.9998203597342686]],
                    [[0.007393978661671322, 0.0], [0.0, -0.007393978661671322]],
                    [[0.017452144291987638, 0.0], [0.0, 0.0]],
                    [[0.0, 0.017452144291987638], [0.0, 0.0]],
                ],
            ).on([3]),
        ]
    ),
    ('X', (4,)): Circuit(
        [
            DepolarizingChannel(0.0006197081231643642).on([4]),
            KrausChannel(
                'TRC',
                [
                    [[0.9997079306196736, 0.0], [0.0, 0.9997079306196736]],
                    [[0.013210359259065274, 0.0], [0.0, -0.013210359259065274]],
                    [[0.020237091302267404, 0.0], [0.0, 0.0]],
                    [[0.0, 0.020237091302267404], [0.0, 0.0]],
                ],
            ).on([4]),
        ]
    ),
    ('X', (4, 3)): Circuit(
        [
            DepolarizingChannel(0.00334786784330221).on([4, 3]),
            KrausChannel(
                'TRC',
                [
                    [[0.9977827924851037, 0.0], [0.0, 0.9977827924851037]],
                    [[0.036348305702920684, 0.0], [0.0, -0.036348305702920684]],
                    [[0.05575212725228879, 0.0], [0.0, 0.0]],
                    [[0.0, 0.05575212725228879], [0.0, 0.0]],
                ],
            ).on([4]),
            KrausChannel(
                'TRC',
                [
                    [[0.9986355805130691, 0.0], [0.0, 0.9986355805130691]],
                    [[0.020359637259881803, 0.0], [0.0, -0.020359637259881803]],
                    [[0.04808807028745732, 0.0], [0.0, 0.0]],
                    [[0.0, 0.04808807028745732], [0.0, 0.0]],
                ],
            ).on([3]),
        ]
    ),
    ('X', (3, 4)): Circuit(
        [
            DepolarizingChannel(0.002535030232903468).on([3, 4]),
            KrausChannel(
                'TRC',
                [
                    [[0.9984561967004905, 0.0], [0.0, 0.9984561967004905]],
                    [[0.021653816054239536, 0.0], [0.0, -0.021653816054239536]],
                    [[0.05115012727922224, 0.0], [0.0, 0.0]],
                    [[0.0, 0.05115012727922224], [0.0, 0.0]],
                ],
            ).on([3]),
            KrausChannel(
                'TRC',
                [
                    [[0.9974914862567469, 0.0], [0.0, 0.9974914862567469]],
                    [[0.03865447270898053, 0.0], [0.0, -0.03865447270898053]],
                    [[0.059300645737605275, 0.0], [0.0, 0.0]],
                    [[0.0, 0.059300645737605275], [0.0, 0.0]],
                ],
            ).on([4]),
        ]
    ),
    ('X', (1, 3)): Circuit(
        [
            DepolarizingChannel(0.005563297925566202).on([1, 3]),
            KrausChannel(
                'TRC',
                [
                    [[0.9996437337030968, 0.0], [0.0, 0.9975743428541523]],
                    [[-0.026690928573809215, 0.0], [0.0, 0.026746296841584066]],
                    [[0.0, 0.064265590204774], [0.0, 0.0]],
                ],
            ).on([1]),
            KrausChannel(
                'TRC',
                [
                    [[0.9976673083761628, 0.0], [0.0, 0.9976673083761628]],
                    [[0.026601957662364843, 0.0], [0.0, -0.026601957662364843]],
                    [[0.06286714281715261, 0.0], [0.0, 0.0]],
                    [[0.0, 0.06286714281715261], [0.0, 0.0]],
                ],
            ).on([3]),
        ]
    ),
    ('X', (3, 1)): Circuit(
        [
            DepolarizingChannel(0.005035946182170403).on([3, 1]),
            KrausChannel(
                'TRC',
                [
                    [[0.9974881065488133, 0.0], [0.0, 0.9974881065488133]],
                    [[0.027601197102600027, 0.0], [0.0, -0.027601197102600027]],
                    [[0.06523535247215849, 0.0], [0.0, 0.0]],
                    [[0.0, 0.06523535247215849], [0.0, 0.0]],
                ],
            ).on([3]),
            KrausChannel(
                'TRC',
                [
                    [[0.9996164670582242, 0.0], [0.0, 0.9973878854769179]],
                    [[-0.02769329857626741, 0.0], [0.0, 0.02775517698488992]],
                    [[0.0, 0.06668625086492613], [0.0, 0.0]],
                ],
            ).on([1]),
        ]
    ),
    ('X', (2, 1)): Circuit(
        [
            DepolarizingChannel(0.004995414241192209).on([2, 1]),
            KrausChannel(
                'TRC',
                [
                    [[0.9986176023954946, 0.0], [0.0, 0.9986176023954946]],
                    [[0.023032770867853436, 0.0], [0.0, -0.023032770867853436]],
                    [[0.04724802273135706, 0.0], [0.0, 0.0]],
                    [[0.0, 0.04724802273135706], [0.0, 0.0]],
                ],
            ).on([2]),
            KrausChannel(
                'TRC',
                [
                    [[0.9998241894677892, 0.0], [0.0, 0.9988054329235668]],
                    [[-0.018750737454261843, 0.0], [0.0, 0.018769862737185672]],
                    [[0.0, 0.04511540108647225], [0.0, 0.0]],
                ],
            ).on([1]),
        ]
    ),
    ('X', (1, 2)): Circuit(
        [
            DepolarizingChannel(0.004401953928950597).on([1, 2]),
            KrausChannel(
                'TRC',
                [
                    [[0.9997967923027294, 0.0], [0.0, 0.998618851470747]],
                    [[-0.020158722706881575, 0.0], [0.0, 0.020182501331290747]],
                    [[0.0, 0.048508309878395536], [0.0, 0.0]],
                ],
            ).on([1]),
            KrausChannel(
                'TRC',
                [
                    [[0.998401788225149, 0.0], [0.0, 0.998401788225149]],
                    [[0.02476157050509446, 0.0], [0.0, -0.02476157050509446]],
                    [[0.050800924154446654, 0.0], [0.0, 0.0]],
                    [[0.0, 0.050800924154446654], [0.0, 0.0]],
                ],
            ).on([2]),
        ]
    ),
    ('X', (1, 0)): Circuit(
        [
            KrausChannel(
                'TRC',
                [
                    [[0.9996001165585451, 0.0], [0.0, 0.9972760200661752]],
                    [[-0.02827732264807533, 0.0], [0.0, 0.028343221381282254]],
                    [[0.0, 0.06809700142224637], [0.0, 0.0]],
                ],
            ).on([1]),
            KrausChannel(
                'TRC',
                [
                    [[0.9914021030748458, 0.0], [0.0, 0.9914021030748458]],
                    [[0.11342722764973884, 0.0], [0.0, -0.11342722764973884]],
                    [[0.06523905307764044, 0.0], [0.0, 0.0]],
                    [[0.0, 0.06523905307764044], [0.0, 0.0]],
                ],
            ).on([0]),
        ]
    ),
    ('X', (0, 1)): Circuit(
        [
            KrausChannel(
                'TRC',
                [
                    [[0.9908190245352387, 0.0], [0.0, 0.9908190245352387]],
                    [[0.11717795985694515, 0.0], [0.0, -0.11717795985694515]],
                    [[0.06743134540257995, 0.0], [0.0, 0.0]],
                    [[0.0, 0.06743134540257995], [0.0, 0.0]],
                ],
            ).on([0]),
            KrausChannel(
                'TRC',
                [
                    [[0.999572881535793, 0.0], [0.0, 0.9970895927377551]],
                    [[-0.029224210823075362, 0.0], [0.0, 0.02929699480948643]],
                    [[0.0, 0.07038487159319538], [0.0, 0.0]],
                ],
            ).on([1]),
        ]
    ),
}
