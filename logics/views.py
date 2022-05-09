from multiprocessing import managers
from xmlrpc.client import Boolean

from pkg_resources import empty_provider
from rest_framework import views
from logics.models import Policies
from rest_framework.response import Response
from logics.models import Employee, AcceptedPolicies, Policies
import logging
import json
from rest_framework.decorators import authentication_classes,\
                                    permission_classes

from rest_framework.status import HTTP_200_OK

from logics.managers import PoliciyManager, PolicyAcceptManager


logger = logging.getLogger(__name__)

@authentication_classes([])
@permission_classes([])
class Login(views.APIView):
    def post(self, request):
        data = json.loads(request.body)
        emp_id = data['emp_id']
        employee_details = Employee.objects.get(emp_id=emp_id)
        if(employee_details.need_accept): #Employee needs to accept
            pending_policies = PoliciyManager(emp_id, employee_details.role.lower()).get_pending_policies()
            if(len(pending_policies['pending_policies']) > 0):
                return Response({
                 "result": data,
                 "message": 'following needs to be accepted',
                  }, status=HTTP_200_OK)

        return Response({
        "message": 'no policy to accept',
         }, status=HTTP_200_OK)

class AcceptPolicy(views.APIView):


    def post(self, request):
        try:
            data = json.loads(request.body)
            emp_details = Employee.objects.get(emp_id=data['emp_id'])
            policy_id = data['policy_pk']
            new_user = data['new_user']
            AcceptedPolicies.objects.create(
                fk_employee = emp_details,
                is_periodic = not bool(new_user),
                fk_policy = Policies.object.get(pk=policy_id)
            )
            if(len(PoliciyManager(data['emp_id'], emp_details.role.lower()).get_pending_policies()['pending_policies']) == 0):
                emp_details.need_to_accept = False  # Can be threaded
                emp_details.save()
            return Response({
             "message": 'accepted',
               }, status=HTTP_200_OK)

        except Exception as error:
            logger.error('Request failed with error: ' + str(error))
            return str(error)

class CustomPolicyGenerate(views.APIView):
    def post(self, request):
        data = json.loads(request.body)
        custom_acks = data['emp_ids'] #Expects array of employee IDS
        PolicyAcceptManager().accept_policies(custom_acks)




