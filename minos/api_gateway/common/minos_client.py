# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.

"""MinosClient is a base class that implements Circuit Breaker pattern.

This module serves as a base class to later extend it and use it with HTTP, RPC ...
"""

from abc import ABC, abstractmethod
import pybreaker


class MinosClient(ABC):
    """Class that implements Circuit Breaker Pattern.

    Attributes:
        cb_fail_max: Integer which specifies a Circuit Breaker max fails.
        cb_reset_timeout: Integer which specifies a Circuit Breaker unlock time.
    """ 
    
    def initialize_circuitbreaker(self, cb_fail_max:int, cb_reset_timeout:int):
        """Circuit Breaker initializer"""
        return pybreaker.CircuitBreaker(fail_max=cb_fail_max, reset_timeout=cb_reset_timeout)