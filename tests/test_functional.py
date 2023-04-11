import os

import docker

dir_path = os.path.dirname(os.path.realpath(__file__))

client = docker.from_env()


def test_file_contents():
    events = []
    targets = ['target_001', 'target_002']
    file_path = '/usr/src/app/events.log'
    with open(f'{dir_path}/resources/large_1M_events.log', 'r') as file:
        expected_events = [line.rstrip() for line in file]

    for target in targets:
        container = client.containers.get(target)
        cmd = f'cat {file_path}'
        _, stream = container.exec_run(cmd=cmd, stream=True)
        for data in stream:
            events.append(data.decode())

    assert len(expected_events) == len(events)

    expected_events = set(expected_events)
    events = set(events)

    assert len(events) == len(expected_events), 'Number of records is not the same'
    diff = expected_events - expected_events.intersection(events)
    assert diff == {}, 'These elements were not correctly processed'
