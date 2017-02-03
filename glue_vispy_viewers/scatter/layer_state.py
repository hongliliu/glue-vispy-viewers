from __future__ import absolute_import, division, print_function

from glue.config import colormaps
from glue.external.echo import CallbackProperty
from glue.core.state_objects import StateAttributeLimitsHelper
from ..common.layer_state import VispyLayerState

__all__ = ['ScatterLayerState']


class ScatterLayerState(VispyLayerState):
    """
    A state object for volume layers
    """

    size_mode = CallbackProperty('Fixed')
    size = CallbackProperty()
    size_attribute = CallbackProperty()
    size_vmin = CallbackProperty()
    size_vmax = CallbackProperty()
    size_scaling = CallbackProperty(1)

    color_mode = CallbackProperty('Fixed')
    color = CallbackProperty()
    cmap_attribute = CallbackProperty()
    cmap_vmin = CallbackProperty()
    cmap_vmax = CallbackProperty()
    cmap = CallbackProperty()
    alpha = CallbackProperty()

    def __init__(self, **kwargs):

        super(ScatterLayerState, self).__init__(**kwargs)

        if self.layer is not None:

            if self.cmap_attribute is None:
                self.cmap_attribute = self.layer.visible_components[0]

            if self.size_attribute is None:
                self.size_attribute = self.layer.visible_components[0]

            self.color = self.layer.style.color
            self.size = self.layer.style.markersize
            self.alpha = self.layer.style.alpha

        self.size_att_helper = StateAttributeLimitsHelper(self, attribute='size_attribute',
                                                          lower='size_vmin', upper='size_vmax')

        self.cmap_att_helper = StateAttributeLimitsHelper(self, attribute='cmap_attribute',
                                                          lower='cmap_vmin', upper='cmap_vmax')

        if self.cmap is None:
            self.cmap = colormaps.members[0][1]
