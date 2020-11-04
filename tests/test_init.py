import pytest

import asahi


def test_init() -> None:
    assert asahi

    assert isinstance(asahi.__version_info__, tuple)
    assert asahi.__version_info__
    assert isinstance(asahi.__version__, str)
    assert len(asahi.__version__)


def test_extras() -> None:
    import asahi.extras
    from asahi import extras

    assert asahi.extras
    assert extras
    assert asahi.extras == extras
    assert asahi.extras == getattr(asahi, "extras")

    assert isinstance(asahi.extras.__version_info__, tuple)
    assert asahi.extras.__version_info__
    assert isinstance(asahi.extras.__version__, str)
    assert len(asahi.extras.__version__)

    assert isinstance(extras.__version_info__, tuple)
    assert extras.__version_info__
    assert isinstance(extras.__version__, str)
    assert len(extras.__version__)


def test_bad_asahi_import() -> None:
    with pytest.raises(ModuleNotFoundError):
        import asahi.shoganai  # noqa  # isort:skip

    with pytest.raises(ImportError):
        from asahi import shoganeee  # noqa  # isort:skip


def test_access_bad_attribute() -> None:
    with pytest.raises(AttributeError):
        asahi.shokattaganai

    with pytest.raises(AttributeError):
        getattr(asahi, "badattribute")
