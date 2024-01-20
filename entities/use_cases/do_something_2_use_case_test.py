import pytest

from entities.use_cases.do_something_2_use_case import DoSomething2UseCase


class TestDoSomething2UseCase:
    @pytest.fixture()
    def do_something_2_use_case(self) -> DoSomething2UseCase:
        return DoSomething2UseCase()

    def test_call(
        self,
        do_something_2_use_case: DoSomething2UseCase,
    ) -> None:
        # Arrange
        input_ = DoSomething2UseCase.Input(
            param_1=1,
            param_2=2,
            param_3=3,
        )

        # Act
        response = do_something_2_use_case(input_)

        # Assert
        assert response.param_1 == 1
        assert response.param_2 == 2
        assert response.param_3 == 3
