import pytest

from use_cases.do_something_3_use_case import DoSomething3UseCase


class TestDoSomething3UseCase:
    @pytest.fixture()
    def do_something_3_use_case(self) -> DoSomething3UseCase:
        return DoSomething3UseCase()

    def test_call(
        self,
        do_something_3_use_case: DoSomething3UseCase,
    ) -> None:
        # Arrange
        input_ = DoSomething3UseCase.Input(
            param_1=[],
            param_2={},
            param_3=None,
        )

        # Act
        response = do_something_3_use_case(input_)

        # Assert
        assert response.param_1 == []
        assert response.param_2 == {}
        assert response.param_3 is None
