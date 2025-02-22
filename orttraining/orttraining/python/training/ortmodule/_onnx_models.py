# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# _onnx_models.py

import os
from dataclasses import dataclass

import onnx
import torch


def _get_onnx_file_name(name_prefix, name, export_mode):
    suffix = "training" if export_mode == torch.onnx.TrainingMode.TRAINING else "inference"
    return f"{name_prefix}_{name}_{suffix}.onnx"


def _save_model(model: onnx.ModelProto, file_path: str):
    onnx.save(model, file_path)


@dataclass
class ONNXModels:
    """Encapsulates all ORTModule onnx models.

    1. optimized_model: For eval mode it's exported_model with concrete input shapes set if needed,
                        for training mode, it's an optimized model after the gradients graph has been built.
    In addition, ORTModule also saves two other models, to the user-provided path:
    a. the pre_grad_model which is the model before the gradients graph is built.
    b. the execution_model which is the model that is being executed by ORT.
      It has further optimizations done by the InferenceSession and is saved by the InferenceSession.
    """

    optimized_model: onnx.ModelProto | None = None

    def save_optimized_model(self, path, name_prefix, export_mode):
        # save the ortmodule optimized model
        _save_model(
            self.optimized_model, os.path.join(path, _get_onnx_file_name(name_prefix, "optimized", export_mode))
        )
