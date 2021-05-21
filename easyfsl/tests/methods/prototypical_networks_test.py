import torch
from torchvision.models import mobilenet_v2

from easyfsl.methods import PrototypicalNetworks


class TestPrototypicalNetworksPipeline:
    @staticmethod
    def test_prototypical_networks_returns_expected_output_for_example_images(
        example_few_shot_classification_task,
    ):
        (
            support_images,
            support_labels,
            query_images,
        ) = example_few_shot_classification_task

        torch.manual_seed(1)
        model = PrototypicalNetworks(mobilenet_v2())

        model.process_support_set(support_images, support_labels)
        predictions = model(query_images)

        # pylint: disable=not-callable
        assert torch.all(
            torch.isclose(
                predictions,
                torch.tensor(
                    [[-7.8325, -9.6273], [-8.1752, -10.2638]],
                ),
            )
        )
        # pylint: enable=not-callable
