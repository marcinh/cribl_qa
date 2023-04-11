import os

import docker
from docker import DockerClient
from pytest import fixture

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
FILE_PATH = '/usr/src/app/events.log'
TARGETS = ['target_001', 'target_002']


@fixture
def client() -> DockerClient:
    return docker.from_env()


def gather_events_from_targets(client, targets: list) -> dict:
    output = {}
    for target in targets:
        container = client.containers.get(target)
        cmd = f'cat {FILE_PATH}'
        _, stream = container.exec_run(cmd=cmd, stream=True)
        whole = ''
        for data in stream:
            whole += data.decode()
        output[target] = whole.splitlines()

    return output


@fixture
def gathered_events(client) -> dict:
    return gather_events_from_targets(client, TARGETS)


@fixture
def expected_events() -> list:
    with open(f'{DIR_PATH}/resources/large_1M_events.log', 'r') as file:
        return [line.rstrip() for line in file]
