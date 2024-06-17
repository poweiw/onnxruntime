// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

#include "common.h"
#include <cstdio>

onnxruntime::ProviderHost* g_host{};

onnxruntime::ProviderHost* Provider_GetHost() {
  printf("Getting host! host == nullptr = %d\n", g_host == nullptr);
  return g_host;
}

void Provider_SetHost(onnxruntime::ProviderHost* p) {
  printf("Host set to %p\n", p);
  g_host = p;
}
