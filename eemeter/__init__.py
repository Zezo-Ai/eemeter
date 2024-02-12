#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

   Copyright 2014-2023 OpenEEmeter contributors

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

"""

import logging

from .__version__ import __title__, __description__, __url__, __version__
from .__version__ import __author__, __author_email__, __license__
from .__version__ import __copyright__
from .eemeter.exceptions import *
from .eemeter.features import *
from .eemeter.io import *
from .eemeter.samples.load import *
from .eemeter.segmentation import *
from .eemeter.transform import *
from .eemeter.visualization import *
from .eemeter.warnings import *
from .eemeter.models.hourly.derivatives import *
from .eemeter.models.hourly.metrics import *
from .eemeter.models import *
from .eemeter.models.hourly.wrapper import HourlyModel
from .eemeter.models.hourly.data import HourlyBaselineData, HourlyReportingData


def get_version():
    return __version__


# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())
