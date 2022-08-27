//   Copyright 2020 <Huawei Technologies Co., Ltd>
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

#ifndef JORDAN_WIGNER_TRANSFORM_HPP
#define JORDAN_WIGNER_TRANSFORM_HPP

#include "ops/gates/fermion_operator_parameter_resolver.hpp"
#include "ops/gates/qubit_operator_parameter_resolver.hpp"

namespace mindquantum::ops::transform {
using qubit_t = QubitOperatorPR;
using fermion_t = FermionOperatorPR;

//! Jordan Wigner transform that transform a Fermion operator to qubit operator.
// TODO(xusheng): Why cannot use template, otherwise undefined symbol error occur.
// template <typename fermion_t, typename qubit_t>
MQ_NODISCARD qubit_t jordan_wigner(const fermion_t& ops);
}  // namespace mindquantum::ops::transform

#endif
