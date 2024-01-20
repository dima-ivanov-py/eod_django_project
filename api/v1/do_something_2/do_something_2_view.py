from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.do_something_2.do_something_2_interactor import (
    DoSomething2Interactor,
)


class DoSomething2View(APIView):
    def post(self, request):
        do_something_2_interactor = DoSomething2Interactor()
        input_ = DoSomething2Interactor.Input(
            param_1=request.POST["param_1"],
            param_2=request.POST["param_2"],
            param_3=request.POST["param_3"],
        )

        try:
            output: DoSomething2Interactor.Output = do_something_2_interactor(
                input_
            )
        except DoSomething2Interactor.Error as e:
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
