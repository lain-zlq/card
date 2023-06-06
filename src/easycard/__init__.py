import pandas
import warnings
from .exceptions import CardDependencyWarning

def check_compatibility(click_version):
    click_version = click_version.split('.')
    assert click_version != ['dev']

    if len(click_version) == 2:
        click_version.append('0')

    major, minor, patch = click_version
    major, minor, patch = int(major), int(minor), int(patch)
    # pandas >= 2.0.0
    assert major == 2
    assert minor >= 0
    assert minor >= 0

# 验证依赖包版本
try:
    check_compatibility(pandas.__version__, pandas.__version__)
except (AssertionError, ValueError):
    warnings.warn("pandas ({}) doesn't match a supported "
                  "version!".format(pandas.__version__),
                  CardDependencyWarning)
    
from .__version__ import __title__, __description__, __version__, __author__

from .verify import bank_no_verify
from .find import find_bank_no