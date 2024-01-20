import pytest

from services.do_something_1_service import DoSomething1Service


class TestDoSomething1Service:
    @pytest.fixture()
    def do_something_1_service(self) -> DoSomething1Service:
        return DoSomething1Service()

    def test_call(
        self,
        do_something_1_service: DoSomething1Service,
    ) -> None:
        # Arrange
        input_ = DoSomething1Service.Input(
            param_1="Hello",
            param_2="World",
            param_3="!",
        )

        # Act
        response = do_something_1_service(input_)

        # Assert
        assert response.param_1 == "Hello"
        assert response.param_2 == "World"
        assert response.param_3 == "!"
