"""
Tests for the ExampleComponent class, essentially showcases how to implement basic tests on a Component.
"""

from psychopy_legacy.components.ratingScale import RatingScaleComponent
from psychopy.tests.test_experiment.test_components.test_base_components import BaseComponentTests

class TestRatingScaleComponent(BaseComponentTests):
    comp = RatingScaleComponent
