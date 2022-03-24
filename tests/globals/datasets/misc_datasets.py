import pytest

from sklearn.cluster import KMeans

from typing import Dict, List, NamedTuple

from relevanceai import Client

from tests.globals.constants import generate_dataset_id


@pytest.fixture(scope="function")
def obj_dataset_id(test_client: Client, dataclass_documents: List[NamedTuple]):
    test_dataset_id = generate_dataset_id()

    test_client._insert_documents(test_dataset_id, dataclass_documents)

    yield test_dataset_id

    test_client.datasets.delete(test_dataset_id)


@pytest.fixture(scope="function")
def clustered_dataset_id(test_client: Client, vector_documents: List[Dict]):
    test_dataset_id = generate_dataset_id()

    test_client._insert_documents(test_dataset_id, vector_documents)

    dataset = test_client.Dataset(test_dataset_id)
    dataset.cluster(
        model=KMeans(n_clusters=10),
        vector_fields=["sample_1_vector_"],
        alias="kmeans-10",
    )
    yield test_dataset_id

    test_client.datasets.delete(test_dataset_id)
