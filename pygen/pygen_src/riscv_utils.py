"""
Copyright 2020 Google LLC
Copyright 2020 PerfectVIPs Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

"""
from pygen_src.riscv_directed_instr_lib import (riscv_directed_instr_stream,
                                                riscv_int_numeric_corner_stream)


def factory(obj_of):
    # print("Factory getting called")
    # objs = {}
    objs = {
        "riscv_directed_instr_stream": riscv_directed_instr_stream,
        "riscv_int_numeric_corner_stream": riscv_int_numeric_corner_stream
    }
    return objs[obj_of]()
