# -*- coding: utf-8 -*-

from .aggregate_base import AggregateBase
from .aggregate_states import ChargeTransferState

class AggregateCT(AggregateBase):
    """
    Class enables adding of charge-transfer states into the aggregate
    """

    def add_CTState(self, state1, state2):
        pass
        #ChargeTransferState(state1,state2)