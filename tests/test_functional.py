from _pytest.fixtures import fixture


@fixture
def all_gathered_events(gathered_events) -> list:
    return sorted(event for t_list in gathered_events.values() for event in t_list)


def test_number_of_events(all_gathered_events, expected_events):
    """
    The purpose fo this test is to validate the correctness of processed data.
    Test reads events.log file on both targets and check total number of processed events
    """

    assert len(expected_events) == len(all_gathered_events), 'Number of records is not the same'


def test_not_processed_events(all_gathered_events, expected_events):
    """
    The purpose fo this test is to validate the correctness of processed data.
    Test reads events.log file on both targets and check if all events were processed
    """

    expected_events = set(expected_events)

    diff = expected_events - expected_events.intersection(set(all_gathered_events))
    assert diff == {}, 'These elements were not correctly processed'


def test_trash_events(all_gathered_events, expected_events):
    """
    The purpose fo this test is to validate the correctness of processed data.
    Test reads events.log file on both targets and check for trash data
    """
    events = set(all_gathered_events)

    diff = events - events.intersection(set(set(expected_events)))
    assert diff == {}, 'These are trash elements found during processing'


def test_process_equality(gathered_events):
    """
    The purpose fo this test is to validate the equality of data split between targets
    """
    target = None
    events = []
    for t, e in gathered_events.items():
        if not target:
            target = t
            events = e
        else:
            assert len(e) == len(events), f'Number of processed items differs between {t} and {target}'
