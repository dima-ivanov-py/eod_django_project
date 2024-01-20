import pytest

from entities.use_cases.do_something_1_use_case import DoSomething1UseCase


class TestDoSomething1UseCase:
    @pytest.fixture()
    def do_something_1_use_case(self) -> DoSomething1UseCase:
        return DoSomething1UseCase()

    def test_call(
        self,
        do_something_1_use_case: DoSomething1UseCase,
    ) -> None:
        # Arrange
        input_ = DoSomething1UseCase.Input(
            param_1="Hello",
            param_2="World",
            param_3="!",
        )

        # Act
        response = do_something_1_use_case(input_)

        # Assert
        assert response.param_1 == "Hello"
        assert response.param_2 == "World"
        assert response.param_3 == "!"
