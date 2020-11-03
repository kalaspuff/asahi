import asahi


def test_init() -> None:
    assert asahi

    assert isinstance(asahi.__version_info__, tuple)
    assert asahi.__version_info__
    assert isinstance(asahi.__version__, str)
    assert len(asahi.__version__)
