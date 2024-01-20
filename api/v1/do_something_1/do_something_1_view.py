from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.do_something_1.do_something_1_interactor import (
    DoSomething1Interactor,
)


class DoSomething1View(APIView):
    def post(self, request):
        do_something_1 = DoSomething1Interactor()
        input_ = DoSomething1Interactor.Input(
            param_1=request.POST["param_1"],
            param_2=request.POST["param_2"],
            param_3=request.POST["param_3"],
        )

        try:
            output: DoSomething1Interactor.Output = do_something_1(input_)
        except DoSomething1Interactor.Error as e:
            response = Response(
                data={"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            response = Response(
                data={
                    "param_1": output.param_1,
                    "param_2": output.param_2,
                    "param_3": output.param_3,
                },
                status=status.HTTP_200_OK,
            )

        return response
