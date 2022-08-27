//   Copyright 2021 <Huawei Technologies Co., Ltd>
//
//   Licensed under the Apache License, Version 2.0 (the "License");
//   you may not use this file except in compliance with the License.
//   You may obtain a copy of the License at
//
//       http://www.apache.org/licenses/LICENSE-2.0
//
//   Unless required by applicable law or agreed to in writing, software
//   distributed under the License is distributed on an "AS IS" BASIS,
//   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
//   See the License for the specific language governing permissions and
//   limitations under the License.

#include "ops/transform/parity.hpp"

#include "ops/gates/terms_operator.hpp"
#include "ops/transform/transform_ladder_operator.hpp"

namespace mindquantum::ops::transform {
// template <typename fermion_t, typename qubit_t>
qubit_t parity(const fermion_t& ops) {
    auto n_qubits = ops.count_qubits();
    auto transf_op = qubit_t();
    for (const auto& [term, coeff] : ops.get_terms()) {
        auto transformed_term = qubit_t(terms_t{}, coeff);
        for (const auto& [idx, value] : term) {
            qlist_t x1 = {}, z1 = {}, x2 = {};
            for (auto i = idx; i < n_qubits; i++) {
                x1.push_back((i));
            }
            for (auto i = idx + 1; i < n_qubits; i++) {
                x2.push_back((i));
            }
            if (idx > 0) {
                z1.push_back(idx - 1);
            }
            transformed_term *= transform_ladder_operator(value, x1, {}, z1, x2, {idx}, {});
        }
        transf_op += transformed_term;
    }
    return transf_op;
}
}  // namespace mindquantum::ops::transform
