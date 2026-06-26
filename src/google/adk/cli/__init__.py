# Copyright 2026 Google LLC
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

from typing import Any

from .cli_tools_click import main as _main


def main(args: Any = None, **kwargs: Any) -> Any:
  """Package entry point that disables Windows glob expansion for all CLI commands."""

  kwargs.setdefault("windows_expand_args", False)
  return _main.main(args=args, **kwargs)
