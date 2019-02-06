# Copyright 2017 Neural Networks and Deep Learning lab, MIPT
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


import numpy as np

from deeppavlov.core.common.registry import register
from deeppavlov.core.common.log import get_logger
from deeppavlov.core.models.estimator import Component

logger = get_logger(__name__)


@register("hybrid_ranker_predictor")
class HybridRankerPredictor(Component):

    def __init__(self,
                 sample_size,
                 **kwargs):
        self.sample_size = sample_size


    def __call__(self, candidates_batch, preds_batch):
        """
        return list of best responses and its confidences
        """

        responses_preds = []
        responses_batch = []

        for i in range(len(candidates_batch)):
            sorted_ids = np.flip(np.argsort(preds_batch[i]), -1)  # choose a random answer as the best one
            chosen_index = np.random.choice(sorted_ids[:self.sample_size])

            responses_batch.append(candidates_batch[i][chosen_index])
            responses_preds.append(preds_batch[i][chosen_index])

        return responses_batch, responses_preds